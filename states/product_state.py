from aiogram.dispatcher.filters.state import State, StatesGroup


class ProductState(StatesGroup):
	ProductName = State()
	ProductDescription = State()
	ProductPhoto = State()
	ProductPrice = State()
