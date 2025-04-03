import streamlit as st
import json
from pathlib import Path
import pandas as pd
from streamlit_autorefresh import st_autorefresh

st.set_page_config(page_title="זיהוי התקף", layout="centered")

json_path = Path("status.json")
history_path = Path("history.json")

st.title("💓 ניטור התקף חרדה - בזמן אמת")

# ניהול מצב התקף קודם
if "alert_triggered" not in st.session_state:
    st.session_state.alert_triggered = False
if "calm_detected" not in st.session_state:
    st.session_state.calm_detected = False
if "attack_start_time" not in st.session_state:
    st.session_state.attack_start_time = None
if "attack_end_time" not in st.session_state:
    st.session_state.attack_end_time = None

# כפתור איפוס
if st.button("🔄 סיימתי את התרגול, איפוס מצב"):
    st.session_state.alert_triggered = False
    st.session_state.calm_detected = False
    st.session_state.attack_start_time = None
    st.session_state.attack_end_time = None
    st.success("המערכת אופסה. ברוך השב!")

# קריאה ועדכון נתונים
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

    st.metric("💓 דופק נוכחי", f"{heart_rate} bpm")
    st.caption(f"עודכן ב־{timestamp}")

    if len(data_history) > 1:
        df = pd.DataFrame(data_history[-30:])
        st.line_chart(df.set_index("זמן"))

    # הפעלת תגובה ראשונה רק פעם אחת
    if attack and not st.session_state.alert_triggered:
        st.session_state.alert_triggered = True
        st.session_state.attack_start_time = timestamp

    # זיהוי הרגעה לאחר התקף
    if st.session_state.alert_triggered and not attack and not st.session_state.calm_detected:
        st.session_state.calm_detected = True
        st.session_state.attack_end_time = timestamp

# אזור קבוע - תגובת הרגעה ראשונה
if st.session_state.alert_triggered:
    st.warning("⚠️ התקף זוהה! מופעלת תגובת הרגעה...")
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
    st.video("https://www.youtube.com/watch?v=1ZYbU82GVz4")

# אזור הרגעה מלאה עם פרטי זמן התקף והמעבר לסטטיסטיקות
if st.session_state.calm_detected:
    st.success("🌿 נראה שהמערכת יציבה. המשך כך, אתה עושה עבודה מעולה!")
    if st.session_state.attack_start_time and st.session_state.attack_end_time:
        st.markdown(f"⏱️ זמן התקף: {st.session_state.attack_start_time} - {st.session_state.attack_end_time}")
    if st.button("📊 עבור לדף סטטיסטיקות"):
        st.switch_page("Statistics_Dashboard.py")
