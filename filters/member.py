from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from utils.db_api.user_commands import select_user


class IsMember(BoundFilter):
	
	async def check(self, message: types.Message) -> bool:
		# print('IsMember -> message.from_user.id={}'.format(message.from_user.id))
		member_db = await select_user(message.from_user.id)
		# print('IsMember -> member_db={}'.format(member_db))
		if member_db is not None:
			return True
		else:
			return False


class IsNotMember(BoundFilter):
	
	async def check(self, message: types.Message) -> bool:
		# print('IsNotMember -> message.from_user.id={}'.format(message.from_user.id))
		member_db = await select_user(message.from_user.id)
		# print('IsNotMember -> member_db={}'.format(member_db))
		if member_db is None:
			return True
		else:
			return False
