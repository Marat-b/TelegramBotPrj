import os
import re

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.utils.deep_linking import decode_payload
from aiogram.utils.markdown import hbold, hitalic

from filters import IsNotMember, IsMember
from keyboards.inline.choice_buy import choice_buy
from keyboards.inline.choise_invite import get_invite_code
from loader import dp, bot
from utils.db_api import user_commands as comm
from utils.db_api.product_commands import get_product_by_itemid
from utils.db_api.user_commands import select_user


@dp.message_handler(IsMember(), CommandStart(deep_link = re.compile('.+?')))
async def param_product(message: types.Message):
	"""Product's shopping"""
	item_id = message.get_args()
	print('param_product -> item_id={}'.format(item_id))
	product = await get_product_by_itemid(int(item_id))
	await message.answer_photo(photo = product.photo,
	                           caption = f'{hbold(product.name)}\n'
	                                     f'{hitalic(product.description)}\n\nЦена = '
	                                     f'{hbold(product.price)}',
	                           reply_markup = choice_buy(item_id))


@dp.message_handler(IsNotMember(), CommandStart())
async def bot_start(message: types.Message):
	"""Referral's operation"""
	referral = decode_payload(message.get_args())
	print('referral = {}'.format(referral))
	member_chat = await message.chat.get_member(message.from_user.id)
	print('IsMember member is admin={}, message.from_user.id={}'.format(member_chat.is_chat_admin(),
	                                                                    str(message.from_user.id)))
	
	if not referral or referral == 'not_user':
		text = ['Чтобы использовать этого бота введите код приглашения, либо пройдите по реферальной ссылке.',
		        'Введите команду /invite для ввода кода приглашения:']
		# \nРеферальная ссылка https://t.me/{bot_username}?start={chat_id}
		await message.answer('\n'.join(text))
	# await message.answer(text = 'Введите команду /invite для ввода кода приглашения:')
	else:
		user_id = message.from_user.id
		if int(referral) != user_id:
			await message.answer(f'Привет, {message.from_user.full_name}!')
			await message.answer('Занесён по реферальной ссылке')
			await message.answer('/help - помощь')
			await comm.add_user(user_id = user_id, username = message.from_user.username,
			                    name = message.from_user.full_name)
			# if int(referral) != int(os.getenv("ADMIN_ID")):
			await comm.update_bonus(int(referral))
