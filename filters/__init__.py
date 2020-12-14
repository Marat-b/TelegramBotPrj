from aiogram import Dispatcher


# from .is_admin import AdminFilter
from .member import IsMember, IsNotMember
from .admin import IsAdmin


def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsMember, IsNotMember)
    dp.filters_factory.bind(IsAdmin)
    pass
