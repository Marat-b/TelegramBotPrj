from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_photo import callback_photo


def get_photo_id(photo_id: str):
	photo = InlineKeyboardMarkup(inline_keyboard = [
		[
			InlineKeyboardButton(text = 'Показать товар',
			                     callback_data = callback_photo.new(button_name = 'show_product',
			                                                        item_id = photo_id
			                                                        ))
		]
	])
	return photo
