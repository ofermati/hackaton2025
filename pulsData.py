import json
import time
import random

while True:
    attack_detected = heart_rate > 110
    # מדמה דופק (אולי פתאום התקף חרדה)
    for i in range (10):
        heart_rate = random.randint(60, 80)  # דופק בין 60 ל-80
        time.sleep(0.5)
    for i in range (10):
        heart_rate = random.randint(115, 130)
        time.sleep(0.5)

    # יוצרים מבנה נתונים
    data = {
        "heart_rate": heart_rate,
        "attack_detected": attack_detected,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

    # שומרים לקובץ JSON
    with open("status.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"שודר דופק: {heart_rate} | התקף? {attack_detected}")
    time.sleep(1)  # פולס כל 3 שניות
