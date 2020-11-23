from aiogram.dispatcher.filters.state import StatesGroup, State


class PurchaseState(StatesGroup):
	AmountQuantity = State()
	DeliveryAddress = State()
	Pay = State()
