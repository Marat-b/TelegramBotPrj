from asgiref.sync import sync_to_async
from asyncpg import UniqueViolationError

from django_project.user_manager.models import Product


@sync_to_async
def add_product(name: str, description: str, photo: str, price: float = 0.0):
	try:
		product = Product(name = name, description = description, photo = photo, price = price).save()
		return product
	except UniqueViolationError:
		pass


@sync_to_async
def get_products(name: str) -> Product:
	print('products_command -> get_products -> name={}'.format(name))
	# query = db.text(f"select * from products where upper(name) like \'%{name}%\'")
	products = Product.objects.filter(name__icontains = name)
	# products = await Product.query.where(Product.name db.func.like(name)).gino.all()
	
	return products


@sync_to_async
def get_product_by_photoid(photoid: str) -> Product:
	product = Product.objects.filter(photo = photoid).first()
	return product


@sync_to_async
def get_product_by_itemid(itemid: int) -> Product:
	product = Product.objects.filter(id = itemid).first()
	return product
