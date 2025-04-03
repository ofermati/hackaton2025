import streamlit as st
import time
import random

st.set_page_config(page_title="Relaxation Response", layout="centered")

# כותרת
st.title("מערכת תגובת הרגעה בזמן אמת")

# הדמיה של נתוני בריאות
heart_rate = st.slider("דופק נוכחי", 60, 140, 75)
sleep_quality = st.selectbox("איכות שינה", ["טובה", "סבירה", "רעה"])
movement = st.selectbox("תנועה", ["נמוכה", "בינונית", "גבוהה"])

# הצגת גרפים או הודעות
if heart_rate > 100 or movement == "גבוהה" or sleep_quality == "רעה":
    st.warning("זוהה מצב סטרס! מופעלת תגובה מרגיעה...")
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
    
    with st.expander("תרגיל נשימה מודרכת"):
        st.markdown("נשום פנימה... ✨")
        st.progress(0)
        for i in range(1, 101):
            time.sleep(0.02)
            st.progress(i)
        st.markdown("נשוף החוצה... 🌬️")

else:
    st.success("הכל נראה תקין – המשך כך!")

