
#Python 3.12   aiogram 3.15


from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message


API_TOKEN = 'TOKEN'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command('start'))
async def start(message: Message):
    print('Привет! Я бот помогающий твоему здоровью.')
    await message.answer('Привет! Я бот, помогающий твоему здоровью.')

@dp.message()
async def all_messages(message: Message):
    await message.answer('Введите команду /start, чтобы начать общение.')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
