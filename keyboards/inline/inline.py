from typing import List

from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultArticle, InlineQueryResultPhoto,\
	InlineQueryResultCachedPhoto

from data.config import BOT_TOKEN
from filters import IsNotMember, IsMember
from keyboards.inline.choice_photo_id import get_photo_id
from loader import dp, bot
from utils.db_api import product_commands as pc


@dp.inline_handler(IsMember(), regexp = '^.+?\:\/\/.+')
async def get_referral(query: types.InlineQuery):
	print('get_referral -> query.query = {}'.format(query.query.title()))
	print('get_referral -> query.from_user.id={}, query.id = {}'.format(query.from_user.id, query.id))


# await query.answer(results =[],  switch_pm_text = query.query.title(), switch_pm_parameter = 'query')


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


# @dp.inline_handler(text = 'z')
# async def member(query: types.InlineQuery):
# 	print('query.query = {}'.format(query.query))
# 	await query.answer(
# 			results = [
# 				types.InlineQueryResultArticle(
# 						id = 'unknown',
# 						title = 'Выбор товаров',
# 						input_message_content = types.InputTextMessageContent(
# 								message_text = 'Товар'
# 						),
#
# 				)
# 			],
# 			cache_time = 5
# 	)

@dp.inline_handler(IsMember())  # , regexp = '^.+?[^\:\/\/].+'
async def member2(query: types.InlineQuery):
	print('query.query = {}'.format(query.query.title()))
	gathered_products = await get_products(query.query.title().upper())
	# res.append(gathered_products)
	# res = await get_products(gathered_products)
	print('gathered_products={}'.format(gathered_products))
	await query.answer(gathered_products, cache_time = 5, is_personal = True)  # , switch_pm_text = 'Private'


# await bot.answer_inline_query(inline_query_id = query.id, results = gathered_products, cache_time = 5)


async def get_products(thing: str):
	# res: List[types.InlineQueryResultPhoto] = []
	res = []
	# res: List[types.InlineQueryResultArticle] = []
	if len(thing) == 0:
		print('get_products -> Quit')
		return res
	products = await pc.get_products(thing)
	print('get_products -> products={}'.format(products))
	for product in products:
		photo_url = await bot.get_file(product.photo)
		print('get_products -> photo_url={}'.format(photo_url.file_path))
		print('get_products -> product={}'.format(product))
		res.append(types.InlineQueryResultArticle(id = str(product.id) + 'id', title = product.name,
		                                          input_message_content = types.InputTextMessageContent(
				                                          message_text = f'ID={product.id}'),  # 'product.photo',
		                                          # disable_web_page_preview = True),
		                                          # reply_markup = get_photo_id(product.id),
		                                          thumb_url =
		                                          # "https://st.depositphotos.com/1002351/2489/i/950/depositphotos_24894359-stock-photo-peeled-tangerine-or-mandarin-fruit.jpg",
		                                          f"https://api.telegram.org/file/bot{BOT_TOKEN}/{photo_url.file_path}",
		                                          description = f"{product.description}. Цена - {str(product.price)}",
		                                          hide_url = True
		                                          # thumb_width = 40,
		                                          # thumb_height = 20
		
		                                          ))
	# res.append(types.InlineQueryResultCachedPhoto(id = str(product.id), title = product.name,
	#                                   caption = f"<b>{product.name}</b>\n{product.description}.\nЦена -"
	#                                             f"<b>{str(product.price)}</b>",
	#                                   #description = f"{product.description}. Цена - {str(product.price)}",
	#                                   photo_file_id = product.photo,
	#                                   parse_mode = 'HTML'
	#                                   ))
	# f: types.InlineQueryResultCachedPhoto(id = str(product.id), title = product.name,
	#                                       caption = product.name,
	#                                       description = f"{product.description}. Цена - {str(product.price)}",
	#                                       # photo_url = product.photo,
	#                                       # thumb_url = product.photo,
	#                                       photo_file_id = product.photo
	#                                       # photo_width = 10,
	#                                       # photo_height = 10
	#                                       )
	# res.append(f)
	# res.append({ 'type':'photo', id:str(product.id), 'title':product.name,
	#              'photo_url':product.photo,
	#              'thumb_url':product.photo })
	print('get_products -> res={}'.format(res))
	return res
