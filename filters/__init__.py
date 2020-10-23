from aiogram import Dispatcher


# from .is_admin import AdminFilter
from .member import IsMember, IsNotMember


def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsMember, IsNotMember)
    # dp.filters_factory.bind(AdminFilter)
    pass
