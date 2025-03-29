echo off

cd project
if not exist pyproject.toml (
    aerich init -t app.TORTOISE_CONFIG
)

aerich init-db
aerich migrate
aerich upgrade
