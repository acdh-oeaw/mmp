import os
from .base import *

SECRET_KEY = os.environ.get('SECRET_KEY', '1234verysecret')

DEBUG = os.environ.get('DEBUG', True)
REDMINE_ID = os.environ.get('REDMINE_ID', '18716')
PROJECT_NAME = os.environ.get('PROJECT_NAME', 'mmp')
BASE_URL = f"https://{PROJECT_NAME}.acdh.oeaw.ac.at"

VOCABS_DEFAULT_PEFIX = os.environ.get('VOCABS_DEFAULT_PEFIX', 'mmp')
VOCABS_SETTINGS = {
    'default_prefix': VOCABS_DEFAULT_PEFIX,
    'default_ns': f"http://www.vocabs/{VOCABS_DEFAULT_PEFIX}/",
    'default_lang': os.environ.get('VOCABS_DEFAULT_LANG', 'en'),
}

ADD_ALLOWED_HOST = os.environ.get('ALLOWED_HOST', '*')
ALLOWED_HOSTS = [
    "127.0.0.1",
    "0.0.0.0",
    ADD_ALLOWED_HOST,
]


DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_TYP', 'django.contrib.gis.db.backends.postgis'),
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST', '172.17.0.1'),
        'PORT': os.environ.get('DB_PORT', '5432')
    }
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')