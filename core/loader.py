import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit('Файл .env не найден. Переменные не загружены')
else:
    load_dotenv()

TOKEN = os.getenv('TOKEN')
admin_id = os.getenv('admin_id')
