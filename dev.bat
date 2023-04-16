echo off
if not exist venv (
    echo "init venv..."
    call python -m venv venv
)
call venv\Scripts\activate
call python -m pip install -r requirements.txt
