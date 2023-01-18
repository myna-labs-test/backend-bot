from bot.models.user import UserFull
from bot.utils.formatter import format_dict_safe
from bot.exceptions.common import CommonException
from bot.requests.base import APIClient


async def add_user(user: UserFull) -> None:
    status, data = await APIClient.post('/user/register', params=format_dict_safe(user))
    if not status == 200:
        raise CommonException(data['message'], None)
