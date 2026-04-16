import smtplib
from email.mime.text import MIMEText
import requests
import os 


def send_telegram_message(message):
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    CHAT_ID = os.getenv("CHAT_ID")
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)

def send_email_message(message ):
    sender = os.getenv("EMAIL_SENDER")
    app_password = os.getenv("EMAIL_PASSWORD")
    receiver = os.getenv("EMAIL_RECEIVER")
    msg = MIMEText(message)
    msg["From"] = sender
    msg["To"] = receiver
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, app_password)
        server.send_message(msg)


