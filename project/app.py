import uvicorn
from convert_case import kebab_case, pascal_case
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

from conf import settings

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOW_ORIGINS,
    allow_credentials=settings.ALLOW_CREDENTIALS,
    allow_methods=settings.ALLOW_METHODS,
    allow_headers=settings.ALLOW_HEADERS
)


@app.get(path='/api/admin/items')
def get_menu_items():
    data: list[dict[str, str]] = []
    for name, meta in Tortoise.apps.get('models').items():
        if name in settings.ADMIN_EXCLUDE_MODELS:
            continue
        data.append({
            'code': kebab_case(string=name),
            'label': getattr(meta.Meta, 'verbose_name_plural', name),
            'fields': [],
        })
    return data


@app.get(path='/api/admin/items/{code}')
async def get_model_fields(code: str):
    model = Tortoise.apps['models'].get(pascal_case(code))
    meta = []
    for f_name, f_meta in model._meta.fields_map.items():
        meta.append({
            'name': f_name,
            'label': f_meta.description or f_name,
            'read_only': f_meta.generated,
            'required': f_meta.required,
            'allow_null': f_meta.null,
            'type': f_meta.field_type.__name__,
        })
    data = []
    for obj in await model.all():
        obj_data = {}
        for field in meta:
            obj_data[field['name']] = getattr(obj, field['name'])
        data.append(obj_data)
    return {'data': data, 'meta': meta}


# Вынесем сюда, ибо не пересчитывается после считывания env файла
TORTOISE_CONFIG = {
    'generate_schemas': True,
    'add_exception_handlers': True,
    'timezone': settings.TIMEZONE,
    'connections': {'default': settings.DATABASE_URL},
    'apps': {
        'models': {
            'models': settings.APP_MODELS,
            'default_connection': 'default',
        },
    },
}

register_tortoise(app, config=TORTOISE_CONFIG)


if __name__ == '__main__':
    uvicorn.run('app:app', host='localhost', port=8000, reload=True)
