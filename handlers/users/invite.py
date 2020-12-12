from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from data.config import INVITE_CODE
from filters import IsNotMember, IsMember
from loader import dp
from states.invite_state import InviteState
from utils.db_api import user_commands as comm


@dp.message_handler(Command('invite'), IsNotMember())
async def invite(message: types.Message):
	await message.answer(text = 'Введите код приглашения:')
	await InviteState.PutInviteCode.set()


@dp.message_handler(state = InviteState.PutInviteCode)
async def invite_code(message: types.Message, state: FSMContext):
	# data = await state.get_data()
	invite_text = message.text
	if invite_text.upper() == INVITE_CODE:
		user_id = message.from_user.id
		username = message.from_user.username
		name = message.from_user.full_name
		await comm.add_user(user_id = user_id, username = username, name = name)
		await message.answer(f'Привет, {message.from_user.full_name}!\n'
		                     'Код приглашения верен. Вы можете выбирать товар и совершать покупки.')
	else:
		await message.answer('Код приглашения не верен. Попробуйте ввести ещё раз после команды /invite')
	# await message.answer(text = message.text)
	await state.finish()
