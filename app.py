import streamlit as st
import json
import time
from pathlib import Path
import pandas as pd

st.set_page_config(page_title="זיהוי התקף", layout="centered")
st.title("💓 ניטור התקף חרדה - בזמן אמת")

json_path = Path("status.json")
placeholder = st.empty()  # אזור תוכן משתנה

data_history = []  # רשימת היסטוריה לגרף

REFRESH_EVERY = 0.5  # כמה שניות בין עדכונים

while True:
    if json_path.exists():
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        heart_rate = data.get("heart_rate")
        attack = data.get("attack_detected")
        timestamp = data.get("timestamp")

        # שמור את הנתונים לגרף
        data_history.append({"זמן": timestamp, "דופק": heart_rate})

        with placeholder.container():
            st.metric("💓 דופק נוכחי", f"{heart_rate} bpm")
            st.caption(f"עודכן ב־{timestamp}")

            if len(data_history) > 1:
                df = pd.DataFrame(data_history[-30:])  # 30 רשומות אחרונות
                st.line_chart(df.set_index("זמן"))

            if attack:
                st.warning("⚠️ התקף זוהה! מפעיל תגובה מרגיעה...")
                st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
                st.video("https://www.youtube.com/watch?v=1ZYbU82GVz4")
                break
            else:
                st.success("✅ מצב תקין")

    time.sleep(REFRESH_EVERY)
    st.experimental_rerun()
