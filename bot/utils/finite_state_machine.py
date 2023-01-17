from datetime import datetime
from typing import List, TypeVar, Optional
from pydantic import BaseModel
from aiogram import Dispatcher, types, Router
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup

from bot.requests import group as group_requests, homeworks as homeworks_requests
from bot.utils.formatter import format_date, format_records_enumerated
from bot.models.homework import Homework
from bot.models.chats import ChatsShortLink
from bot.utils.loader import bot

T = TypeVar("T", bound=BaseModel)


async def print_canceled(msg: types.Message, state: Optional[FSMContext] = None) -> None:
    await bot.send_message(msg.chat.id, "Список пуст\nОтменено", parse_mode="HTML")
    if state:
        await state.clear()


async def print_models(
    msg: types.Message,
    state: FSMContext,
    models: List[T],
    description: str,
) -> None:
    await msg.reply(description)
    result = '\n'.join(map(str,models))
    if not result:
        await print_canceled(msg,state)
        return
    await bot.send_message(msg.chat.id, result, parse_mode="HTML")


async def prepare_chat_id(msg: types.Message, state: FSMContext) -> None:
    chats = await group_requests.get_chats_of_user(msg.from_user.id)
    chats = format_records_enumerated(chats, ChatsShortLink)
    await print_models(msg,state,chats,'Вы состоите в следующих чатах:')
    await bot.send_message(msg.chat.id, 'Выберете id чата:')


