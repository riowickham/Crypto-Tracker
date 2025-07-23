import json, smtplib, os
from email.mime.text import MIMEText

def load_json(file, default):
    if not os.path.exists(file):
        save_json(file, default)
        return default
    try:
        with open(file, "r") as f:
            return json.load(f)
    except:
        return default

def save_json(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

def send_email(to, subject, body):
    EMAIL = os.getenv("EMAIL", "your_email@gmail.com")
    PASSWORD = os.getenv("APP_PASSWORD", "your_app_password")
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL
    msg["To"] = to

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL, PASSWORD)
        server.sendmail(EMAIL, to, msg.as_string())
