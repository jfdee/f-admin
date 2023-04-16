import uvicorn
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from conf import settings


app = FastAPI()

# Вынесем сюда, ибо не пересчитывается после считывания env файла
TORTOISE_CONFIG = {
    'generate_schemas': True,
    'add_exception_handlers': True,
    'timezone': settings.TIMEZONE,
    'connections': {'default': settings.DATABASE_URL},
    'apps': {
        'models': {
            'models': settings.APP_MODELS, 'default_connection': 'default',
        }
    }
}

register_tortoise(app, config=TORTOISE_CONFIG)

if __name__ == '__main__':
    uvicorn.run('app:app', host='localhost', port=8000, reload=True)
