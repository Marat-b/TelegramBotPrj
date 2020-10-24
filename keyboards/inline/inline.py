from typing import List

from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultArticle

from filters import IsNotMember, IsMember
from loader import dp


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
	# query.query
	
	print('query.query = {}'.format(query.query.title()))
	res: List[InlineQueryResultArticle] = []  # .append(id ='', title ='t')
	res.append(types.InlineQueryResultArticle(id = '1', title = '2', description = '3',
	                                          input_message_content = types.InputTextMessageContent(
			                                          message_text = 'Товар2'
	                                          )))
	res.append(types.InlineQueryResultArticle(id = '41', title = '42', description = '43', input_message_content =
	types.InputTextMessageContent(
			message_text = 'Товар4'
	)))
	# res.append([id = '1'])
	# rez = [res.append( )]
	# await query.answer(
	# 		results = [
	# 			types.InlineQueryResultArticle(
	# 					id = 'unknown',
	# 					title = 'Выбор товаров...',
	# 					description = 'Товар отличного качества',
	# 					input_message_content = types.InputTextMessageContent(
	# 							message_text = 'Товар'
	# 					),
	#
	# 			)
	# 		],
	# 		cache_time = 5
	# )
	await query.answer(res)
