from datetime import datetime

from aiogram import Dispatcher, types, Router
from aiogram.types.error_event import ErrorEvent
from bot.utils.loader import bot
from bot.exceptions.common import CommonException

exception_router = Router()


@exception_router.errors()
async def error_handler(exception: ErrorEvent) -> None:
    await bot.send_message(exception.update.message.chat.id, str(exception.exception))


