from dataclasses import dataclass
from typing import List

from environs import Env


@dataclass
class Bot:
    token: str
    admins: List[int]


@dataclass
class DbConfig:
    host: str
    port: str
    name: str
    password: str
    user: str


@dataclass
class Config:
    bot: Bot
    db: DbConfig


def load_config(path: str = None):
    env = Env()
    env.read_env(path)
    return Config(
        bot=Bot(
            token=env.str('BOT_TOKEN'),
            admins=list(map(int, env.list('ADMINS')))
        ),
        db=DbConfig(
            host=env.str('DB_HOST'),
            password=env.str('DB_PASSWORD'),
            user=env.str('DB_USER'),
            name=env.str('DB_NAME'),
            port=env.str('DB_PORT')
        )
    )
