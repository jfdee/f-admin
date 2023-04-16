from tortoise import (fields, models)


class User(models.Model):
    created_at = fields.DatetimeField(description='Дата создания', auto_now_add=True)
    username = fields.CharField(description='Логин', max_length=128)
    email = fields.CharField(description='Почта', max_length=128)
    full_name = fields.CharField(description='ФИО', max_length=256)


__all__ = ('User', )
