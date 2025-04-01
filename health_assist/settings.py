import os
from pathlib import Path

from decouple import config
from django.urls import reverse_lazy
from dotenv import load_dotenv
import environ
from django.utils.translation import gettext_lazy as _
import cloudinary
import cloudinary.uploader
import cloudinary.api

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = [
        'healthnet.finance',
]

# Application definition
MY_APPS = [
    'health_assist.accounts',
    'health_assist.web_pages',
    'health_assist.common',
    'health_assist.packages',
]

INSTALLED_APPS = [

                     "unfold",  # before django.contrib.admin
                     "unfold.contrib.filters",  # optional, if special filters are needed
                     "unfold.contrib.forms",  # optional, if special form elements are needed
                     'django.contrib.admin',
                     'django.contrib.auth',
                     'django.contrib.contenttypes',
                     'django.contrib.sessions',
                     'django.contrib.messages',
                     'django.contrib.staticfiles',
                     'crispy_forms',
                     'crispy_bootstrap4',
                     'rosetta',
                     'parler',
                     'cloudinary',
                     'cloudinary_storage',
                     'storages',

                 ] + MY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'health_assist.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'health_assist.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases


env = environ.Env()
environ.Env.read_env()

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv('NAME', config('NAME')),
        "USER": os.getenv("USER", config('USER')),
        "PASSWORD": os.getenv("PASSWORD", config('PASSWORD')),
        "HOST": os.getenv("HOST", config('HOST')),
        "PORT": os.getenv("PORT", config('PORT')),
    }
}
# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'bg'

LANGUAGES = [
    ('en', _('English')),
    ('bg', _('Bulgarian')),
]
TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = "bootstrap4"

STATIC_URL = 'static/'

STATICFILES_DIRS = (
    BASE_DIR / 'static',
)
LOCALE_PATHS = [
    BASE_DIR / 'locale',
]
PARLER_LANGUAGES = {
    None: (
        {'code': 'en', 'name': 'English'},
        {'code': 'bg', 'name': 'Bulgarian'},
    ),
    'default': {
        'fallback': 'bg',
    }
}

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'accounts.HnfUserModel'

LOGIN_REDIRECT_URL = reverse_lazy('health-home')
LOGOUT_REDIRECT_URL = reverse_lazy('login')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST', config('EMAIL_HOST'))
EMAIL_PORT = os.getenv('EMAIL_PORT', config('EMAIL_PORT'))
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', config('EMAIL_USE_TLS')) == "True"
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', config('EMAIL_HOST_USER'))
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', config('EMAIL_HOST_PASSWORD'))

cloudinary.config(
    cloud_name=os.getenv('CLOUD_NAME', config('CLOUD_NAME')),
    api_key=os.getenv('API_KEY', config('API_KEY')),
    api_secret=os.getenv('API_SECRET', config('API_SECRET')),
)

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

AWS_STORAGE_BUCKET_NAME = 'hnfbg-bkt'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_FILE_OVERWRITE = False

STORAGES = {
    'default': {
        'BACKEND': 'storages.backends.s3boto3.S3Boto3Storage',
    },
    'staticfiles': {
        'BACKEND': 'storages.backends.s3boto3.S3Boto3Storage',
    },
}

