import os

import django


# from utils.db_api import db_gino, product_commands, purchase_commands
# from loader import db, bot
# from utils.db_api import user_commands as comm


async def on_startup(dp):
	import filters
	import middlewares
	filters.setup(dp)
	middlewares.setup(dp)
	
	from utils.notify_admins import on_startup_notify
	# print("Подключаем БД")
	# await db_gino.on_startup(dp)
	# print("Готово")
	
	# print("Чистим базу")
	# await db.gino.drop_all()
	#
	# print("Готово")
	#
	# print("Создаем таблицы")
	# await db.gino.create_all()
	# print('Добавляем админа')
	# await comm.add_user(id = int(os.getenv("ADMIN_ID")), name = "")
	# print('Создаём покупку')
	# await purchase_commands.add_purchase(product_id = 1, amount = 1, address = '4343')
	# # for testing
	# print("Готово")
	
	await on_startup_notify(dp)


# await set_default_commands(dp)


def setup_django():
	os.environ.setdefault(
			"DJANGO_SETTINGS_MODULE",
			"django_project.django_project.settings"
	)
	os.environ.update({ 'DJANGO_ALLOW_ASYNC_UNSAFE':"true" })
	django.setup()


# async def on_shutdown(dp):
# 	await bot.close()


if __name__ == '__main__':
	setup_django()
	
	from aiogram import executor
	from handlers import dp
	
	executor.start_polling(dp, on_startup = on_startup)
