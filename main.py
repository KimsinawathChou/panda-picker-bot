import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Starts the conversation and provides a link to the external form."""
    chat_id = update.effective_chat.id
    form_url = f'https://foodpanda.vaneath.com/orders/create?chat-id={chat_id}'

    # Create an inline keyboard with a button that links to the form
    keyboard = [
        [InlineKeyboardButton("Panda Picker Form", url=form_url)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        text=f'<b>សួស្ដីបង! {update.effective_user.name}</b>\n'
             'នេះគឺជា Bot សម្រាប់យកម្ហូបអាហាររបស់បងមកកាន់ជាន់ការិយាល័យការងាររបស់បង\n\nដើម្បីចាប់ផ្តើមសម្រាប់យកម្ហូបអាហាររបស់បងមកកាន់ជាន់ការិយាល័យការងាររបស់បង សូមបងជួយបំពេញទិន្នន័យខាងក្រោមនេះ',
        parse_mode='HTML',
        reply_markup=reply_markup,
    )

    return update.effective_chat.id

def main() -> None:
    """Run the bot."""
    application = Application.builder().token("7377788205:AAG_U_Qm_Orf42C2RQpu4_OWGqnTUQLCX40").build()

    # Handle the case when a user sends /start but they're not in a conversation
    application.add_handler(CommandHandler('start', start))

    application.run_polling()

if __name__ == '__main__':
    main()
