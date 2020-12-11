import os

from utils.db_api import db_gino, product_commands, purchase_commands
from loader import db
from utils.db_api import user_commands as comm


async def on_startup(dp):
	import filters
	import middlewares
	filters.setup(dp)
	middlewares.setup(dp)
	
	from utils.notify_admins import on_startup_notify
	print("Подключаем БД")
	await db_gino.on_startup(dp)
	print("Готово")
	
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
	# await product_commands.add_product(name = 'Pizza', description = 'Богатая крахмалом',
	#                                    photo = 'AgACAgIAAxkBAAIEYV-YWqKEl2sJp6HbXzidUAcXf85fAAKIrzEbaCvJSIgliXTciiDAAAFMEJguAAMBAAMCAAN5AAMfVwIAARsE',
	#                                    price = 1.23)
	# await product_commands.add_product(name = 'Popcorn', description = 'Богатая пектином',
	#                                    photo = 'AgACAgIAAxkBAAIEYV-YWqKEl2sJp6HbXzidUAcXf85fAAKIrzEbaCvJSIgliXTciiDAAAFMEJguAAMBAAMCAAN5AAMfVwIAARsE',
	#                                    price = 2.23)
	# await product_commands.add_product(name = 'Honey', description = 'Богатый сахаром',
	#                                    photo = 'AgACAgIAAxkBAAIEYV-YWqKEl2sJp6HbXzidUAcXf85fAAKIrzEbaCvJSIgliXTciiDAAAFMEJguAAMBAAMCAAN5AAMfVwIAARsE',
	#                                    price = 1.2367)
	# await product_commands.add_product(name = 'Pasta', description = 'Богатый зеленью',
	#                                    photo = 'AgACAgIAAxkBAAIEgl-cJPKM6H686VsxViYTuhO-WFouAAKOsDEbNnngSKGA8l32kdtNg00SlS4AAwEAAwIAA3kAA0PoBQABGwQ',
	#                                    price = 1.2367)
	# await product_commands.add_product(name = 'Potato', description = 'Very delicious',
	#                                    photo = 'AgACAgIAAxkBAAIEYV-YWqKEl2sJp6HbXzidUAcXf85fAAKIrzEbaCvJSIgliXTciiDAAAFMEJguAAMBAAMCAAN5AAMfVwIAARsE',
	#                                    price = 1.23)
	
	# await product_commands.add_product(name = 'Parrot', description = 'Very delicious',
	#                                    photo = 'AgACAgIAAxkBAAIE_1-dkhSIWcZ7teRpcAr0e0YivhWIAAIfsTEbQWPoSIZCTMaj_8VOGLNFmC4AAwEAAwIAA20AA494AgABGwQ',
	#                                    price = 10.23)
	# await product_commands.add_product(name = 'Popcorn', description = 'Very delicious',
	#                                    photo = 'AAMCAgADGQEAAgURX52apRtyDZfGmO58Qd_zX-0am_kAAp0JAAJBY-hIyCaG5nZ2iHantqeZLgADAQAHbQAD4BYAAhsE',
	#                                    price = 10.23)
	
	print("Готово")
	await on_startup_notify(dp)


if __name__ == '__main__':
	from aiogram import executor
	from handlers import dp
	
	executor.start_polling(dp, on_startup = on_startup)
