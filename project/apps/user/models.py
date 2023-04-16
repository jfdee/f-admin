from tortoise import (fields, models)
from tortoise.contrib.pydantic import pydantic_model_creator


class User(models.Model):
    created_at = fields.DatetimeField(description='Дата создания', auto_now_add=True)
    username = fields.CharField(description='Логин', max_length=128)
    email = fields.CharField(description='Почта', max_length=128)
    full_name = fields.CharField(description='ФИО', max_length=256)

    class Meta:
        verbose_name: str = 'Пользователь'
        verbose_name_plural: str = 'Пользователи'


UserPydantic = pydantic_model_creator(User)


__all__ = ('User', )
