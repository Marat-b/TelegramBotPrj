from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import ContentType, Message

from loader import dp, bot


@dp.message_handler(Command('photo'))
async def photo(message: types.Message):
	await message.answer('Введи фото')


@dp.message_handler(content_types = ContentType.PHOTO)
async def get_photo(message: Message):
	# await message.reply(message.photo[-1].file_id)
	file_id = message.photo[-1].file_id
	file_info = await bot.get_file(file_id)
	print('file_info.file_path={}'.format(file_info.file_path))
	# AgACAgIAAxkBAAIEYV-YWqKEl2sJp6HbXzidUAcXf85fAAKIrzEbaCvJSIgliXTciiDAAAFMEJguAAMBAAMCAAN5AAMfVwIAARsE
	downloaded_file = await message.photo[-1].download(destination = "image.jpg")

# with open("image.jpg", 'wb') as new_file:
# 	new_file.write(downloaded_file)
