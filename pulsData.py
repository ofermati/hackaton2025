import json
import time
import random

# שלב 1: דופק רגוע (10 פולסים)
for i in range(40):
    heart_rate = random.randint(60, 80)
    attack_detected = heart_rate > 110  # פה תמיד False
    data = {
        "heart_rate": heart_rate,
        "attack_detected": attack_detected,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    with open("status.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"💓 דופק: {heart_rate} | התקף? {attack_detected}")
    time.sleep(0.5)

# שלב 2: דופק גבוה (התקף חרדה)
for i in range(60):
    heart_rate = random.randint(115, 130)
    attack_detected = heart_rate > 110  # פה תמיד True
    data = {
        "heart_rate": heart_rate,
        "attack_detected": attack_detected,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    with open("status.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"💓 דופק: {heart_rate} | התקף? {attack_detected}")
    time.sleep(0.5)

        # שלב 1: דופק רגוע (10 פולסים)
while True:
    heart_rate = random.randint(60, 80)
    attack_detected = heart_rate > 110  # פה תמיד False
    data = {
        "heart_rate": heart_rate,
        "attack_detected": attack_detected,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    with open("status.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"💓 דופק: {heart_rate} | התקף? {attack_detected}")
    time.sleep(0.5)
