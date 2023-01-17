from tokenize import group
from aiogram import types, Router
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command
from bot.requests.user import add_user
from bot.models.user import UserFull

start_router = Router()


@start_router.message(Command('start'))
async def start_handler(msg: types.Message):
    user = UserFull(
        first_name=msg.from_user.first_name,
        last_name=msg.from_user.last_name,
        username=msg.from_user.username,
        tg_id=msg.from_user.id
    )
    await add_user(user)
    await msg.reply("Пользователь зарегистрирован")


@start_router.message(Command('cancel'))
async def cancel(msg: types.Message, state: FSMContext):
    cur = await state.get_state()
    if not cur:
        return
    await state.clear()
    await msg.reply('Отменено')
