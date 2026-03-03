import re
import json
from decimal import Decimal, InvalidOperation

# ----------------------------
# Helpers
# ----------------------------

def norm_money(s: str) -> str:
    """
    "1 200,00" -> "1200.00"
    "308,00"   -> "308.00"
    """
    s = s.strip()
    s = s.replace(" ", "")      # remove thousand spaces
    s = s.replace("\u00a0", "") # remove non-breaking spaces
    s = s.replace(",", ".")     # decimal comma -> dot
    return s

def to_decimal(s: str):
    try:
        return Decimal(norm_money(s))
    except (InvalidOperation, ValueError):
        return None

# ----------------------------
# 1) Extract ALL prices (any money like 308,00 or 1 200,00)
# ----------------------------
PRICE_RE = re.compile(r"\b\d{1,3}(?:[ \u00a0]\d{3})*,\d{2}\b|\b\d+,\d{2}\b")

def extract_all_prices(text: str):
    return [norm_money(x) for x in PRICE_RE.findall(text)]

# ----------------------------
# 4) Date & time
# "Время: 18.04.2019 11:13:58"
# ----------------------------
DATETIME_RE = re.compile(r"Время:\s*(\d{2}\.\d{2}\.\d{4})\s+(\d{2}:\d{2}:\d{2})")

def extract_datetime(text: str):
    m = DATETIME_RE.search(text)
    if not m:
        return {"date": None, "time": None}
    return {"date": m.group(1), "time": m.group(2)}

# ----------------------------
# 5) Payment method
# "Банковская карта:" or "Наличные:" etc.
# ----------------------------
PAYMENT_RE = re.compile(r"^(Банковская карта|Наличные|Карта|Cash|VISA|MasterCard)\s*:", re.MULTILINE | re.IGNORECASE)

def extract_payment_method(text: str):
    m = PAYMENT_RE.search(text)
    if not m:
        return None
    return m.group(1)

# ----------------------------
# 2) Product names + 3) totals per item
#
# Item block pattern (your чек):
# 1.
# Натрия хлорид ...
# 2,000 x 154,00
# 308,00
# Стоимость
# 308,00
#
# We'll extract:
# - name (line after "n.")
# - qty and unit price (line "2,000 x 154,00")
# - line total (the line right after qty x price)
# ----------------------------
ITEM_START_RE = re.compile(r"^\s*(\d+)\.\s*$", re.MULTILINE)
QTY_UNIT_RE = re.compile(r"^\s*(\d+,\d{3})\s*x\s*([\d \u00a0]+,\d{2})\s*$", re.MULTILINE)

def parse_items(text: str):
    lines = [ln.rstrip() for ln in text.splitlines()]
    items = []

    i = 0
    while i < len(lines):
        # detect "n."
        if re.fullmatch(r"\s*\d+\.\s*", lines[i]):
            idx_line = lines[i].strip()
            # next non-empty line is name
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j >= len(lines):
                break
            name = lines[j].strip()

            # find qty x unit on next lines
            k = j + 1
            while k < len(lines) and not QTY_UNIT_RE.match(lines[k]):
                k += 1
            if k >= len(lines):
                # couldn't find qty/unit, still store name
                items.append({"name": name, "qty": None, "unit_price": None, "line_total": None})
                i = j + 1
                continue

            m = QTY_UNIT_RE.match(lines[k])
            qty = m.group(1)              # "2,000"
            unit_price = m.group(2)       # "154,00"

            # line total usually next non-empty line
            t = k + 1
            while t < len(lines) and not lines[t].strip():
                t += 1
            line_total = lines[t].strip() if t < len(lines) else None

            items.append({
                "name": name,
                "qty": qty.replace(",", "."),                # 2.000
                "unit_price": norm_money(unit_price),        # 154.00
                "line_total": norm_money(line_total) if line_total else None
            })

            i = t + 1
            continue

        i += 1

    return items

# ----------------------------
# 3) Calculate total amount
# Prefer "ИТОГО" value; fallback sum(line_total)
# ----------------------------
TOTAL_RE = re.compile(r"^ИТОГО:\s*([\d \u00a0]+,\d{2})\s*$", re.MULTILINE)
CARD_SUM_RE = re.compile(r"^Банковская карта:\s*([\d \u00a0]+,\d{2})\s*$", re.MULTILINE)

def extract_total(text: str, items):
    m = TOTAL_RE.search(text)
    if m:
        return norm_money(m.group(1))

    # fallback: sum of item totals
    s = Decimal("0")
    for it in items:
        if it["line_total"]:
            d = to_decimal(it["line_total"])
            if d is not None:
                s += d
    return str(s)

# ----------------------------
# Main parse
# ----------------------------
def parse_receipt(text: str):
    prices = extract_all_prices(text)
    dt = extract_datetime(text)
    payment = extract_payment_method(text)
    items = parse_items(text)
    total = extract_total(text, items)

    # Merchant name: first non-empty line
    merchant = None
    for ln in text.splitlines():
        ln = ln.strip()
        if ln:
            merchant = ln
            break

    return {
        "merchant": merchant,
        "date": dt["date"],
        "time": dt["time"],
        "payment_method": payment,
        "items": items,
        "prices_found": prices,
        "total_amount": total
    }

# Example usage:
# with open("raw.txt", "r", encoding="utf-8") as f:
#     text = f.read()
# print(json.dumps(parse_receipt(text), ensure_ascii=False, indent=2))