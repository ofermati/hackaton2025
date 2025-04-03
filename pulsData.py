import json
import time
import random

while True:
    # מדמה דופק (אולי פתאום התקף חרדה)
    heart_rate = random.randint(108, 130)
    attack_detected = heart_rate > 110

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
    time.sleep(3)  # פולס כל 3 שניות
