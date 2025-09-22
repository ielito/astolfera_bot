# telegram_bot.py
import os
from telegram import Bot

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_message(text):
    """Sends a message to a Telegram chat.

    This function initializes a Telegram bot with the provided token and sends
    a message to the specified chat ID.

    Args:
        text (str): The message to be sent.
    """
    bot = Bot(token=TELEGRAM_TOKEN)
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=text)
    print("📨 Mensagem enviada ao Telegram!")