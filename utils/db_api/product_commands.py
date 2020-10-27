import gino
from asyncpg import UniqueViolationError

from utils.db_api import db_gino
from utils.db_api.db_gino import db
from utils.db_api.shemas.product import Product


async def add_product(name: str, description: str, price: float = 0.0, photo: bin = None):
	try:
		product = Product(name = name, description = description, price = price)
		await product.create()
	except UniqueViolationError:
		pass


async def get_products(name: str):
	print('products_command -> get_products -> name={}'.format(name))
	query = db.text(f"select * from products where name like \'%{name}%\'")
	products = await db.all(query)
	# products = await Product.query.where(Product.name db.func.like(name)).gino.all()
	
	return products
