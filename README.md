<div align="center">

<br/>

# 💗 MrQR — Smart QR Attendance

**Effortless class check-ins. Dreamy aesthetic. Zero paper.**

[![Python](https://img.shields.io/badge/Python-3.10+-ff69b4?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-c77dff?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io)
[![QR Code](https://img.shields.io/badge/QRCode-7.4+-ffb3d1?style=flat-square&logo=qrcode&logoColor=white)](https://pypi.org/project/qrcode/)
[![License: MIT](https://img.shields.io/badge/License-MIT-f4a7c3?style=flat-square)](LICENSE)

*A modern, QR-powered attendance system with a soft pink ✦ aesthetic.*

<br/>

</div>

---
![UI](assets/dashboard.png)

## 🌸 What Is MrQR?

**MrQR** replaces paper attendance sheets with a sleek Streamlit web application.
A professor generates a unique session QR code; students upload it to instantly mark
themselves present — all within a beautiful, pink-gradient interface.

> 💡 Designed for classrooms, workshops, or any event where you need quick headcounts.

---

## ✨ Features

| 💫 Feature | Description |
|---|---|
| **QR Generation** | Create a unique, session-specific QR code in one click |
| **Instant Registration** | Students upload the QR image → attendance logged instantly |
| **Live Dashboard** | Real-time attendance counter, always visible |
| **CSV Export** | One-click download of the full attendance report |
| **Aesthetic UI** | Soft pink + purple gradient design — Streamlit at its prettiest |
| **Persistent Storage** | All records saved to CSV, survives app restarts |

---

## 🛠️ Tech Stack

```
Language    →  Python 3.10+
Framework   →  Streamlit  (web UI & state management)
QR Engine   →  qrcode + Pillow  (generate & render QR codes)
Storage     →  CSV  (lightweight, portable attendance records)
Design      →  Custom CSS injected via st.markdown
```

---

## 📁 Project Structure

```
mrqr-attendance/
│
├── app.py                  ← Main Streamlit application
│
├── assets/                 ← UI illustration images
│   ├── scan.png
│   ├── create.png
│   └── report.png
│
├── data/
│   └── attendance.csv      ← Attendance records (auto-created on first run)
│
├── QR_Codes/               ← Generated QR images (gitignored except .gitkeep)
│   └── .gitkeep
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Quick Start

### 1 · Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/mrqr-attendance.git
cd mrqr-attendance
```

### 2 · Create & activate a virtual environment *(recommended)*

```bash
python -m venv venv

# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3 · Install dependencies

```bash
pip install -r requirements.txt
```

### 4 · Run the app

```bash
streamlit run app.py
```

> 🌐 Opens automatically at `http://localhost:8501`

---

## 🎓 Usage Guide

### 👩‍🏫 For the Instructor

1. Open the **"Create Class QR"** panel (centre column)
2. Enter the **Class Name** and **Session Name**
3. Click **Create QR Code** — a QR image appears instantly
4. Display the QR on your screen / projector for students to scan

### 👩‍🎓 For Students

1. Open the **"Scan QR Code"** panel (left column)
2. Enter your **Student Name** and **Student ID**
3. Upload a photo of the class QR code
4. Click **Register Attendance** — done! 💗

### 📊 For Reports

- The right column shows a **live attendance table**
- Click **Download Report (CSV)** to export at any time

---

## 📸 Screenshots

> *Coming soon — add screenshots of your running app here!*
>
> Tip: Press `F12 → Screenshots` in Streamlit or use `cmd/ctrl + shift + 5` on Mac/Windows.

---

## 🔮 Roadmap

- [ ] 📱 Camera-based live QR scanning (no upload needed)
- [ ] 🔐 Student login / authentication
- [ ] 📧 Email attendance reports automatically
- [ ] 📊 Per-student attendance percentage charts
- [ ] ☁️ Cloud database backend (Firebase / Supabase)

---

## 🤝 Contributing

Contributions are warmly welcomed 💗

```bash
# Fork → clone → create branch
git checkout -b feature/your-idea

# Make changes, then
git commit -m "✨ Add your feature"
git push origin feature/your-idea

# Open a Pull Request!
```

---

## 📄 License

Distributed under the **MIT License** — feel free to use, modify, and share.

---

<div align="center">

*Made with 💗 and a lot of pink gradients*

</div>
