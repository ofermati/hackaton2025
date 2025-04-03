import streamlit as st
import pandas as pd
import json
from pathlib import Path
import altair as alt

st.set_page_config(page_title="📊 סטטיסטיקות", layout="centered")

st.title("📊 דוח סטטיסטיקות - ניטור והרגעה")

history_path = Path("history.json")

st.markdown("---")

if history_path.exists():
    with open(history_path, "r", encoding="utf-8") as f:
        data_history = json.load(f)

    df = pd.DataFrame(data_history)
    df['זמן'] = pd.to_datetime(df['זמן'])

    # סינון לפי טווח תאריכים
    min_date = df['זמן'].min().date()
    max_date = df['זמן'].max().date()
    start_date, end_date = st.date_input("בחר טווח תאריכים", [min_date, max_date], min_value=min_date, max_value=max_date)

    df = df[(df['זמן'].dt.date >= start_date) & (df['זמן'].dt.date <= end_date)]

    st.subheader("📈 גרף היסטורי של הדופק")
    attack_threshold = 110
    df['התקף'] = df['דופק'] > attack_threshold

    chart = alt.Chart(df).mark_line().encode(
        x='זמן:T',
        y='דופק:Q',
        color=alt.condition(
            alt.datum.התקף,
            alt.value('red'),  # התקף בצבע אדום
            alt.value('green')  # רגוע בצבע ירוק
        )
    ).properties(height=300)

    st.altair_chart(chart, use_container_width=True)

    st.markdown("---")
    st.subheader("📋 נתונים סטטיסטיים כלליים")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("ממוצע דופק", f"{df['דופק'].mean():.1f} bpm")
    with col2:
        st.metric("דופק מקסימלי", f"{df['דופק'].max()} bpm")
    with col3:
        st.metric("דופק מינימלי", f"{df['דופק'].min()} bpm")

    st.markdown("---")
    st.subheader("⚠️ זיהוי התקפים")
    attack_periods = df[df['התקף']]

    if not attack_periods.empty:
        st.success(f"נמצאו {len(attack_periods)} מדידות שמצביעות על התקף.")
        st.dataframe(attack_periods.tail(10), use_container_width=True)
    else:
        st.info("✨ לא נמצאו התקפים בתקופה האחרונה!")

    st.markdown("---")
    st.download_button("⬇️ הורד את הנתונים כ-CSV", data=df.to_csv(index=False), file_name="history.csv", mime="text/csv")

else:
    st.warning("לא נמצאו נתונים להצגה. אנא הפעל את ניטור הדופק תחילה.")
