import os

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.choise_invite import get_invite_code
from loader import dp, bot
from utils.db_api import quick_commands as comm


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    # await message.answer(f'Привет, {message.from_user.full_name}!')
    
    refferal = message.get_args()
    print('referral = {}'.format(refferal))
    
    if not refferal:
        chat_id = message.from_user.id
        bot_username = (await bot.get_me()).username
        print('chat_id = {}\nbot_username = {}\nreferral = {}'.format(chat_id, bot_username, refferal))
        text = f'Чтобы использовать этого бота введите код приглашения, либо пройдите по реферальной ссылке.'
        # \nРеферальная ссылка https://t.me/{bot_username}?start={chat_id}
        # await bot.send_message(chat_id, text)
    
        # await message.answer(text = 'Введите код приглашения', reply_markup = get_invite_code('invite'))
    else:
        user_id = message.from_user.id
        if int(refferal) != user_id:
            await message.answer(f'Привет, {message.from_user.full_name}!')
            await message.answer('Занесён по реферальной ссылке')
            await comm.add_user(id = user_id, name = message.from_user.username)
            if int(refferal) != int(os.getenv("ADMIN_ID")):
                await comm.update_bonus(int(refferal))
