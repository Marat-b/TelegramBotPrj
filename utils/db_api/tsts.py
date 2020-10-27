import asyncio

from data import config
from utils.db_api.db_gino import db
from utils.db_api import user_commands, product_commands


async def tst():
    await db.set_bind(config.POSTGRES_URI)
    await db.gino.drop_all()
    await db.gino.create_all()

    print("Добавляем пользователей")
    # await user_commands.add_user(1, "One", 666)
    # await quick_commands.add_user(2, "Vasya", "vv@gmail.com")
    # await quick_commands.add_user(3, "1", "1")
    # await quick_commands.add_user(4, "1", "1")
    # await quick_commands.add_user(5, "John", "john@mail.com")
    print("Готово")
    print('Добавляем товары')
    await product_commands.add_product(name = 'Картошка', description = 'Богатая крахмалом', price = 10.23)
    await product_commands.add_product(name = 'Крыжовник', description = 'Богатая пектином', price = 20.23)
    await product_commands.add_product(name = 'Мёд', description = 'Богатый сахаром', price = 100.2367)
    await product_commands.add_product(name = 'Капуста', description = 'Богатый зеленью', price = 100.2367)
    products = await product_commands.get_products('К')
    print('products = {}'.format(products))
    products = await product_commands.get_products('Z')

    print('products = {}'.format(products))

    # users = await user_commands.select_all_users()
    # print(f"Получил всех пользователей: {users}")
    #
    # count_users = await user_commands.count_users()
    # print(f"Всего пользователей: {count_users}")
    #
    # user = await user_commands.select_user(id = 5)
    # print(f"Получил пользователя: {user}")


loop = asyncio.get_event_loop()
loop.run_until_complete(tst())
