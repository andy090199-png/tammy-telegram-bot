from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

import os

TOKEN = os.getenv("BOT_TOKEN")

CHANNEL_LINK = "https://t.me/tammy18368"
ADMIN_USERNAME = "https://t.me/tammy1836"
REGISTER_LINK = "https://rr88.pro/rf/69eb1864ba2df"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎁 CLAIM ID", callback_data="claim")],
        [InlineKeyboardButton("📢 JOIN CHANNEL", url=CHANNEL_LINK)],
        [InlineKeyboardButton("💬 CONTACT TAMMY", url=ADMIN_USERNAME)],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    text = """
🌙 Selamat Datang Ke Tammy Official Bot 🌙

🔥 Welcome Bonus 288%
💰 IN 100 DPT 388
🎁 Daily Checkin Bonus
⚡ Fast Withdraw

Klik button bawah untuk claim bonus sekarang 👇
"""

    await update.message.reply_text(text, reply_markup=reply_markup)


async def button_click_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    try:
        await query.answer()
    except:
        pass

    if query.data == "claim":

        keyboard = [
            [InlineKeyboardButton("🚀 REGISTER SEKARANG", url=REGISTER_LINK)],
            [InlineKeyboardButton("📢 JOIN CHANNEL", url=CHANNEL_LINK)],
            [InlineKeyboardButton("💬 CONTACT TAMMY", url=ADMIN_USERNAME)],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.message.reply_text(
            """
🎁 CLAIM BONUS NEW MEMBER

🔥 Welcome Bonus 288%
💰 IN 100 DPT 388
✅ Senang IN & OUT
✅ Fast Service

Tekan button bawah untuk register 👇
""",
            reply_markup=reply_markup
        )


async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.lower()

    if "bonus" in user_text:
        await update.message.reply_text("🎁 Welcome Bonus 288%\\n💰 IN 100 DPT 388\\n\\nTekan /start untuk claim sekarang 👇")

    elif "withdraw" in user_text or "wd" in user_text:
        await update.message.reply_text("💸 Fast Withdraw tersedia.\\nUntuk bantuan, tekan /start dan hubungi admin.")

    elif "register" in user_text or "daftar" in user_text:
        await update.message.reply_text("📝 Untuk register, tekan /start kemudian klik CLAIM ID.")

    elif "claim" in user_text or "id" in user_text:
        await update.message.reply_text("🎁 Nak claim ID? Tekan /start sekarang 👇")

    else:
        await update.message.reply_text("Hai boss 👋\\n\\nTaip: Bonus / Withdraw / Register / Claim\\nAtau tekan /start")


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_click_handler))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

print("Bot Running...")
app.run_polling()
