from aiohttp import ClientSession
from bot.configs.get_settings import get_backend_settings
from bot.models.user import UserFull
from bot.utils.formatter import format_dict_safe


async def add_user(user: UserFull) -> None:
    settings = get_backend_settings()
    url = f"http://{settings.BACKEND_CLIENT_HOSTNAME}:{settings.BACKEND_CLIENT_PORT}/user/register"
    async with ClientSession() as session:
        async with session.post(url, params=format_dict_safe(user)) as response:
            return
