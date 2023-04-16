echo off

cd project
:: если нет конфигурационного файла, создаем его
if not exist pyproject.toml (
    aerich init -t app.TORTOISE_CONFIG
)

:: создаем миграцию
aerich init-db
aerich migrate
:: применяем миграции
aerich upgrade
