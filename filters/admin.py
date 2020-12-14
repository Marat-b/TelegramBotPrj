from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from data.config import admins


class IsAdmin(BoundFilter):
    
    async def check(self, message: types.Message) -> bool:
        is_admin = False
        for admin in admins:
            if str(message.from_user.id) == str(admin):
                is_admin = True
        return is_admin
