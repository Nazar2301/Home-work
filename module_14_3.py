from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import FSInputFile

API_TOKEN = 'TOKEN'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Рассчитать')],
        [KeyboardButton(text='Информация')],
        [KeyboardButton(text='Купить')]
    ],
    resize_keyboard=True
)

inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')],
        [InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')]
    ]
)

product_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Product1', callback_data='product_buying')],
        [InlineKeyboardButton(text='Product2', callback_data='product_buying')],
        [InlineKeyboardButton(text='Product3', callback_data='product_buying')],
        [InlineKeyboardButton(text='Product4', callback_data='product_buying')]
    ]
)


@dp.message(Command('start'))
async def start(message: Message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью. Выберите действие:', reply_markup=keyboard)


@dp.message(lambda message: message.text == 'Рассчитать')
async def main_menu(message: Message):
    await message.answer('Выберите опцию:', reply_markup=inline_keyboard)


@dp.message(lambda message: message.text == 'Купить')
async def get_buying_list(message: Message):
    for i in range(1, 5):
        product_name = f'Product{i}'
        description = f'Описание {i}'
        price = f'{i * 100}'

        image_path = f'imeges\\{i}.jpg'
        image = FSInputFile(image_path)

        await message.answer_photo(photo=image,
                                   caption=f'Название: {product_name} | Описание: {description} | Цена: {price}')
    await message.answer('Выберите продукт для покупки:', reply_markup=product_keyboard)


@dp.callback_query(lambda call: call.data == 'formulas')
async def get_formulas(call: types.CallbackQuery):
    formula = (
        "Формула Миффлина-Сан Жеора для женщин:\n"
        "Калории = 10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (годы) - 161"
    )
    await call.message.answer(formula)


@dp.callback_query(lambda call: call.data == 'calories')
async def set_age(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer('Введите свой возраст:')
    await state.set_state(UserState.age)


@dp.callback_query(lambda call: call.data == 'product_buying')
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer('Вы успешно приобрели продукт!')


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

    calories = 10 * weight + 6.25 * growth - 5 * age - 161

    await message.answer(f'Ваша норма калорий: {calories} ккал в день.')
    await state.clear()


@dp.message()
async def all_messages(message: Message):
    await message.answer('Введите команду /start, чтобы начать общение.')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    import asyncio

    asyncio.run(main())
