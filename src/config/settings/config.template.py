from .get_env import get_env_or_default
import os
from django.core.management.utils import get_random_secret_key
from datetime import timedelta

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SCHOOLS_DIR = os.path.join(os.path.split(BASE_DIR)[0], 'schools')
PATTERNS_DIR = os.path.join(SCHOOLS_DIR, 'patterns.json')

DEBUG = False
SECRET_KEY = get_random_secret_key()
ALLOWED_HOSTS = ['*']

# BD configurations
ENGINE = 'django.db.backends.postgresql_psycopg2'
NAME_DB = get_env_or_default('NAME_DB', 'postgres')
USER_NAME = get_env_or_default('USER_NAME', 'postgres')
USER_PW = get_env_or_default('USER_PW', 'postgres')
HOST = get_env_or_default('HOST', 'db')
PORT = get_env_or_default('PORT', '5432')

