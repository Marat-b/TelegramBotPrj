from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import ContentType, Message

from filters import IsAdmin
from loader import dp, bot
from utils.db_api.product_commands import add_product


@dp.message_handler(IsAdmin(), Command('photo'))
async def photo(message: types.Message):
	await message.answer('Загрузи фото')


@dp.message_handler(content_types = ContentType.PHOTO)
async def get_photo(message: Message):
	file_id = message.photo[-1].file_id
	# file_info = await bot.get_file(file_id)
	# print('file_info.file_path={}'.format(file_info.file_path))
	# await add_product(name = 'name', description = 'description', photo = file_id, price = 11.11)
	await message.answer(f'ID файла:\n{file_id}')


@dp.message_handler(content_types = ContentType.DOCUMENT)
async def get_document(message: Message):
	if message.document.mime_type.__contains__('image'):
		file_id = message.document.file_id
		# file_info = await bot.get_file(file_id)
		await message.answer(f'ID файла:\n{file_id}')
