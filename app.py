import streamlit as st
import json
import pandas as pd
from pathlib import Path
from streamlit_autorefresh import st_autorefresh

st.set_page_config(page_title="ניטור חכם", layout="centered")

# עיצוב הכפתור בצד ימין למעלה
col1, col2, col3, col4, col5, col6 = st.columns([1, 1, 1, 1, 1, 1])
with col6:
    if st.button("🌙"):
        st.switch_page("Night_Mode.py")


st.title("📡 ניטור בזמן אמת")

# מרענן את העמוד כל 1 שנייה (1000 מילישניות)
st_autorefresh(interval=1000, key="refresh")

# קובץ נתונים
json_path = Path("status.json")

# קריאה מהקובץ
if json_path.exists():
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    hr = data["heart_rate"]
    sweat = data["sweat_level"]
    move = data["movement"]
    attack = data["attack_detected"]
    timestamp = data["timestamp"]

    # תצוגה
    st.markdown(f"**עודכן בתאריך:** {timestamp}")

    col1, col2, col3 = st.columns(3)
    col1.metric("💓 דופק", f"{hr} bpm", delta=None)
    col2.metric("💦 הזעה", f"{sweat:.2f}", delta=None)
    col3.metric("🏃 תנועה", move)

    # נשתמש במשתנה לזיהוי האם התקף התרחש בעבר
    if "was_attack" not in st.session_state:
        st.session_state.was_attack = False

    if attack:
        st.session_state.was_attack = True
        st.error("המדדים השתנו, בוא ננסה להרגע ביחד")
            # טקסט ופרטי השיר
        st.markdown("### 🎶 עכשיו מתנגן:")
        st.markdown("*Bohemian Rhapsody - Queen*")
        st.audio("https://drive.google.com/uc?export=download&id=1sShXwsYsx0uUF3LrSXUimi1W4RBNCVbS")
        st.video("https://www.youtube.com/watch?v=1ZYbU82GVz4")

    elif st.session_state.was_attack:
        st.success("🌿 המצב התייצב! כל הכבוד.")
        st.audio("https://drive.google.com/uc?export=download&id=1sShXwsYsx0uUF3LrSXUimi1W4RBNCVbS")
        st.video("https://www.youtube.com/watch?v=1ZYbU82GVz4")
        if st.button("📊 עבור לדף הסטטיסטיקות"):
            st.switch_page("Statistics_Dashboard.py")  # ודא שהשם תואם לשם הקובץ שלך
    else:
        st.success("✅ המצב רגוע")


