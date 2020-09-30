from .get_env import get_env_or_default
from django.core.management.utils import get_random_secret_key
from datetime import timedelta

DEBUG = False
SECRET_KEY = get_random_secret_key()
ALLOWED_HOSTS = ['*']

# BD configurations
ENGINE = 'django.db.backends.postgresql_psycopg2'
NAME_DB = get_env_or_default('NAME_DB', 'course')
USER_NAME = get_env_or_default('USER_NAME', 'course')
USER_PW = get_env_or_default('USER_PW', 'course')
HOST = get_env_or_default('HOST', 'localhost')
PORT = get_env_or_default('PORT', '5432')

