from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def start_keyboard():
    keyboard = [
        [InlineKeyboardButton("🚪 Begin Application", callback_data="begin")]
    ]
    return InlineKeyboardMarkup(keyboard)


def question1_keyboard():
    keyboard = [
        [InlineKeyboardButton("🚀 Build a business", callback_data="business")],
        [InlineKeyboardButton("💪 Build discipline", callback_data="discipline")],
        [InlineKeyboardButton("🤝 Meet ambitious men", callback_data="network")],
        [InlineKeyboardButton("👀 Just curious", callback_data="curious")]
    ]
    return InlineKeyboardMarkup(keyboard)


def question2_keyboard():
    keyboard = [
        [InlineKeyboardButton("🚀 I'm already building something", callback_data="building")],
        [InlineKeyboardButton("💡 I have an idea", callback_data="idea")],
        [InlineKeyboardButton("📚 I'm learning", callback_data="learning")],
        [InlineKeyboardButton("😴 I'm just browsing", callback_data="browsing")]
    ]
    return InlineKeyboardMarkup(keyboard)


def question3_keyboard():
    keyboard = [
        [InlineKeyboardButton("✅ Yes", callback_data="yes")],
        [InlineKeyboardButton("❌ No", callback_data="no")]
    ]
    return InlineKeyboardMarkup(keyboard)