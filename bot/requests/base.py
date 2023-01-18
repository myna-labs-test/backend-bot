from bot.utils.config import settings
from abc import ABC, abstractmethod
from aiohttp import ClientSession


class BaseClient:
    host: str
    port: str

    @classmethod
    def __make_url(cls, endpoint: str):
        return f"http://{cls.host}:{cls.port}{endpoint}"

    @classmethod
    async def post(cls, endpoint: str, **kwargs):
        async with ClientSession() as session:
            async with session.post(cls.__make_url(endpoint), **kwargs) as response:
                return response.status, await response.json()

    @classmethod
    async def put(cls, endpoint: str, **kwargs):
        async with ClientSession() as session:
            async with session.put(cls.__make_url(endpoint), **kwargs) as response:
                return response.status, await response.json()

    @classmethod
    async def get(cls, endpoint: str, **kwargs):
        async with ClientSession() as session:
            async with session.get(cls.__make_url(endpoint), **kwargs) as response:
                return response.status, await response.json()


class APIClient(BaseClient):
    host: str = settings.BACKEND_CLIENT_HOSTNAME
    port: str = settings.BACKEND_CLIENT_PORT


class APICharacters(BaseClient):
    host: str = settings.BACKEND_CHARACTER_HOSTNAME
    port: str = settings.BACKEND_CHARACTER_PORT
