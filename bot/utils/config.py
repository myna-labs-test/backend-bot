from pydantic import BaseSettings


class Settings(BaseSettings):

    BACKEND_CLIENT_HOSTNAME: str
    BACKEND_CLIENT_PORT: str
    BACKEND_CHARACTER_HOSTNAME: str
    BACKEND_CHARACTER_PORT: str
    BOT_TOKEN: str

    class Config:
        env_file: str = ".env"


settings = Settings()

