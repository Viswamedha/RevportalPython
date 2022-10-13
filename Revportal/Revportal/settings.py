"""






"""

# Imports
from pathlib import Path
from decouple import config
import os 


BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = config('SECRET_KEY', cast = str)


POSTGRES_USER = config('POSTGRES_USER', cast = str)
POSTGRES_PASS = config('POSTGRES_PASS', cast = str)
POSTGRES_HOST = config('POSTGRES_HOST', cast = str)
POSTGRES_PORT = config('POSTGRES_PORT', cast = int)
POSTGRES_DB   = config('POSTGRES_DB',   cast = str)


EMAIL_EMAIL = config('EMAIL', cast = str)
EMAIL_PASSWORD = config('EMAIL_PASS', cast = str)


DEBUG = True
ALLOWED_HOSTS = ['*'] # Change in future


DJANGO_CORE_APPS = [
    #'admin_volt.apps.AdminVoltConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
MY_APPS = [
    'revwand.apps.RevwandConfig',
    'revwizard.apps.RevwizardConfig'
]
THIRD_PARTY_APPS = [
    'django_cleanup.apps.CleanupConfig',
]
INSTALLED_APPS = MY_APPS + DJANGO_CORE_APPS + THIRD_PARTY_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'revportal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS':  [os.path.join(BASE_DIR, 'templates'),],
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


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': POSTGRES_DB,
        'USER': POSTGRES_USER,
        'PASSWORD': POSTGRES_PASS,
        'HOST': POSTGRES_HOST,
        'PORT': POSTGRES_PORT,
    },
    'backup': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
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


LANGUAGE_CODE = 'en-uk'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


WSGI_APPLICATION = 'revportal.wsgi.application'
ASGI_APPLICATION = 'revportal.asgi.application'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = EMAIL_EMAIL
EMAIL_HOST_PASSWORD = EMAIL_PASSWORD


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


AUTH_USER_MODEL = 'revwand.RevportalUser'
SITE_URL = 'http://77.102.37.242:8000'


LOGIN_URL = '../'
LOGIN_REDIRECT_URL = '/userprofile'
LOGOUT_REDIRECT_URL = '/'


SESSION_COOKIE_PATH = '/;HttpOnly'
SESSION_COOKIE_HTTPONLY = True





