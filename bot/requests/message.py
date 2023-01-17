from .common import post_request
from aiohttp import ClientSession
from bot.configs.get_settings import get_backend_settings
from bot.models.message import MessageNew


async def add_message(message: MessageNew):
    settings = get_backend_settings()
    url = f"http://{settings.BACKEND_CLIENT_HOSTNAME}:{settings.BACKEND_CLIENT_PORT}/user/register"
    async with ClientSession() as session:
        async with session.post(url, params=dict(message)) as response:
            return

