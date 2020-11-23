import uuid

from utils.db_api.shemas.purchase import Purchase


async def add_purchase(product_id: int, amount: int, address: str, payed: bool = False):
	id = uuid.uuid4()
	purchase = Purchase(id = str(id), product_id = int(product_id), amount = int(amount), address = address,
	                    payed = payed)
	await purchase.create()
	return id


async def update_payed(id: str, payed: bool):
	purchase = await Purchase.get(id)
	await purchase.update(payed = payed).apply()
