import telegram
from telegram.ext import Updater
from telegram.ext import MessageHandler, filters
import asyncio

token = '6040831561:AAESQjZP7-_BeRscu25hzm0HVXK_JfQzpFg'
chat_id = '5377358530'

async def main():
    bot = telegram.Bot(token=token)
    await bot.get_me()

if __name__ == '__main__':
    asyncio.run(main())
#
# updater = Updater(bot=bot)
# dispatcher = updater.dispatcher
#
# async def handler(update, context):
#     user_text = update.message.text
#     if user_text == '안녕':
#         await bot.sendMessage(chat_id=chat_id, text='그래 안녕')
#     elif user_text == '뭐해':
#         await bot.sendMessage(chat_id=chat_id, text='그냥 있징')
#
# echo_handler = MessageHandler(filters.text, handler())
# dispatcher.add_handler(echo_handler)
#
# async def main():
#     await bot.sendMessage(chat_id=chat_id, text='Msg from python')
#     await updater.start_polling()
#
# if __name__ == '__main__':
#     try:
#         asyncio.run(main())
#     except:
#         print('except!')