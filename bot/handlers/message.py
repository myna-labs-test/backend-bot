from aiogram import Dispatcher, types, Router
from bot.models.user import UserShort
from bot.requests.character import get_active_character
from bot.models.message import MessageNew, SenderType
from bot.requests.message import add_message
from bot.requests.character import get_character_text_response
from aiogram.fsm.context import FSMContext

message_router = Router()


@message_router.message()
async def message_handler(msg: types.Message) -> None:
    user = UserShort(
        tg_id=msg.from_user.id
    )
    active_character = await get_active_character(user)
    message = MessageNew(
        sender_type=SenderType.USER,
        message=msg.text,
        character_id=active_character.character_id,
        tg_id=msg.from_user.id,
    )
    await add_message(message)
    response = await get_character_text_response(message)
    await msg.reply(response.text)