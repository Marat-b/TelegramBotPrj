import re

from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from data.config import BOT_TOKEN
from keyboards.inline.choice_photo_id import get_photo_id
from loader import dp, bot
from utils.db_api.product_commands import get_product_by_itemid


@dp.message_handler(text = 'Товар')
async def choice_product(message: types.Message):
	await message.answer('Выбран товар...')


# @dp.message_handler(regexp = '.+?\..+?')
@dp.message_handler(regexp = '^ID\=\d+')
async def get_photo(message: types.Message):
	print('get_photo -> photo_id={}, item_id={}'.format(message.text, re.sub('^ID\=', '', message.text)))
	item_id = re.sub('^ID\=', '', message.text)
	# await message.delete_reply_markup()
	await message.delete()
	# product = await get_product_by_itemid(int(item_id))
	# print('get_photo -> photo_id={}'.format(product.photo))
	# file_info = await bot.get_file(product.photo)
	# print(f"get_photo -> URL_photo=https://api.telegram.org/file/bot{BOT_TOKEN}/{file_info.file_path}")
	await message.answer('Нажмите кнопку...', reply_markup = get_photo_id(str(item_id)), disable_notification = True)
# await bot.send_photo(chat_id = message.chat.id,
#                      photo = product.photo,
#                      caption = "Product",
#                      reply_markup = get_photo_id(str(item_id)))
