from asgiref.sync import sync_to_async
from asyncpg import UniqueViolationError, RaiseError

# from utils.db_api.db_gino import db
# from utils.db_api.shemas.user import User
from django_project.user_manager.models import User


@sync_to_async
def add_user(user_id: int, username: str = '', name: str = '', bonus: float = 0.0) -> User:
    try:
        User(user_id=user_id, username=username,
             name=name,
             bonus=bonus).save()
    except UniqueViolationError:
        pass


# @sync_to_async
# def select_all_users():
# 	users = User.objects.all()
# 	return users


@sync_to_async
def select_user(user_id: int) -> User:
    user = User.objects.filter(user_id=user_id).first()
    return user


# async def count_users():
# 	total = await db.func.count(User.id).gino.scalar()
# 	return total

@sync_to_async
def update_bonus(user_id: int):
    try:
        user = User.objects.get(user_id=user_id)
        user.bonus += 10
        user.save()
    except RaiseError:
        pass


@sync_to_async
def is_admin(user_id: int):
    """Check for administrator rights"""
    try:
        user = User.objects.get(user_id=user_id)
        return user.supervisor
    except RaiseError:
        return False
