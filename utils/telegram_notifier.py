# Sends messages to Telegram bot

import os
import requests
from dotenv import load_dotenv

load_dotenv()

def send_telegram_message(text):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        return
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": text}
    try:
        requests.post(url, data=data)
    except Exception as e:
        print("Failed to send Telegram message:", e)
