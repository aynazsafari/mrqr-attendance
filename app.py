"""
app.py — MrQR Smart Attendance System
A Streamlit app for QR-code-based classroom attendance tracking.

Run with:
    streamlit run app.py
"""

import streamlit as st
import qrcode
import csv
import os
from datetime import datetime

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="MrQR Attendance",
    page_icon="💗",
    layout="wide",
)

# ── Paths ─────────────────────────────────────────────────────────────────────
BASE_DIR    = os.path.dirname(os.path.abspath(__file__))
DATA_DIR    = os.path.join(BASE_DIR, "data")
QR_DIR      = os.path.join(BASE_DIR, "QR_Codes")
ASSETS_DIR  = os.path.join(BASE_DIR, "assets")
CSV_PATH    = os.path.join(DATA_DIR, "attendance.csv")

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(QR_DIR,   exist_ok=True)

# Initialise CSV with headers if it does not yet exist
if not os.path.exists(CSV_PATH):
    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow(["Student Name", "Student ID", "Class", "Time"])

# ── Styling ───────────────────────────────────────────────────────────────────
st.markdown("""
<style>
header { visibility: hidden; }

.main .block-container {
    padding-top: 0.8rem;
    padding-bottom: 1rem;
    border: 2px solid rgba(255,255,255,0.45);
    border-radius: 28px;
    margin: 8px 12px 12px 12px;
    background: rgba(255,255,255,0.04);
    backdrop-filter: blur(8px);
}

.stApp {
    background: linear-gradient(135deg, #ffe8f3, #f6edff, #fff3f8);
}

.block-container {
    padding-top: 1rem;
    max-width: 1500px;
}

.title {
    text-align: center;
    font-size: 64px;
    font-weight: 900;
    background: linear-gradient(90deg, #ff4fa3, #8b5cf6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    text-align: center;
    font-size: 22px;
    color: #555;
    margin-bottom: 35px;
}

.card-title   { font-size: 28px; font-weight: 800; margin-top: 12px; }
.pink         { color: #ff4fa3; }
.purple       { color: #8b5cf6; }
.small-text   { color: #666; font-size: 15px; margin-bottom: 18px; }

.stButton > button {
    width: 100%;
    border: none;
    border-radius: 18px;
    height: 52px;
    font-size: 17px;
    font-weight: 700;
    background: linear-gradient(90deg, #ff4fa3, #8b5cf6);
    color: white;
}

.stDownloadButton > button {
    width: 100%;
    border-radius: 18px;
    height: 48px;
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown('<div class="title">Scan and Create</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">QR Code Attendance System</div>', unsafe_allow_html=True)

# ── Three-column layout ───────────────────────────────────────────────────────
col1, col2, col3 = st.columns(3, gap="large")

# ─ Column 1 · Scan QR ─────────────────────────────────────────────────────────
with col1:
    scan_img = os.path.join(ASSETS_DIR, "scan.png")
    if os.path.exists(scan_img):
        st.image(scan_img, use_container_width=True)

    st.markdown('<div class="card-title pink">Scan QR Code</div>', unsafe_allow_html=True)
    st.markdown('<div class="small-text">Register student attendance for the class.</div>',
                unsafe_allow_html=True)

    student_name = st.text_input("Student Name")
    student_id   = st.text_input("Student ID")
    class_name_scan = st.text_input("Class Name (Scan)", value="Software Engineering 2",
                                    key="scan_class")
    uploaded_qr  = st.file_uploader("Upload QR Code Image", type=["png", "jpg", "jpeg"])

    if uploaded_qr:
        st.success("QR Code uploaded successfully ✅")

    if st.button("Register Attendance"):
        if not student_name or not student_id:
            st.warning("⚠️ Please enter student name and ID.")
        elif uploaded_qr is None:
            st.warning("⚠️ Upload the QR Code image first.")
        else:
            with open(CSV_PATH, "a", newline="", encoding="utf-8") as f:
                csv.writer(f).writerow([
                    student_name,
                    student_id,
                    class_name_scan,
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                ])
            st.success("✅ Attendance registered successfully 💗")

# ─ Column 2 · Create QR ───────────────────────────────────────────────────────
with col2:
    create_img = os.path.join(ASSETS_DIR, "create.png")
    if os.path.exists(create_img):
        st.image(create_img, use_container_width=True)

    st.markdown('<div class="card-title purple">Create Class QR</div>', unsafe_allow_html=True)
    st.markdown('<div class="small-text">Generate a unique QR code for today\'s session.</div>',
                unsafe_allow_html=True)

    class_name   = st.text_input("Class Name",   value="Software Engineering 2")
    session_name = st.text_input("Session Name", value="QR Attendance Session")

    qr_data = (
        f"Class: {class_name} | Session: {session_name} | "
        f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    )

    qr_output_path = os.path.join(QR_DIR, "class_qr.png")

    if st.button("Create QR Code"):
        img = qrcode.make(qr_data)
        img.save(qr_output_path)
        st.success("✨ QR Code created successfully!")

    if os.path.exists(qr_output_path):
        st.image(qr_output_path, width=230)
        with open(qr_output_path, "rb") as f:
            st.download_button(
                "⬇️ Download QR Code",
                f,
                file_name="class_qr.png",
                mime="image/png",
            )

# ─ Column 3 · Report ──────────────────────────────────────────────────────────
with col3:
    report_img = os.path.join(ASSETS_DIR, "report.png")
    if os.path.exists(report_img):
        st.image(report_img, use_container_width=True)

    st.markdown('<div class="card-title pink">Attendance Report</div>', unsafe_allow_html=True)
    st.markdown('<div class="small-text">Live attendance records and export.</div>',
                unsafe_allow_html=True)

    with open(CSV_PATH, "r", encoding="utf-8") as f:
        rows = list(csv.reader(f))

    total = max(len(rows) - 1, 0)
    st.metric("Total Registered", total, help="Total students who scanned in")
    st.table(rows)

    with open(CSV_PATH, "rb") as f:
        st.download_button(
            "⬇️ Download Report (CSV)",
            f,
            file_name="attendance_report.csv",
            mime="text/csv",
        )
