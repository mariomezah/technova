from pathlib import Path
from decouple import config, Csv
from django.urls import reverse_lazy

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config("SECRET_KEY")

DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

INSTALLED_APPS = [
    "unfold",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'clientes',
    'reportes',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

UNFOLD = {
    "SITE_TITLE": "TechNova Seguridad",
    "SITE_HEADER": "TechNova Seguridad",
    "SITE_SUBHEADER": "Sistema web para gestión de clientes y transacciones",
    "SITE_SYMBOL": "shield",
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": False,

    "SIDEBAR": {        
        "show_all_applications": False,
        "navigation": [
            {
                "title": "Gestión de clientes",
                "separator": True,
                "items": [
                    {
                        "title": "Clientes",
                        "icon": "person",
                        "link": reverse_lazy("admin:clientes_cliente_changelist"),
                    },
                    {
                        "title": "Transacciones",
                        "icon": "receipt_long",
                        "link": reverse_lazy("admin:clientes_transaccion_changelist"),
                    },
                ],
            },
            {
                "title": "Reportes internos",
                "separator": True,
                "items": [
                    {
                        "title": "Reporte de clientes",
                        "icon": "summarize",
                        "link": "/reportes/clientes/",
                    },
                    {
                        "title": "Reporte de transacciones",
                        "icon": "payments",
                        "link": "/reportes/transacciones/",
                    },
                ],
            },
        ],
    },
}

WSGI_APPLICATION = 'config.wsgi.application'


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST", default="127.0.0.1"),
        "PORT": config("DB_PORT", default="5432"),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]



LANGUAGE_CODE = 'es-pe'
TIME_ZONE = 'America/Lima'
USE_I18N = True
USE_TZ = True


STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

CSRF_TRUSTED_ORIGINS = config(
    "CSRF_TRUSTED_ORIGINS",
    default="https://www.technova.demo.org.pe",
    cast=Csv()
)


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
