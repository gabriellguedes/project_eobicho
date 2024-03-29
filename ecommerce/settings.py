import os
import django_heroku
from decouple import config, Csv
from pathlib import Path
from django.urls import reverse_lazy

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG =  config('SECRET_KEY')

ALLOWED_HOSTS = config('DEBUG', default=False, cast=bool)

#CONFIGURAÇÕES DO EMAIL
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'gguedes10@gmail.com'
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = config('EMAIL_USE_TLS')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_HOST = config('EMAIL_HOST')

# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Apps de terceiros
    'localflavor',
    'widget_tweaks',
    'fontawesomefree',
    'bootstrapform',
    'rolepermissions',
    # Meus Apps 
    'ecommerce.accounts',
    'ecommerce.core',
    'ecommerce.consultorio',
    'ecommerce.estoque',
    'ecommerce.ficha',
    'ecommerce.ficha.boca',
    'ecommerce.ficha.doenca',
    'ecommerce.ficha.especie',
    'ecommerce.ficha.olhos',
    'ecommerce.ficha.orelhas',
    'ecommerce.ficha.patas',
    'ecommerce.ficha.pele',
    'ecommerce.ficha.pelos',
    'ecommerce.ficha.peso',
    'ecommerce.ficha.temperamento',
    'ecommerce.ficha.raca',
    'ecommerce.ficha.unhas',
    'ecommerce.pet',
    'ecommerce.services',
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

ROOT_URLCONF = 'ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'ecommerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME'),
        'HOST': config('DB_HOST'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'PORT': config('DB_PORT'),
        'OPTIONS': {
            'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"'
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True

DATE_INPUT_FORMATS = ['%d/%m/%Y']
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS =(os.path.join(BASE_DIR, 'static')),

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGIN_URL = 'core:home'
LOGIN_REDIRECT_URL = 'core:home'
LOGOUT_REDIRECT_URL = '/accounts/login'

ROLEPERMISSIONS_MODULE = "ecommerce.roles"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
django_heroku.settings(locals())

#del DATABASES['default']['OPTIONS']['sslmode']
