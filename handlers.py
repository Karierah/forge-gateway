from telegram import Update
from telegram.ext import ContextTypes
from keyboards import question1_keyboard, question2_keyboard, question3_keyboard
from config import ADMIN_ID, INVITE_LINK


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query

    await query.answer()

    if query.data == "begin":

        await query.edit_message_text(
            "📋 Application - Question 1 of 3\n\n"
            "Why do you want to join The Forge?",
            reply_markup=question1_keyboard()
        )

    elif query.data in ["business", "discipline", "network"]:

        await query.edit_message_text(
            "📋 Application - Question 2 of 3\n\n"
            "Which best describes you today?",
            reply_markup=question2_keyboard()
        )

    elif query.data == "curious":

        await query.edit_message_text(
            "Thank you for your interest.\n\n"
            "The Forge is built for men who are ready to build, grow and contribute.\n\n"
            "We hope to see you again when you're ready."
        )

    elif query.data in ["building", "idea", "learning"]:

        await query.edit_message_text(
            "📋 Application - Question 3 of 3\n\n"
            "Are you willing to follow The Forge standards and contribute to the brotherhood?",
            reply_markup=question3_keyboard()
        )

    elif query.data == "browsing":

        await query.edit_message_text(
            "Thank you for your interest.\n\n"
            "The Forge is for men actively building and improving.\n\n"
            "You may reapply when you're ready."
        )

    elif query.data == "yes":

        user = update.effective_user

        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=(
                "🔥 NEW APPLICATION ACCEPTED\n\n"
                f"Name: {user.first_name}\n"
                f"Username: @{user.username if user.username else 'No username'}\n"
                f"User ID: {user.id}\n\n"
                f"Invite Link Sent: {INVITE_LINK}"
            )
        )

        await query.edit_message_text(
            "🔥 Application Accepted\n\n"
            "Welcome to The Forge.\n\n"
            f"Join here: {INVITE_LINK}"
        )

    elif query.data == "no":

        user = update.effective_user

        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=(
                "❌ APPLICATION REJECTED\n\n"
                f"Name: {user.first_name}\n"
                f"Username: @{user.username if user.username else 'No username'}\n"
                f"User ID: {user.id}"
            )
        )

        await query.edit_message_text(
            "Thank you for applying.\n\n"
            "At this time, The Forge is for those fully committed.\n\n"
            "You may reapply in the future."
        )
