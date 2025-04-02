from dotenv import load_dotenv
import os

load_dotenv()
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import requests


TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Oi! Eu sou a Sarah no Telegram 😄 Manda uma pergunta aí!")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    response = requests.post(
        "http://127.0.0.1:8080/respond",
        json={"question": user_message})

    sarah_reply = response.json().get("reply", "Desculpa, não entendi 😢")
    await update.message.reply_text(sarah_reply)


if __name__ == '__main__':
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Sarah no Telegram está rodando...")
    app.run_polling()
