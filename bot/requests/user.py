from aiohttp import ClientSession
from bot.configs.get_settings import get_backend_settings
from bot.models.user import UserFull
from bot.requests.common import post_request


async def add_user(user: UserFull) -> None:
    settings = get_backend_settings()
    url = f"http://{settings.BACKEND_CLIENT_HOSTNAME}:{settings.BACKEND_CLIENT_PORT}/user/register"
    async with ClientSession() as session:
        async with session.post(url, params=dict(user)) as response:
            return
