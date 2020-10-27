import os

from utils.db_api import db_gino, product_commands
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

    print("Чистим базу")
    await db.gino.drop_all()

    print("Готово")

    print("Создаем таблицы")
    await db.gino.create_all()
    print('Добавляем админа')
    await comm.add_user(id = int(os.getenv("ADMIN_ID")), name = "")
    # for testing
    await product_commands.add_product(name = 'Картошка', description = 'Богатая крахмалом', price = 10.23)
    await product_commands.add_product(name = 'Крыжовник', description = 'Богатая пектином', price = 20.23)
    await product_commands.add_product(name = 'Мёд', description = 'Богатый сахаром', price = 100.2367)
    await product_commands.add_product(name = 'Капуста', description = 'Богатый зеленью', price = 100.2367)

    print("Готово")
    await on_startup_notify(dp)
    


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)
