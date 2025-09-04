from pathlib import Path
from datetime import timedelta
#import sricrm.custom_token

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-+_#7yk$@ow=-nrk+)31$-i2o&^#71_-ju(d7m%fw$163_j^8dc'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_yasg',
    'knox',
    'sricrm'
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

ROOT_URLCONF = 'MyCRM.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'MyCRM.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mycrm',
        'USER': 'root',
        'PASSWORD': 'Sriram',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}

AUTH_USER_MODEL = 'sricrm.Users'

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'knox.auth.TokenAuthentication',
    ],
}
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Token': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization',
            'description': "Format: Token <your_token>"
        }
    },
}
from hashlib import sha512
REST_KNOX = {
    'SECURE_HASH_ALGORITHM': sha512,
    "TOKEN_TTL": timedelta(hours=24),
    "AUTO_REFRESH": True,
    "AUTH_HEADER_PREFIX": "Token",
    "USER_SERIALIZER": "sricrm.serializers.UserRegisterSerializer",
    "TOKEN_LIMIT_PER_USER": 1,
    "AUTH_TOKEN_CHARACTER_LENGTH": 128,
}
