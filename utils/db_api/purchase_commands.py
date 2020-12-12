import uuid

from asgiref.sync import sync_to_async

from django_project.user_manager.models import Purchase, User, Product


@sync_to_async
def add_purchase(user_id: int, product_id: int, amount: float, quantity: int, address: str, payed: bool = False):
	purchase_id = uuid.uuid4()
	user = User.objects.get(user_id = user_id)
	product = Product.objects.get(id = product_id)
	Purchase(id = str(purchase_id), buyer = user, product = product, amount = amount, quantity = int(
			quantity), shipping_address = address, payed = payed).save()
	return purchase_id


@sync_to_async
def update_payed(id: str, payed: bool):
	purchase = Purchase.objects.get(id = id)
	purchase.payed = payed
	purchase.save()
