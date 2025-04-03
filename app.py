import streamlit as st
import json
import time
from pathlib import Path

st.set_page_config(page_title="זיהוי התקף", layout="centered")
st.title("💓 ניטור התקף חרדה - בזמן אמת")

json_path = Path("status.json")

placeholder = st.empty()  # מקום להודעות

while True:
    if json_path.exists():
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        heart_rate = data.get("heart_rate")
        attack = data.get("attack_detected")
        timestamp = data.get("timestamp")

        st.metric("💓 דופק", heart_rate)
        st.caption(f"עודכן ב־{timestamp}")

        if attack:
            placeholder.warning("⚠️ התקף זוהה! מפעיל תגובה מרגיעה...")
            st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
            st.video("https://www.youtube.com/watch?v=1ZYbU82GVz4")  # מדיטציה
            break  # מפסיקים את הלולאה אחרי זיהוי
        else:
            placeholder.success("✅ מצב תקין")
    time.sleep(2)
