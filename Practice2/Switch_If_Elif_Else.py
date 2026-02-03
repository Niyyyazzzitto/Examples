score = 78
if score >= 90:
    print("A")
elif score >= 75:
    print("B")
elif score >= 60:
    print("C")
else:
    print("F")

n = 13
if n % 2 == 0:
    print("четное")
else:
    print("нечетное")

t = 5
if t < 0:
    print("мороз")
elif t < 15:
    print("прохладно")
else:
    print("тепло")

op = "*"
a, b = 2, 5
actions = {
    "+": a + b,
    "-": a - b,
    "*": a * b,
    "/": a / b if b != 0 else "деление на ноль",
}
print(actions.get(op, "неизвестная операция"))

