import json
import os

SETTINGS_FILE = "settings.json"
LEADERBOARD_FILE = "leaderboard.json"

def load_settings():
    """Загружает настройки. Если файла нет, возвращает стандартные."""
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r") as f:
            return json.load(f)
    return {"sound": True, "color": "BLUE", "difficulty": "Medium"}

def save_settings(settings):
    """Сохраняет настройки в JSON."""
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f, indent=4)

def load_leaderboard():
    """Загружает таблицу лидеров."""
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r") as f:
            return json.load(f)
    return []

def save_score(name, score, distance):
    """Добавляет новый рекорд и оставляет только Топ-10."""
    lb = load_leaderboard()
    lb.append({"name": name, "score": score, "distance": distance})
    # Сортируем по убыванию очков и берем первые 10
    lb = sorted(lb, key=lambda x: x["score"], reverse=True)[:10]
    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(lb, f, indent=4)