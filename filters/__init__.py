from aiogram import Dispatcher


# from .is_admin import AdminFilter
from .is_member import IsMember


def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsMember)
    # dp.filters_factory.bind(AdminFilter)
    pass
