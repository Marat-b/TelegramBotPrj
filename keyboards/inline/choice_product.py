from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

callback_product = CallbackData('callback_product', 'button_name')

choice_product = InlineKeyboardMarkup(row_width = 2,
                                      inline_keyboard = [
	                                      [
		                                      InlineKeyboardButton(text = 'Ввод данных',
		                                                           callback_data = 'button_product')
	                                      ],
	                                      [
		                                      InlineKeyboardButton(text = '\U0000274C Отмена',
		                                                           callback_data = 'cancel_product')
	                                      ]
                                      ])
