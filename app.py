import streamlit as st
import time

st.set_page_config(page_title="זיהוי התקף", layout="centered")

st.title("💓 אפליקציית התמודדות עם התקף חרדה")

st.write("ברגע שהמערכת מזהה סימנים מוקדמים, היא מציגה את המסך הזה כדי לסייע למשתמש.")

# כפתור הפעלה
if st.button("🔍 הדגם זיהוי התקף"):
    st.warning("⚠ סימנים מוקדמים להתקף זוהו!")
    time.sleep(1)
    
    # שלב 1: טקסט מרגיע
    st.markdown("### 💬 את לא לבד.\n#### זה יעבור. בואי ננשום יחד.")
    
    # שלב 2: תרגול נשימה מודרך
    st.markdown("---")
    st.markdown("### 🌬 תרגול נשימה מודרך")
    
    for i in range(3):
        st.markdown("#### שאיפה... 🫁")
        time.sleep(4)
        st.markdown("#### החזקה...")
        time.sleep(2)
        st.markdown("#### נשיפה איטית... 😌")
        time.sleep(6)
        st.markdown("---")
    
    # שלב 3: הודעה לאיש קשר
    st.markdown("### 📲 התרעה לאיש קשר חירום תישלח בעוד 10 שניות...")
    cancel = st.button("❌ בטלי שליחת הודעה")
    
    if not cancel:
        time.sleep(10)
        if not st.session_state.get("cancelled", False):
            st.success("הודעה נשלחה למיכל. 📤")
        else:
            st.info("השליחה בוטלה.")
    else:
        st.session_state["cancelled"] = True
        st.info("השליחה בוטלה.")

st.markdown("---")
st.caption("גרסה לדמו בלבד | האקתון שיקום 2025")


