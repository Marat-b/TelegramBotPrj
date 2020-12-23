from io import BytesIO

import aiohttp
from aiogram import types

from data.config import BOT_TOKEN
from loader import bot


async def photo_link(file_id: int) -> str:
	downloaded = await bot.download_file_by_id(file_id)
	with downloaded as file:
		form = aiohttp.FormData()
		# print(f'photo_link2 -> form={form}')
		form.add_field(
				name = 'file',
				value = file,
		)
		# print(f'photo_link2 -> form={form}')
		async with bot.session.post('https://telegra.ph/upload', data = form) as response:
			img_src = await response.json()
	# print(f'photo_link2 -> img_src={img_src}')
	link = 'http://telegra.ph' + img_src[0]["src"]
	return link
