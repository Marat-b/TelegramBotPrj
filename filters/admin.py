from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from data.config import admins
from utils.db_api.user_commands import is_admin


class IsAdmin(BoundFilter):
    
    async def check(self, message: types.Message) -> bool:
        admin = await is_admin(message.from_user.id)
        # for admin in admins:
        #     if str(message.from_user.id) == str(admin):
        #         is_admin = True
        return admin
