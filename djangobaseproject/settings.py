import os
from pathlib import Path

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
SECRET_KEY = os.environ.get("SECRET_KEY", "1234verysecret")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
BASE_DIR = Path(__file__).resolve().parent.parent

if os.environ.get("DEBUG"):
    DEBUG = True
else:
    DEBUG = False

ADD_ALLOWED_HOST = os.environ.get("ALLOWED_HOST", "*")
ALLOWED_HOSTS = [
    "127.0.0.1",
    "0.0.0.0",
    ADD_ALLOWED_HOST,
]

if os.environ.get("SQLITE"):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": os.environ.get(
                "DB_TYP", "django.contrib.gis.db.backends.postgis"
            ),
            "OPTIONS": {"options": "-c search_path=public,mmp"},
            "NAME": os.environ.get("DB_NAME", "mmp"),
            "USER": os.environ.get("DB_USER", "postgres"),
            "PASSWORD": os.environ.get("DB_PASSWORD", "postgres"),
            "HOST": os.environ.get("DB_HOST", "localhost"),
            "PORT": os.environ.get("DB_PORT", "5432"),
            "DISABLE_SERVER_SIDE_CURSORS": True,
        }
    }


SHARED_URL = "https://shared.acdh.oeaw.ac.at/"
PROJECT_NAME = "djangobaseproject"


ACDH_IMPRINT_URL = "https://imprint.acdh.oeaw.ac.at/"
REDMINE_ID = os.environ.get("REDMINE_ID", "18716")

# Application definition

INSTALLED_APPS = [
    "dal",
    "django.contrib.admin",
    "dal_select2",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.gis",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework_gis",
    "reversion",
    "ckeditor",
    "django_filters",
    "rest_framework",
    "drf_spectacular",
    "mptt",
    "leaflet",
    "webpage",
    "vocabs",
    "infos",
    "archiv",
    "topics",
    "story_map",
    "layers",
    "generic_ac",
]
if DEBUG:
    INSTALLED_APPS.insert(10, "django_extensions")

CRISPY_TEMPLATE_PACK = "bootstrap4"
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
SPAGHETTI_SAUCE = {
    "apps": ["archiv", "topics"],
    "show_fields": False,
    "exclude": {"auth": ["user"]},
}
CORS_ALLOW_ALL_ORIGINS = True
AUTHENTICATION_BACKENDS = ("django.contrib.auth.backends.ModelBackend",)

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 50,
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "reversion.middleware.RevisionMiddleware",
]

ROOT_URLCONF = "djangobaseproject.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "djangobaseproject.wsgi.application"

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = "en"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles/")
STATIC_URL = "/static/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
MEDIA_URL = "/media/"
DATA_UPLOAD_MAX_MEMORY_SIZE = None

ARCHE_SETTINGS = {
    "project_name": ROOT_URLCONF.split(".")[0],
    "base_url": "https://id.acdh.oeaw.ac.at/{}".format(ROOT_URLCONF.split(".")[0]),
}

VOCABS_DEFAULT_PEFIX = os.environ.get("VOCABS_DEFAULT_PEFIX", "mmp")
VOCABS_SETTINGS = {
    "default_prefix": VOCABS_DEFAULT_PEFIX,
    "default_ns": f"http://www.vocabs/{VOCABS_DEFAULT_PEFIX}/",
    "default_lang": os.environ.get("VOCABS_DEFAULT_LANG", "en"),
}


SERIALIZATION_MODULES = {
    "geojson": "django.contrib.gis.serializers.geojson",
}

LEAFLET_CONFIG = {
    "DEFAULT_CENTER": (40, 10),
    "DEFAULT_ZOOM": 4,
    "MIN_ZOOM": 3,
    "OVERLAYS": [],
}

# default empty choice label = '-----'; if set to None it is removed as option
# https://django-filter.readthedocs.io/en/stable/ref/settings.html#filters-empty-choice-label
FILTERS_EMPTY_CHOICE_LABEL = None
CKEDITOR_UPLOAD_PATH = "uploads/"


GENERIC_AC_CONFIG = [
    {
        "app_name": "archiv",
        "model_name": "autor",
        "search_fields": [
            "name",
            "name_lat",
            "name_en",
            "name_fr",
            "name_it",
            "name_gr",
        ],
    },
    {
        "app_name": "archiv",
        "model_name": "ort",
        "search_fields": [
            "name",
            "name_antik",
            "name_de",
            "name_fr",
            "name_it",
            "name_gr",
        ],
        "additional_fields": {
            "art": {"lookup": "art", "label": "Type of Place"},
            "kategorie": {"lookup": "kategorie", "label": "Category of Place"},
        },
    },
    {"app_name": "archiv", "model_name": "text", "search_fields": ["title"]},
    {
        "app_name": "archiv",
        "model_name": "stelle",
        "search_fields": ["zitat", "text__title"],
        "additional_fields": {
            "text": {"lookup": "text", "label": "Text"},
        },
    },
    {
        "app_name": "archiv",
        "model_name": "keyword",
        "search_fields": [
            "stichwort",
            "wurzel",
            "varianten",
        ],
        "additional_fields": {"art": {"lookup": "art", "label": "Type of Keyword"}},
    },
    {
        "app_name": "archiv",
        "model_name": "usecase",
        "search_fields": [
            "title",
        ],
    },
]
