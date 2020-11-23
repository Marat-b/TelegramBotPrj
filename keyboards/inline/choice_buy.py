from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_buy import callback_buy


def choice_buy(item_id: int):
	buy = InlineKeyboardMarkup(row_width = 1,
	                           inline_keyboard = [
		                           [
			                           InlineKeyboardButton(text = '\U0001F4B3 Купить',
			                                                callback_data = callback_buy.new(button_name = 'button_buy',
			                                                                                 item_id = item_id))
		                           ],
		                           [
			                           InlineKeyboardButton(text = '<<Назад',
			                                                switch_inline_query_current_chat = '')
		                           ]
	                           ])
	return buy
