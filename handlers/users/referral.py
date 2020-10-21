from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.inline.choise_invite import get_invite_code
from loader import dp, bot


@dp.message_handler(Command('referral'))
async def referral(message: types.Message):
	chat_id = message.from_user.id
	bot_username = (await bot.get_me()).username
	referral_link = f'https://t.me/{bot_username}?start={chat_id}'
	await message.answer('Сформируйте ссылку и отправьте её нужному пользователю', reply_markup = get_invite_code(
			referral_link))
