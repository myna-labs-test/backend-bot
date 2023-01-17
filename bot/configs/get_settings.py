from bot.configs.bot import BotSettings
from bot.configs.backend import BackendSettings


def get_backend_settings() -> BackendSettings:
    return BackendSettings()


def get_bot_settings() -> BotSettings:
    return BotSettings()
