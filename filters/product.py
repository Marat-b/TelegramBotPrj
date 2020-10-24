from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class GetProducts(BoundFilter):
	
	async def check(self, message: types.Message) -> bool:
		member_db = True
		return member_db
