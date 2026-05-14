import tkinter as tk
from datetime import datetime
import sqlite3
import time
from cryptography.fernet import Fernet
import matplotlib.pyplot as plt

# =========================
# ENCRYPTION SETUP
# =========================
key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt(text):
    return cipher.encrypt(text.encode()).decode()

# =========================
# DATABASE SETUP
# =========================
conn = sqlite3.connect("keystrokes.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    key_pressed TEXT
)
""")
conn.commit()

# =========================
# VARIABLES
# =========================
keystrokes = 0
start_time = time.time()
time_series = []
count_series = []

# =========================
# GUI SETUP
# =========================
root = tk.Tk()
root.title("Secure Keystroke Analytics Dashboard")
root.geometry("650x550")

label = tk.Label(root, text="Type inside the box (Analytics System)", font=("Arial", 12))
label.pack(pady=10)

text_box = tk.Text(root, height=15, width=70)
text_box.pack()

status = tk.Label(root, text="", fg="green")
status.pack()

# =========================
# KEY PRESS FUNCTION
# =========================
def key_pressed(event):
    global keystrokes

    key = event.char if event.char else event.keysym
    timestamp = datetime.now().strftime("%H:%M:%S")

    encrypted_key = encrypt(key)

    keystrokes += 1

    # store graph data
    current_time = time.time() - start_time
    time_series.append(current_time)
    count_series.append(keystrokes)

    text_box.insert(tk.END, f"{timestamp} - {key}\n")

    cursor.execute(
        "INSERT INTO logs (timestamp, key_pressed) VALUES (?, ?)",
        (timestamp, encrypted_key)
    )
    conn.commit()

# =========================
# GRAPH DASHBOARD
# =========================
def show_graph():
    if len(time_series) == 0:
        status.config(text="No data to show graph")
        return

    plt.figure(figsize=(8,5))
    plt.plot(time_series, count_series, marker="o")

    plt.title("Keystroke Activity Over Time")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Total Keystrokes")
    plt.grid(True)

    plt.show()

# =========================
# REPORT FUNCTION
# =========================
def generate_report():
    duration = time.time() - start_time
    if duration < 1:
        duration = 1

    cpm = keystrokes / (duration / 60)

    if cpm > 300:
        status_text = "Suspicious Activity"
    elif cpm > 120:
        status_text = "Fast Typing"
    else:
        status_text = "Normal Activity"

    report = f"""
===== KEYSTROKE REPORT =====
Total Keystrokes: {keystrokes}
Time (sec): {int(duration)}
Typing Speed: {int(cpm)} CPM
Status: {status_text}
===========================
"""

    with open("report.txt", "w", encoding="utf-8") as f:
        f.write(report)

    status.config(text="Report Generated")

# =========================
# CLEAR FUNCTION
# =========================
def clear_data():
    global keystrokes, start_time, time_series, count_series

    keystrokes = 0
    start_time = time.time()
    time_series = []
    count_series = []

    text_box.delete("1.0", tk.END)
    status.config(text="Data Cleared")

# =========================
# BUTTONS
# =========================
tk.Button(root, text="Generate Report", command=generate_report).pack(pady=5)
tk.Button(root, text="Show Graph Dashboard", command=show_graph).pack(pady=5)
tk.Button(root, text="Clear Data", command=clear_data).pack(pady=5)

# =========================
# EVENT BINDING
# =========================
root.bind("<Key>", key_pressed)

root.mainloop()