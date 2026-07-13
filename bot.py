from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# --- جزء يخلي Render يشوف البوت "حي" ---
app_web = Flask('')

@app_web.route('/')
def home():
    return "Bot is alive"

def run():
    app_web.run(host='0.0.0.0', port=8080)

def keep_alive():
    Thread(target=run).start()

# --- جزء البوت ---
TABLE = {
    '0': 'f', '1': 'e', '2': 'd', '3': 'c',
    '4': 'b', '5': 'a', '6': '9', '7': '8',
    '8': '7', '9': '6', 'a': '5', 'b': '4',
    'c': '3', 'd': '2', 'e': '1', 'f': '0'
}

def fh_to_wlan(fh_code):
    hexpart = fh_code.split('_')[-1].split('-')[-1]
    return 'wlan' + ''.join(TABLE[c] for c in hexpart.lower())

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ابعثلي اسم الـ FH (مثال: fh_b181e8) ونعطيك الكود.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    try:
        result = fh_to_wlan(text)
        await update.message.reply_text(f"الكود: {result}")
    except KeyError:
        await update.message.reply_text("الصيغة غلط، تأكد من الاسم (مثال: fh_b181e8)")

keep_alive()

app = ApplicationBuilder().token("853
