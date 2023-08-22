from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = 'your token'
BOT_USERNAME: Final = 'your bot name'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("hello! Thanks for chatting with the bot!")
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("hello ! what help do you need?")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
            await update.message.reply_text("this is a custom command!")

#response

def handle_response(text: str) -> str:
    if "hello" in text:
        return 'hey there'
    if 'how are you' in text:
        return "iam doing fine!"
    if 'what can you do' in text:
        return 'nothing'
    return 'I do not understand what you are saying'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type:str = update.message.chat.type
    text: str = update.message.text

    print(f'user ({update.message.chat.id}) in {message_type}: "{text}" ')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = tetx.replace(BOT_USERNAME, '').strip()
            response:str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)

async def error (update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'update {update} caused error {context.error}')



if __name__ == '__main__':
    print('Starting bot.....')
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', start_command))
    app.add_handler(CommandHandler('custom', start_command))


#messages
app.add_handler(MessageHandler(filters.TEXT, handle_message))

#error
app.add_error_handler(error)

print('starting')

app.run_polling(poll_interval= 3)
