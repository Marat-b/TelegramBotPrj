from aiogram.types import CallbackQuery, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.deep_linking import get_start_link

from data.config import BOT_TOKEN
from keyboards.inline.callback_photo import callback_photo
from loader import dp, bot
from utils.db_api.product_commands import get_product_by_photoid, get_product_by_itemid


@dp.callback_query_handler(callback_photo.filter(button_name = 'show_product'))
async def button_show_product(call: CallbackQuery, callback_data: dict):
	await call.answer(cache_time = 60)
	item_id = callback_data.get('item_id')
	print('button_show_product -> item_id={}'.format(item_id))
	# product = await get_product_by_itemid(int(item_id))
	# print('button_show_product -> photo_id={}'.format(product.photo))
	# file_info = await bot.get_file(product.photo)
	# print('button_show_product -> file_info.file_path={}'.format(file_info.file_path))
	# print('button_show_product -> call.message.chat.id={}'.format(call.id))
	#
	# print('button_show_product -> call.message.chat.id={}'.format(call.message.chat.id))
	# await call.answer(text = 'Product', cache_time = 5)
	deep_link = await get_start_link(item_id)
	await call.message.answer(text = f'Нажми ссылку для показа товара {deep_link}')
