from .base import *

SECRET_KEY = 'changemeforproduction'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
REDMINE_ID = 11176

BASE_URL = 'https://mpp.acdh.oeaw.ac.at'


ALLOWED_HOSTS = [
    "127.0.0.1"
]

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'mmp',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')