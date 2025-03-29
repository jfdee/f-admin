from datetime import datetime

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


DATE_FORMAT: str = '%d.%m.%Y'
DATETIME_FORMAT: str = '%d.%m.%Y %H:%S'


def to_representation(fields: list, queryset) -> list:
    """object -> json"""
    items = []
    for obj in queryset:
        item = {}
        for field in fields:
            value = getattr(obj, field['name'])
            if value and field['type'] == 'datetime':
                value = value.strftime(DATETIME_FORMAT)
            if value and field['type'] == 'date':
                value = value.strftime(DATE_FORMAT)
            item[field['name']] = value
        items.append(item)
    return items


def to_internal_value(model, data: dict):
    """json -> object"""
    for key, value in data.items():
        f_meta = model._meta.fields_map[key]
        f_type = f_meta.field_type.__name__
        if f_type == 'datetime':
            value = datetime.strptime(value, DATETIME_FORMAT)
        if f_type == 'date':
            value = datetime.strptime(value, DATE_FORMAT).date()
        if f_type == 'bool' and value is None:
            value = f_meta.default
        if f_type == 'int':
            value = f_meta.default if not value else int(value)
        data[key] = value


def get_fields_meta(model) -> list:
    fields = []
    for f_name, f_meta in model._meta.fields_map.items():
        if getattr(f_meta, 'related_model', None):
            # fk
            continue
        # if f_meta.allows_generated:
            # fk _id
            # continue
        read_only = any([
            f_meta.generated,
            getattr(f_meta, 'auto_now_add', False),
            getattr(f_meta, 'auto_now', False),
        ])
        fields.append({
            'name': f_name,
            'label': f_meta.description or f_name,
            'read_only': read_only,
            'required': f_meta.required,
            'allow_null': f_meta.null,
            'type': f_meta.field_type.__name__,
        })
    return fields


async def menu_item_list(code: str):
    model = _get_model(code)
    queryset = await model.all().order_by('-created_at')
    fields_meta = get_fields_meta(model)
    items = to_representation(fields=fields_meta, queryset=queryset)
    return {'data': items, 'meta': fields_meta}


async def menu_item_post(code: str, data: dict):
    model = _get_model(code)
    to_internal_value(model=model, data=data)
    instance = await model.create(**data)
    return {'pk': instance.pk}


async def menu_item_instance_retrieve(code: str, pk: int):
    instance = await _get_model_instance(code, pk)
    return dict(instance)


async def menu_item_instance_put(code: str, pk: int, data: dict):
    model = _get_model(code)
    to_internal_value(model=model, data=data)
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
