import logging
from dataclasses import dataclass, field

from environs import Env

env = Env()
env.read_env()


@dataclass
class BotConfig:
    """Bot configuration."""

    token: str = env.str("TELEGRAM_TOKEN")
    admins: list = field(default_factory=lambda: env.list("ADMIN_IDS"))
    debug: bool = env.bool("DEBUG", False)
    log_chat_id: int = -1002140838197


@dataclass
class MongoDBConfig:
    """MongoDB configuration."""

    host: str = env.str("MONGODB_HOST")
    port: int = env.int("MONGODB_PORT")
    username: str = env.str("MONGODB_USERNAME")
    password: str = env.str("MONGODB_PASSWORD")
    database: str = env.str("MONGODB_DATABASE")


@dataclass
class Configuration:
    """All in one configuration's class."""

    bot = BotConfig()
    db = MongoDBConfig()


conf = Configuration()
