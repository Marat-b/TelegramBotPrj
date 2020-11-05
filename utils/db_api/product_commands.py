import gino
from asyncpg import UniqueViolationError

from utils.db_api import db_gino
from utils.db_api.db_gino import db
from utils.db_api.shemas.product import Product


async def add_product(name: str, description: str, photo: str, price: float = 0.0):
	try:
		product = Product(name = name, description = description, photo = photo, price = price)
		await product.create()
	except UniqueViolationError:
		pass


async def get_products(name: str) -> Product:
	print('products_command -> get_products -> name={}'.format(name))
	query = db.text(f"select * from products where upper(name) like \'%{name}%\'")
	products = await db.all(query)
	# products = await Product.query.where(Product.name db.func.like(name)).gino.all()
	
	return products


async def get_product_by_photoid(photoid: str) -> Product:
	product = await Product.query.where(Product.photo == photoid).gino.first()
	return product


async def get_product_by_itemid(itemid: int) -> Product:
	product = await Product.query.where(Product.id == itemid).gino.first()
	return product
