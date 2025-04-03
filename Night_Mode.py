import streamlit as st
import json
from pathlib import Path
from streamlit_autorefresh import st_autorefresh

# חייב לבוא ראשון!
st.set_page_config(page_title="מצב לילה 🌙", layout="centered")

# CSS כהה
st.markdown("""
    <style>
    body {
        background-color: #111 !important;
        color: #eee !important;
    }
    .stApp {
        background-color: #111 !important;
    }
    .block-container {
        padding-top: 2rem;
        color: #eee;
    }
    .metric-label, .metric-value {
        color: #eee !important;
    }
    button {
        background-color: #444 !important;
        color: #fff !important;
    }
    </style>
""", unsafe_allow_html=True)

# כפתור לחזרה
col1, col2, col3 = st.columns([1, 3, 1])
with col3:
    if st.button("☀️"):
        st.switch_page("app.py")

# כותרת
st.title("🌙 ניטור במצב לילה")

# רענון אוטומטי
st_autorefresh(interval=1000, key="refresh-night")

# קריאת נתונים
json_path = Path("status.json")

if json_path.exists():
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    hr = data["heart_rate"]
    sweat = data["sweat_level"]
    move = data["movement"]
    attack = data["attack_detected"]
    timestamp = data["timestamp"]

    st.markdown(f"**עודכן בתאריך:** {timestamp}")

    col1, col2, col3 = st.columns(3)
    col1.metric("💓 דופק", f"{hr} bpm")
    col2.metric("💦 הזעה", f"{sweat:.2f}")
    col3.metric("🏃 תנועה", move)

    if "was_attack" not in st.session_state:
        st.session_state.was_attack = False

    if attack:
        st.session_state.was_attack = True
        st.error("⚠️ התקף מזוהה! מצב לילה מופעל להרגעה.")
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3")
        st.video("https://www.youtube.com/watch?v=2OEL4P1Rz04")  # וידאו רגוע אחר
    elif st.session_state.was_attack:
        st.success("🌿 נראה שחזרת לאיזון. כל הכבוד.")
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3")
        st.video("https://www.youtube.com/watch?v=2OEL4P1Rz04")
    else:
        st.info("🌙 ניטור פעיל. הכל רגוע.")

else:
    st.warning("אין נתונים עדיין...")
