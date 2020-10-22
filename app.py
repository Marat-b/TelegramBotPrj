import os

from utils.db_api import db_gino
from loader import db
from utils.db_api import quick_commands as comm


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
    
    print("Готово")
    await on_startup_notify(dp)
    


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)
