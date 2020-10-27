from typing import List

from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultArticle

from filters import IsNotMember, IsMember
from loader import dp
from utils.db_api import product_commands as pc


@dp.inline_handler(IsNotMember())
async def not_member(query: types.InlineQuery):
	user = query.from_user.id
	print('inline user={}'.format(user))
	await query.answer(
			results = [],
			switch_pm_text = 'Бот не доступен',
			switch_pm_parameter = 'not_user',
			cache_time = 5
	)


@dp.inline_handler(text = 'z')
async def member(query: types.InlineQuery):
	print('query.query = {}'.format(query.query))
	await query.answer(
			results = [
				types.InlineQueryResultArticle(
						id = 'unknown',
						title = 'Выбор товаров',
						input_message_content = types.InputTextMessageContent(
								message_text = 'Товар'
						),
				
				)
			],
			cache_time = 5
	)


@dp.inline_handler(IsMember())
async def member2(query: types.InlineQuery):
	print('query.query = {}'.format(query.query.title()))
	# res: List[InlineQueryResultArticle] = []
	# res.append(types.InlineQueryResultArticle(id = '1', title = '2', description = '3',
	#                                           input_message_content = types.InputTextMessageContent(
	# 		                                          message_text = 'Товар2'
	#                                           )))
	# res.append(types.InlineQueryResultArticle(id = '41', title = '42', description = '43', input_message_content =
	# types.InputTextMessageContent(
	# 		message_text = 'Товар4'
	# )))
	gathered_products = await get_products(query.query.title())
	# res.append(gathered_products)
	# res = await get_products(gathered_products)
	await query.answer(gathered_products)


async def get_products(thing: str):
	res: List[InlineQueryResultArticle] = []
	if len(thing) == 0:
		return res
	products = await pc.get_products(thing)
	print('get_products -> products={}'.format(products))
	for product in products:
		print('get_products -> product={}'.format(product))
		res.append(types.InlineQueryResultArticle(id = product.id, title = product.name,
		                                          description = f"{product.description}. Цена - {str(product.price)}",
		                                          input_message_content = types.InputTextMessageContent(
			                                          message_text = str(product.id))))
	return res
