from aiohttp import ClientSession
from bot.configs.get_settings import get_backend_settings
from bot.models.message import MessageNew
from bot.utils.formatter import format_dict_safe
from bot.exceptions.common import CommonException


async def add_message(message: MessageNew):
    settings = get_backend_settings()
    url = f"http://{settings.BACKEND_CLIENT_HOSTNAME}:{settings.BACKEND_CLIENT_PORT}/user/message"
    async with ClientSession() as session:
        async with session.post(url, params=format_dict_safe(message)) as response:
            if not response.status == 200:
                raise CommonException((await response.json())['message'], None)

