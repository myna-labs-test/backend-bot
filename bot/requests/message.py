from bot.models.message import MessageNew
from bot.utils.formatter import format_dict_safe
from bot.exceptions.common import CommonException
from bot.requests.base import APICharacters


async def add_message(message: MessageNew) -> None:
    status, data = await APICharacters.post('/user/message', params=format_dict_safe(message))
    if not status == 200:
        raise CommonException(data['message'], None)

