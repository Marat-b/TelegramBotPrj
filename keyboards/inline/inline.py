import urllib
from typing import List
from urllib import request

import png
import requests
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultArticle, InlineQueryResultPhoto,\
	InlineQueryResultCachedPhoto
from aiogram.utils.markdown import hbold, bold, hcode

from data.config import BOT_TOKEN
from filters import IsNotMember, IsMember
from keyboards.inline.choice_photo_id import get_photo_id
from loader import dp, bot
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


@dp.inline_handler(IsMember())  # , regexp = '^.+?[^\:\/\/].+'
async def is_member(query: types.InlineQuery):
	"""Gain product's information from bot inline query """
	print('query.query = {}'.format(query.query.title()))
	gathered_products = await get_products(query.query.title().upper())
	print('gathered_products={}'.format(gathered_products))
	await query.answer(gathered_products, cache_time = 60, is_personal = True)  # , switch_pm_text = 'Private'


async def get_products(thing: str):
	"""Building product's list"""
	res = []
	if len(thing) == 0:
		print('get_products -> Quit')
		return res
	products = await pc.get_products(thing)
	print('get_products -> products={}'.format(products))
	for product in products:
		photo_url = await bot.get_file(product.photo)
		print('get_products -> photo_url.file_path={}'.format(photo_url.file_path))
		print(f"https://api.telegram.org/file/bot{BOT_TOKEN}/{photo_url.file_path}")
		print('get_products -> product={}'.format(product))
		res.append(types.InlineQueryResultArticle(id = str(product.id), title = product.name,
		                                          input_message_content = types.InputTextMessageContent(
				                                          message_text = f'ID={product.id}'),
		                                          description = f"{product.description}.\nЦена - "
		                                                        f"{str(product.price)}"
		                                          ))
	print('get_products -> res={}'.format(res))
	return res
