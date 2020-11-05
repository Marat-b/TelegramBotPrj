from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import ContentType, Message

from loader import dp, bot
from utils.db_api.product_commands import add_product


@dp.message_handler(Command('photo'))
async def photo(message: types.Message):
	await message.answer('Введи фото')


@dp.message_handler(content_types = ContentType.PHOTO)
async def get_photo(message: Message):
	# await message.reply(message.photo[-1].file_id)
	for photo in message.photo:
		print('get_photo -> photo.file_id={}, photo.file_size={}'.format(photo.file_id, photo.file_size))
	file_id = message.photo[-1].file_id
	file_info = await bot.get_file(file_id)
	print('file_info.file_path={}'.format(file_info.file_path))
	# AgACAgIAAxkBAAIEYV-YWqKEl2sJp6HbXzidUAcXf85fAAKIrzEbaCvJSIgliXTciiDAAAFMEJguAAMBAAMCAAN5AAMfVwIAARsE
	# AgACAgIAAxkBAAIEgl - cJPKM6H686VsxViYTuhO - WFouAAKOsDEbNnngSKGA8l32kdtNg00SlS4AAwEAAwIAA3kAA0PoBQABGwQ
	# downloaded_file = await message.photo[-1].download(destination = "image.jpg")
	await add_product(name = 'name', description = 'description', photo = file_id, price = 11.11)

# with open("image.jpg", 'wb') as new_file:
# 	new_file.write(downloaded_file)

@dp.message_handler(content_types = ContentType.DOCUMENT)
async def get_document(message: Message):
	print('get_document -> doc.file_id={}, doc.file_size={}, thumb.file_id={}, thumb.file_size={}'.format(
			message.document.file_id,
			message.document.file_size,
			message.document.thumb.file_id,
			message.document.thumb.file_size))
