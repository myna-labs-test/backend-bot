from pydantic import BaseSettings


class BackendSettings(BaseSettings):
    BACKEND_CLIENT_HOSTNAME: str
    BACKEND_CLIENT_PORT: str
    BACKEND_CHARACTER_HOSTNAME: str
    BACKEND_CHARACTER_PORT: str

    class Config:
        env_file: str = ".env"
