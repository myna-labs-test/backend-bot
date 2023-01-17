from pydantic import BaseSettings


class BotSettings(BaseSettings):
    BOT_TOKEN: str

    class Config:
        env_file: str = ".env"
