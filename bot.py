from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

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

app = ApplicationBuilder().token("8535910981:AAGTRrfNW72Ozl9e4uGjeXBLrE59cYP2ndQ").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
