from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.utils.deep_linking import get_start_link
from aiogram.utils.markdown import bold, hcode

from filters import IsMember
from keyboards.inline.choise_invite import get_invite_code
from loader import dp, bot


@dp.message_handler(IsMember(), Command('referral'))
async def referral(message: types.Message):
	"""Making referral link"""
	start_link_encoded = await get_start_link(message.from_user.id, encode = True)
	# bot_username = (await bot.get_me()).username
	await message.answer(f'Скопируйте ссылку и отправьте её выбранному пользователю <b>{hcode(start_link_encoded)}</b>')
