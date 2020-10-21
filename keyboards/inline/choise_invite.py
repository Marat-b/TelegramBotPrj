from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

callback_invite = CallbackData('callback_invite', 'invite_code')


def get_invite_code(invite_code: str):
	choise_invite = InlineKeyboardMarkup(inline_keyboard = [
		[
			InlineKeyboardButton(text = 'Реферальная ссылка', switch_inline_query = invite_code)
		]
	])
	return choise_invite
