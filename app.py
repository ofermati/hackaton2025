import streamlit as st
import json
from pathlib import Path
import pandas as pd
import time

st.set_page_config(page_title="זיהוי התקף", layout="centered")

st.title("💓 ניטור התקף חרדה - בזמן אמת")

json_path = Path("status.json")
placeholder = st.empty()  # אזור תוכן משתנה
history_path = Path("history.json")

# ניהול מצב התקף קודם
if "alert_triggered" not in st.session_state:
    st.session_state.alert_triggered = False

# כפתור איפוס
if st.button("🔄 סיימתי את התרגול, איפוס מצב"):
    st.session_state.alert_triggered = False
    st.success("המערכת אופסה. ברוך השב!")

# אזור קבוע - תגובת הרגעה ראשונה
if st.session_state.alert_triggered:
    st.warning("⚠️ התקף זוהה! מופעלת תגובת הרגעה...")
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
    st.video("https://www.youtube.com/watch?v=1ZYbU82GVz4")
    st.info("🌿 נראה שהמערכת יציבה. המשך כך, אתה עושה עבודה מעולה!")

# לולאת רענון של אזור הדופק בלבד (לייב)
for _ in range(1):
    if json_path.exists():
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        heart_rate = data.get("heart_rate")
        attack = data.get("attack_detected")
        timestamp = data.get("timestamp")

        # שמירת היסטוריה לגרף
        if history_path.exists():
            with open(history_path, "r", encoding="utf-8") as f:
                data_history = json.load(f)
        else:
            data_history = []

        data_history.append({"זמן": timestamp, "דופק": heart_rate})
        with open(history_path, "w", encoding="utf-8") as f:
            json.dump(data_history[-50:], f, ensure_ascii=False, indent=2)

        with placeholder.container():
            st.metric("💓 דופק נוכחי", f"{heart_rate} bpm")
            st.caption(f"עודכן ב־{timestamp}")

            if len(data_history) > 1:
                df = pd.DataFrame(data_history[-30:])
                st.line_chart(df.set_index("זמן"))

            # הפעלת תגובה ראשונה רק פעם אחת
            if attack and not st.session_state.alert_triggered:
                st.session_state.alert_triggered = True
                st.rerun()
    time.sleep(0.5)
