"""
在线问诊预约网站 —— 本地框架 (Flask)
运行: 在 web_project 目录下执行  python app.py
访问: http://localhost:5000
"""
import sqlite3
import os
from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "clinic.db")


def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        """CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            department TEXT NOT NULL,
            doctor TEXT,
            appt_date TEXT NOT NULL,
            timeslot TEXT NOT NULL,
            symptoms TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )"""
    )
    conn.commit()
    conn.close()


init_db()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/appointments")
def appointments():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        "SELECT id, name, phone, department, doctor, appt_date, timeslot, symptoms, created_at "
        "FROM appointments ORDER BY id DESC"
    )
    rows = c.fetchall()
    conn.close()
    return render_template("appointments.html", appointments=rows)


@app.route("/api/appointments", methods=["POST"])
def add_appointment():
    data = request.form
    name = (data.get("name") or "").strip()
    phone = (data.get("phone") or "").strip()
    department = (data.get("department") or "").strip()
    doctor = (data.get("doctor") or "").strip()
    appt_date = (data.get("appt_date") or "").strip()
    timeslot = (data.get("timeslot") or "").strip()
    symptoms = (data.get("symptoms") or "").strip()

    if not (name and phone and department and appt_date and timeslot):
        return jsonify({"error": "请填写姓名、手机号、科室、就诊日期和时间段等必填项"}), 400

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        "INSERT INTO appointments (name, phone, department, doctor, appt_date, timeslot, symptoms) "
        "VALUES (?,?,?,?,?,?,?)",
        (name, phone, department, doctor, appt_date, timeslot, symptoms),
    )
    conn.commit()
    conn.close()
    return jsonify({"success": True, "message": "预约成功"})


if __name__ == "__main__":
    # 本地默认 5000; 云平台通过环境变量 PORT 注入端口; debug 默认关闭(线上安全)
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG", "0") == "1"
    app.run(host="0.0.0.0", port=port, debug=debug)
