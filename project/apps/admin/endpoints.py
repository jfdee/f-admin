from convert_case import kebab_case, pascal_case
from starlette import status
from starlette.exceptions import HTTPException
from tortoise import Tortoise

from conf import settings


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


def _get_model(code: str):
    model = Tortoise.apps['models'].get(pascal_case(code))
    if not model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return model


async def _get_model_instance(code: str, pk: int):
    model = _get_model(code)
    instance = await model.filter(pk=pk).first()
    if not instance:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return instance


async def menu_item_list(code: str):
    model = _get_model(code)
    meta = []
    for f_name, f_meta in model._meta.fields_map.items():
        read_only = any([
            f_meta.generated,
            getattr(f_meta, 'auto_now_add', False),
            getattr(f_meta, 'auto_now', False),
        ])
        meta.append({
            'name': f_name,
            'label': f_meta.description or f_name,
            'read_only': read_only,
            'required': f_meta.required,
            'allow_null': f_meta.null,
            'type': f_meta.field_type.__name__,
        })
    data = []
    for obj in await model.all().order_by('-created_at'):
        obj_data = {}
        for field in meta:
            obj_data[field['name']] = getattr(obj, field['name'])
        data.append(obj_data)
    return {'data': data, 'meta': meta}


async def menu_item_post(code: str, data: dict):
    model = _get_model(code)
    instance = await model.create(**data)
    return {'pk': instance.pk}


async def menu_item_instance_retrieve(code: str, pk: int):
    instance = await _get_model_instance(code, pk)
    return dict(instance)


async def menu_item_instance_put(code: str, pk: int, data: dict):
    instance = await _get_model_instance(code, pk)
    for key, value in data.items():
        setattr(instance, key, value)
    await instance.save()
    return dict(instance)


async def menu_item_instance_delete(code: str, pk: int):
    instance = await _get_model_instance(code, pk)
    await instance.delete()


__all__ = (
    'get_menu_items',
    'menu_item_list',
    'menu_item_post',
    'menu_item_instance_retrieve',
    'menu_item_instance_put',
    'menu_item_instance_delete',
)
