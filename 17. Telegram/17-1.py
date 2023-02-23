import telegram
import asyncio

token = '6040831561:AAESQjZP7-_BeRscu25hzm0HVXK_JfQzpFg'
chat_id = '5377358530'

bot = telegram.Bot(token=token)

async def main():
    await bot.sendMessage(chat_id=chat_id, text='Msg from python')

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except:
        print('except!')

# updates = bot.getUpdates()
# for u in updates:
#     print(u.message)