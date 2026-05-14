🔐 Secure Keystroke Analytics Project

This is a Python-based cybersecurity project that records keyboard input inside an application, stores data securely using encryption and SQLite, and shows analytics with a graph dashboard.

📁 Project Structure
secure-keylogger-project/
│
├── secure_logger.py     # Main Python application
├── keystrokes.db        # Database file (auto-created)
├── report.txt           # Generated report file
└── README.md            # Project documentation
⚙️ Requirements
Python 3.x
pip package manager
📦 Install required libraries
pip install cryptography matplotlib
▶️ How to Run the Project
Step 1: Open Command Prompt

Go to your project folder:

cd C:\password_Streagth\keylogger
Step 2: Run the program
python secure_logger.py
🖥 How to Use
Run the program
A GUI window will open
Type inside the text box
Click buttons:
📄 Generate Report → Creates report.txt
📊 Show Graph Dashboard → Shows graph of keystrokes
🧹 Clear Data → Resets all data
📊 Output Files
📄 report.txt

Contains:

Total keystrokes
Typing speed (CPM)
Activity status
🗄 keystrokes.db

Stores encrypted keystroke data

🧠 Features
GUI-based application (Tkinter)
Encryption using Fernet
SQLite database storage
Graph visualization using Matplotlib
Typing speed analysis
Simple anomaly detection
⚠️ Disclaimer

This project is only for educational purposes and cybersecurity learning.
It does NOT capture system-wide keystrokes.

👨‍💻 Project Purpose

To understand:

Keyboard event handling
Data encryption
Database storage
Cybersecurity monitoring basics
Data visualization
