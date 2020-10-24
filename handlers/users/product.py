from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from loader import dp


@dp.message_handler(text = 'Товар')
async def choice_product(message: types.Message):
	await message.answer('Выбран товар...')
