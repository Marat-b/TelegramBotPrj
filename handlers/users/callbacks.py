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


@dp.callback_query_handler(callback_photo.filter(button_name='show_product'))
async def button_show_product(call: CallbackQuery, callback_data: dict):
    # await call.answer(cache_time = 60)
    item_id = callback_data.get('item_id')
    # await call.message.delete()
    print('button_show_product -> item_id={}'.format(item_id))
    deep_link = await get_start_link(item_id)
    await call.message.answer(text=f'Нажми ссылку для показа товара {deep_link}')


@dp.callback_query_handler(callback_buy.filter(button_name='button_buy'))
async def button_buy(call: CallbackQuery, callback_data: dict, state: FSMContext):
    """ Button 'button_buy' is pressed, we will start to choose a quantity of things"""
    await call.answer(cache_time=60)
    item_id = callback_data.get('item_id')
    # await call.message.delete()
    print('button_buy -> item_id={}'.format(item_id))
    await state.update_data(product_id=item_id)
    await call.message.answer('Введите количество товара:')
    await PurchaseState.AmountQuantity.set()


@dp.message_handler(state=PurchaseState.AmountQuantity)
async def purchase_amountquantity(message: types.Message, state: FSMContext):
    """There was chosen a quantity of things. Input a delivery address"""
    answer = message.text
    if answer.isdigit():
        await state.update_data(amount_quantity=answer)
        await message.answer('Введите адрес доставки:')
        await PurchaseState.DeliveryAddress.set()
    else:
        await message.answer('Количество товара должно быть цифрой, повторите ввод:')
        await PurchaseState.AmountQuantity.set()


@dp.message_handler(state=PurchaseState.DeliveryAddress)
async def purchase_shippingaddress(message: types.Message, state: FSMContext):
    """Purchase shipping"""
    user_id = message.from_user.id
    delivery_address = message.text
    purchase = await state.get_data()
    quantity = purchase.get('amount_quantity')
    product_id = purchase.get('product_id')
    product = await get_product_by_itemid(itemid=int(product_id))
    cost = round(product.price * int(quantity), 2)
    print(f'Quintity={quantity}, DeliveryAddress={delivery_address}, product_id = {product_id}, Amount='
          f'{product.price}')
    purchase_id = await add_purchase(user_id=user_id, product_id=product_id, amount=product.price,
                                     quantity=quantity, address=delivery_address)
    await state.update_data(purchase_id=purchase_id)
    payment = Payment(amount=cost)
    payment.create()
    await state.update_data(payment=payment)
    await message.answer(
        f'Наименование товара: {hbold(product.name)}\nКоличество товара: {hbold(quantity)} шт.\nАдрес '
        f'доставки:'
        f' {hbold(delivery_address)}\n\nСумма к '
        f"оплате:\t{hbold(cost)}\n\n"

        f"Оплатите не менее {cost:.2f} по номеру телефона или по адресу\n"
        f'{hlink(config.QIWI_WALLET, url=payment.invoice)}\n'
        "И обязательно укажите ID платежа:\n"
        f'{hcode(payment.id)}'
        '\n\nПосле оплаты нажмите кнопку "Оплачено"',
        reply_markup=choice_payed(str(cost)))
    await PurchaseState.Pay.set()


# await state.finish()


@dp.callback_query_handler(callback_payed.filter(button_name='button_payed'), state=PurchaseState.Pay)
async def button_payed(call: CallbackQuery, callback_data: dict, state: FSMContext):
    """Purchase checking and buying"""
    await call.answer(cache_time=60)
    # purchase_id = callback_data.get('purchase_id')
    data = await state.get_data()
    payment: Payment = data.get("payment")
    purchase_id = data.get("purchase_id")
    print('button_payed -> payment_id={}, purchase_id={}'.format(payment.id, purchase_id))

    try:
        payment.check_payment()
    except NoPaymentFound:
        await call.message.answer("Транзакция не найдена.")
        return
    except NotEnoughMoney:
        await call.message.answer("Оплаченная сума меньше необходимой.")
        return

    else:
        await update_payed(id=str(purchase_id), payed=True)
        await call.message.answer("Успешно оплачено")

    await call.message.edit_reply_markup()
    await state.finish()


@dp.callback_query_handler(text="cancel_pay", state=PurchaseState.Pay)
async def cancel_payment(call: types.CallbackQuery, state: FSMContext):
    """Purchase cancellation"""
    await call.message.edit_text("Покупка отменена")
    print('cancel_payment ->')
    await state.finish()
