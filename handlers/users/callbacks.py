from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.deep_linking import get_start_link
from aiogram.utils.markdown import hlink, hcode, bold, hbold

from data import config
from data.config import BOT_TOKEN
from keyboards.inline.callback_buy import callback_buy
from keyboards.inline.callback_photo import callback_photo
from keyboards.inline.choice_payed import choice_payed, callback_payed
from loader import dp, bot
from states.purchase_state import PurchaseState
from utils.db_api.product_commands import get_product_by_photoid, get_product_by_itemid
from utils.db_api.purchase_commands import add_purchase, update_payed
from utils.misc.qiwi import Payment, NotEnoughMoney, NoPaymentFound


@dp.callback_query_handler(callback_photo.filter(button_name = 'show_product'))
async def button_show_product(call: CallbackQuery, callback_data: dict):
	await call.answer(cache_time = 60)
	item_id = callback_data.get('item_id')
	# await call.message.delete()
	print('button_show_product -> item_id={}'.format(item_id))
	# me = await bot.get_me()
	# print('button_show_product -> me={}'.format(me))
	# chat_id = me.id
	# is_bot = call.from_user.is_bot
	# print('button_show_product ->  is_bot={}'.format(is_bot))
	# if is_bot:
	# 	print('Is bot')
	# else:
	# 	print('Is not bot')
	# product = await get_product_by_itemid(int(item_id))
	# print('button_show_product -> photo_id={}'.format(product.photo))
	# file_info = await bot.get_file(product.photo)
	# print('button_show_product -> file_info.file_path={}'.format(file_info.file_path))
	# print('button_show_product -> call.message.chat.id={}'.format(call.id))
	#
	# print('button_show_product -> call.message.chat.id={}'.format(call.message.chat.id))
	# await call.answer(text = 'Product', cache_time = 5)
	deep_link = await get_start_link(item_id)
	# await call.answer(text = f'Нажми ссылку для показа товара {deep_link}')
	# chat = await bot.get_chat(chat_id = chat_id)
	# print('button_show_product -> chat={}'.format(chat))
	# await bot.send_message(chat_id = chat_id, text = 'button_show_product -> send_message')
	
	await call.message.answer(text = f'Нажми ссылку для показа товара {deep_link}')


@dp.callback_query_handler(callback_buy.filter(button_name = 'button_buy'))
async def button_buy(call: CallbackQuery, callback_data: dict, state: FSMContext):
	await call.answer(cache_time = 60)
	item_id = callback_data.get('item_id')
	# await call.message.delete()
	print('button_buy -> item_id={}'.format(item_id))
	await state.update_data(product_id = item_id)
	await call.message.answer('Введите количество товара:')
	await PurchaseState.AmountQuantity.set()


@dp.message_handler(state = PurchaseState.AmountQuantity)
async def purchase_amountquantity(message: types.Message, state: FSMContext):
	answer = message.text
	await state.update_data(amount_quantity = answer)
	await message.answer('Введите адрес доставки:')
	await PurchaseState.DeliveryAddress.set()


@dp.message_handler(state = PurchaseState.DeliveryAddress)
async def purchase_shippingaddress(message: types.Message, state: FSMContext):
	delivery_address = message.text
	purchase = await state.get_data()
	amount_quantity = purchase.get('amount_quantity')
	product_id = purchase.get('product_id')
	product = await get_product_by_itemid(itemid = int(product_id))
	amount = round(product.price * int(amount_quantity), 2)
	print(f'Quintity={amount_quantity}, DeliveryAddress={delivery_address}, product_id = {product_id}, Amount='
	      f'{amount}')
	# await message.answer(
	# 		f'Наименование товара: {product.name}\nКоличество товара: {amount_quantity} шт.\nАдрес доставки:'
	# 		f' {delivery_address}\n\nСумма к '
	# 		f"оплате:\t{hbold(amount)}"
	#
	# )
	purchase_id = await add_purchase(product_id = product_id, amount = int(amount_quantity), address = delivery_address)
	await state.update_data(purchase_id = purchase_id)
	payment = Payment(amount = amount)
	payment.create()
	await state.update_data(payment = payment)
	await message.answer(
			f'Наименование товара: {hbold(product.name)}\nКоличество товара: {hbold(amount_quantity)} шт.\nАдрес '
			f'доставки:'
			f' {hbold(delivery_address)}\n\nСумма к '
			f"оплате:\t{hbold(amount)}\n\n"
			
			f"Оплатите не менее {amount:.2f} по номеру телефона или по адресу\n"
			f'{hlink(config.QIWI_WALLET, url = payment.invoice)}\n'
			"И обязательно укажите ID платежа:\n"
			f'{hcode(payment.id)}'
			'\n\nПосле оплаты нажмите кнопку "Оплачено"',
			reply_markup = choice_payed(str(amount)))
	await PurchaseState.Pay.set()


# await state.finish()


@dp.callback_query_handler(callback_payed.filter(button_name = 'button_payed'), state = PurchaseState.Pay)
async def button_payed(call: CallbackQuery, callback_data: dict, state: FSMContext):  # , state: FSMContext
	await call.answer(cache_time = 60)
	# purchase_id = callback_data.get('purchase_id')
	data = await state.get_data()
	payment: Payment = data.get("payment")
	purchase_id = data.get("purchase_id")
	print('button_payed -> payment_id={}, purchase_id={}'.format(payment.id, purchase_id))
	await update_payed(id = str(purchase_id), payed = True)
	try:
		payment.check_payment()
	except NoPaymentFound:
		await call.message.answer("Транзакция не найдена.")
		return
	except NotEnoughMoney:
		await call.message.answer("Оплаченная сума меньше необходимой.")
		return
	
	else:
		await call.message.answer("Успешно оплачено")
	await call.message.edit_reply_markup()
	await state.finish()


@dp.callback_query_handler(text = "cancel_pay", state = PurchaseState.Pay)
async def cancel_payment(call: types.CallbackQuery, state: FSMContext):
	await call.message.edit_text("Покупка отменена")
	print('cancel_payment ->')
	await state.finish()
