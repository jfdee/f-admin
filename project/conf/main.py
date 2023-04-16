from dotenv import load_dotenv
from pydantic import BaseSettings


# Локальные настройки в .env файле
load_dotenv()


class Settings(BaseSettings):
    TIMEZONE: str = 'UTC'
    INSTALLED_APPS: list[str] = [
        'apps.organization',
        'apps.user',
    ]
    APP_MODELS: list[str] = [
        'aerich.models',
        *[f'{x}.models' for x in INSTALLED_APPS],
    ]

    # DATABASE
    DATABASE_URL: str = ''

    # REDIS
    REDIS_PORT: int = 6379
    REDIS_HOST: str = 'redis'
    REDIS_PASSWORD: str = ''
    REDIS_DB: int = 0

    class Config(BaseSettings.Config):
        env_file: str = '.env'
        env_file_encoding: str = 'utf-8'


settings = Settings()

__all__ = ('settings', )
