import os

from pathlib import Path
from dotenv import load_dotenv

env = Path('.') / '.env'
load_dotenv(dotenv_path=env)

SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')

SECRET_KEY = os.getenv('SECRET_KEY')




