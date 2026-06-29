from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)
from config import BOT_TOKEN
from keyboards import start_keyboard, question1_keyboard
from handlers import button

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🔥 *Welcome to The Forge*\n\n"
        "The Forge is a brotherhood of men who build, lead, and hold one another accountable.\n\n"
        "Membership is earned.\n\n"
        "If you're ready, begin your application below.",
        parse_mode="Markdown",
        reply_markup=start_keyboard()
    )





app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

print("The Forge Gateway is running...")