from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

callback_payed = CallbackData('callback_payed', 'button_name')


def choice_payed(amount: str):
	payed = InlineKeyboardMarkup(row_width = 1,
	                             inline_keyboard = [
		                             [
			                             InlineKeyboardButton(text = '\U0001F4B8 Оплачено',
			                                                  callback_data = callback_payed.new(button_name =
			                                                                                     'button_payed'
			                                                                                     ))
		                             ],
		                             [
			                             InlineKeyboardButton(text = '\U0000274C Отмена',
			                                                  callback_data = 'cancel_pay')
		                             ]
	                             ])
	return payed
