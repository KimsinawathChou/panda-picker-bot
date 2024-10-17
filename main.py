import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Starts the conversation and provides a link to the external form."""
    chat_id = update.effective_chat.id
    form_url = f'https://foodpanda.vaneath.com/orders/create?chat-id={chat_id}'

    # Create an inline keyboard with a button that links to the form
    inline_keyboard = [
        [InlineKeyboardButton("Panda ToanChet Form", url=form_url)]
    ]
    inline_reply_markup = InlineKeyboardMarkup(inline_keyboard)

    # Create a reply keyboard with a button for customer support
    reply_keyboard = [
        [KeyboardButton("Customer Support")]
    ]
    reply_markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)

    await update.message.reply_text(
        text=f'<b>សួស្ដីបង! {update.effective_user.name}</b>\n'
             'នេះគឺជា Bot សម្រាប់យកម្ហូបអាហាររបស់បងមកកាន់ជាន់ការិយាល័យការងាររបស់បង\n\n'
             'ដើម្បីចាប់ផ្តើមសម្រាប់យកម្ហូបអាហាររបស់បងមកកាន់ជាន់ការិយាល័យការងាររបស់បង សូមបងជួយបំពេញទិន្នន័យខាងក្រោមនេះ:',
        parse_mode='HTML',
        reply_markup=inline_reply_markup,
    )

    # Send the reply keyboard separately
    await update.message.reply_text(
        text='For customer support, please click the button below.',
        reply_markup=reply_markup,
    )

    return update.effective_chat.id

async def log_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Logs the incoming messages from users."""
    user = update.effective_user
    chat_id = update.effective_chat.id
    message = update.message.text

    logger.info(f"Received message from user {user.name} (ID: {chat_id}): {message}")

    # Handle the customer support button click
    if message == "Customer Support":
        await update.message.reply_text(
            text='Please contact our customer support at @SunLeang123.',
            parse_mode='HTML'
        )

def main() -> None:
    """Run the bot."""
    application = Application.builder().token("7901123954:AAErTOKfnjGPSgb1tcR1VJYB-68O1GzVdgk").build()

    # Handle the case when a user sends /start
    application.add_handler(CommandHandler('start', start))

    # Log all incoming messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, log_message))

    application.run_polling()

if __name__ == '__main__':
    main()

#7338894408:AAFsZB-pSibo4UMytDSxBkcLfoAqQbQcxAQ
