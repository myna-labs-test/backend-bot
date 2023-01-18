from datetime import datetime
from typing import List, TypeVar, Optional
from pydantic import BaseModel
from aiogram import Dispatcher, types, Router
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup

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



