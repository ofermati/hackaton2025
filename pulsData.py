import json
import time
import random

# שלב 1: דופק רגוע (40 פולסים)
for i in range(40):
    heart_rate = random.randint(60, 80)
    sweat_level = random.uniform(0.1, 0.4)  # הזעה רגועה
    movement = random.choice(["low", "very low"])
    attack_detected = heart_rate > 110 or sweat_level > 0.7
    data = {
        "heart_rate": heart_rate,
        "sweat_level": round(sweat_level, 2),
        "movement": movement,
        "attack_detected": attack_detected,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    with open("status.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"💓 דופק: {heart_rate} | הזעה: {sweat_level:.2f} | תנועה: {movement} | התקף? {attack_detected}")
    time.sleep(0.5)

# שלב 2: התקף חרדה (60 פולסים)
for i in range(60):
    heart_rate = random.randint(115, 130)
    sweat_level = random.uniform(0.7, 1.0)  # הזעה גבוהה
    movement = random.choice(["high", "very high"])
    attack_detected = heart_rate > 110 or sweat_level > 0.7
    data = {
        "heart_rate": heart_rate,
        "sweat_level": round(sweat_level, 2),
        "movement": movement,
        "attack_detected": attack_detected,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    with open("status.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"💓 דופק: {heart_rate} | הזעה: {sweat_level:.2f} | תנועה: {movement} | התקף? {attack_detected}")
    time.sleep(0.5)

# שלב 3: חזרה למצב רגוע בלולאה אינסופית
while True:
    heart_rate = random.randint(60, 80)
    sweat_level = random.uniform(0.2, 0.5)
    movement = random.choice(["low", "very low"])
    attack_detected = heart_rate > 110 or sweat_level > 0.7
    data = {
        "heart_rate": heart_rate,
        "sweat_level": round(sweat_level, 2),
        "movement": movement,
        "attack_detected": attack_detected,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    with open("status.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"💓 דופק: {heart_rate} | הזעה: {sweat_level:.2f} | תנועה: {movement} | התקף? {attack_detected}")
    time.sleep(0.5)
