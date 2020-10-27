from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from utils.db_api.user_commands import select_user


class IsMember(BoundFilter):
	
	async def check(self, message: types.Message) -> bool:
		member_db = await select_user(message.from_user.id)
		return member_db

class IsNotMember(BoundFilter):
	
	async def check(self, message: types.Message) -> bool:
		member_db = await select_user(message.from_user.id)
		return not member_db
