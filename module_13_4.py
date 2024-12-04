from aiogram import Bot, Dispatcher
from aiogram.filters import Command, Text
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage

API_TOKEN = 'TOKEN'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message(Command('start'))
async def start(message: Message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью. Введите команду /calories, чтобы начать.')


@dp.message(Command('calories'))
async def set_age(message: Message, state: FSMContext):
    await message.answer('Введите свой возраст:')
    await state.set_state(UserState.age)


@dp.message(UserState.age)
async def set_growth(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await state.set_state(UserState.growth)


@dp.message(UserState.growth)
async def set_weight(message: Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await state.set_state(UserState.weight)


@dp.message(UserState.weight)
async def send_calories(message: Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()

    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])

    # Упрощённая формула Миффлина - Сан Жеора для женщин
    calories = 10 * weight + 6.25 * growth - 5 * age - 161

    await message.answer(f'Ваша норма калорий: {calories} ккал в день.')
    await state.clear()


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    import asyncio

    asyncio.run(main())
