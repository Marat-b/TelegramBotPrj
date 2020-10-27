from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.shemas.user import User


async def add_user(id: int, name: str, bonus: float = 0.0):
	try:
		user = User(id = id, name = name, bonus = bonus)
		await user.create()
	except UniqueViolationError:
		pass


async def select_all_users():
	users = await User.query.gino.all()
	return users


async def select_user(id: int):
	user = await User.query.where(User.id == id).gino.first()
	return user


async def count_users():
	total = await db.func.count(User.id).gino.scalar()
	return total


async def update_bonus(id: int):
	user = await User.get(id)  # .query.where(User.id == id).gino.first()
	bonus = user.bonus + 10
	await user.update(bonus = bonus).apply()
