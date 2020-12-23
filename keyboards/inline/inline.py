from aiogram import types

from data.config import BOT_TOKEN
from filters import IsNotMember, IsMember
from loader import dp, bot
from utils import photo_link
from utils.db_api import product_commands as pc


@dp.inline_handler(IsNotMember())
async def not_member(query: types.InlineQuery):
	user = query.from_user.id
	print('inline user={}'.format(user))
	await query.answer(
			results = [],
			switch_pm_text = 'Бот не доступен, перейти в бот',
			switch_pm_parameter = 'not_user',
			cache_time = 5
	)


@dp.inline_handler(IsMember())  # , regexp = '^.+?[^\:\/\/].+'
async def is_member(query: types.InlineQuery):
	"""Gain product's information from bot inline query """
	# print('query.query = {}'.format(query.query.title()))
	gathered_products = await get_products(query.query.title().upper())
	# print('gathered_products={}'.format(gathered_products))
	await query.answer(gathered_products, cache_time = 60)


async def get_products(thing: str):
	"""Building product's list"""
	res = []
	if len(thing) == 0:
		print('get_products -> Quit')
		res.append(types.InlineQueryResultArticle(id = '0', title = 'Введите название товара, после имени бота...',
		                                          input_message_content = types.InputTextMessageContent(
				                                          message_text = 'Введите название товара:\n@название_бота '
				                                                         'телевизор')))
		return res
	products = await pc.get_products(thing)
	# print('get_products -> products={}'.format(products))
	for product in products:
		link = await photo_link(product.photo)
		res.append(types.InlineQueryResultArticle(id = str(product.id), title = product.name,
		                                          input_message_content = types.InputTextMessageContent(
				                                          message_text = f'ID={product.id}'),
		                                          description = f"{product.description[:30]}.\nЦена - "
		                                                        f"{str(product.price)}",
		                                          thumb_url = link
		                                          )
		           )
	# print('get_products -> res={}'.format(res))
	return res
