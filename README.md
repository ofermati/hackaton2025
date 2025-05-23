﻿# hackaton2025
# 🌿 Smart Anxiety Detection & Relaxation System

A real-time mental wellness app that detects potential anxiety attacks using physiological signals, and responds instantly with calming actions like music, breathing exercises, emotional journaling, and alert messaging. Built during a 24h hackathon.

---

## 🎯 Project Goals

- Detect anxiety episodes using real-time signals: heart rate, sweat level, movement.
- Trigger calming responses: music, guided breathing, and emotional reflection.
- Notify support contacts if needed (via WhatsApp).
- Log all data sessions for post-analysis and tracking progress over time.

---

## ⚙️ Tech Stack

- **Python 3**
- **Streamlit** – interactive frontend
- **Pandas** – data management
- **Altair / Streamlit Charts** – visualization
- **Twilio API** – WhatsApp alerts
- **JSON files** – local session logs

---

## 🧩 Main Components

| File | Description |
|------|-------------|
| `Day_Mode.py` | Real-time dashboard with alert detection, relaxing music, video, and WhatsApp message |
| `Night_Mode🌙.py` | Night-friendly mode with dark theme, image and green noise instead of video |
| `pulsData.py` | Simulator for sensor data (HR, sweat, movement) with anxiety attack emulation |
| `status.json` | Current reading from the "sensor" |
| `history.json` | Historical heart rate data for graph display |
| `sessions.json` | Past anxiety sessions: start/end, average stats |
| `Statistics_Dashboard.py` | Summary dashboard with charts and analytics |
| `Notes_emotions.py` | Emotional journaling tool post-attack |
| `emotions_log.json` | Log of emotional entries |
| `Relaxing_breathing_session.py` | Guided breathing exercise using the 4-7-8 method |
| `night_relax.jpg` | Calming background image for night mode |

---

## 🧪 How to Run

1. Install dependencies:
```bash
pip install streamlit twilio pandas streamlit-autorefresh
```

2. Start the sensor simulator:
```bash
python pulsData.py
```

3. Launch the main dashboard (choose one):
```bash
streamlit run Day_Mode.py
```
```bash
streamlit run Night_Mode🌙.py
```

Optional:
```bash
streamlit run Statistics_Dashboard.py
streamlit run Notes_emotions.py
streamlit run Relaxing_breathing_session.py
```

---

## 🖼 Features

- Real-time physiological monitoring
- Triggered relaxing response (music, messages, breathing)
- Statistics dashboard and session logging
- Emotional journaling support
- Fully localized in Hebrew 🇮🇱

---

## 🔐 Privacy

All data is stored **locally**. No personal identifying information is collected.

---

## 🙌 Team

Created during a hackathon by a team passionate about digital mental wellness 💙
