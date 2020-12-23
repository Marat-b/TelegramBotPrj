import re

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart, Command
from aiogram.types import ContentType, CallbackQuery
from aiogram.utils.markdown import hbold, hitalic

from data.config import BOT_TOKEN
from filters import IsAdmin
from keyboards.inline.choice_buy import choice_buy
from keyboards.inline.choice_product import choice_product, callback_product
from loader import dp, bot
from states.product_state import ProductState
from utils.db_api.product_commands import get_product_by_itemid, add_product


@dp.message_handler(regexp = '^ID\=\d+')
async def get_photo(message: types.Message):
	# print('get_photo -> photo_id={}, item_id={}'.format(message.text, re.sub('^ID\=', '', message.text)))
	item_id = re.sub('^ID\=', '', message.text)
	# await message.delete_reply_markup()
	await message.delete()
	# await message.answer('~~~~~~~~~~', reply_markup = get_photo_id(str(item_id)), disable_notification = True)
	
	product = await get_product_by_itemid(int(item_id))
	await message.answer_photo(photo = product.photo,
	                           caption = f'{hbold(product.name)}\n'
	                                     f'{hitalic(product.description)}\n\nЦена = '
	                                     f'{hbold(product.price)}',
	                           reply_markup = choice_buy(item_id))


@dp.message_handler(IsAdmin(), Command('product'))
async def product(message: types.Message):
	print('product ->')
	await message.answer('Ввод реквизитов товара:\n'
	                     '1. Наименование.\n'
	                     '2. Описание.\n'
	                     '3. Фото.\n'
	                     '4. Цена.\n\n'
	                     '1. Введите <u>наименование</u> товара:')
	
	await ProductState.ProductName.set()


@dp.message_handler(state = ProductState.ProductName)
async def product_name(message: types.Message, state: FSMContext):
	answer = message.text
	await state.update_data(product_name = answer)
	await message.answer('2. Введите <u>описание</u> товара:')
	await ProductState.ProductDescription.set()


@dp.message_handler(state = ProductState.ProductDescription)
async def product_description(message: types.Message, state: FSMContext):
	answer = message.text
	await state.update_data(product_description = answer)
	await message.answer('3. Загрузите <u>фото</u> товара:')
	await ProductState.ProductPhoto.set()


@dp.message_handler(content_types = ContentType.PHOTO, state = ProductState.ProductPhoto)
async def product_photo(message: types.Message, state: FSMContext):
	file_id = message.photo[-1].file_id
	await state.update_data(product_photo = file_id)
	print(f'product_photo -> file_id={file_id}')
	await message.answer('4. Введите <u>цену</u> товара:')
	await ProductState.ProductPrice.set()


@dp.message_handler(state = ProductState.ProductPrice)
async def product_photo(message: types.Message, state: FSMContext):
	try:
		text = message.text
		product_price = float(text)
		data = await state.get_data()
		product_name = data.get('product_name')
		product_description = data.get('product_description')
		product_photo = data.get('product_photo')
		await add_product(name = product_name, description = product_description, photo = product_photo,
						  price = product_price)
		await state.finish()
		print('product_photo -> state.finish')
		await message.answer('Ввод данных закончен', reply_markup = choice_product)
	except Exception:
		await message.answer('Цена товара должно быть числом, повторите ввод:')
		await ProductState.ProductPrice.set()


@dp.callback_query_handler(text = 'button_product')
async def button_product(call: CallbackQuery):
	await call.answer(cache_time = 60)
	await call.message.edit_text('/product')


@dp.callback_query_handler(text = 'cancel_product')
async def cancel_product(call: CallbackQuery):
	await call.answer(cache_time = 60)
	await call.message.edit_text('Ввод данных отменён')
