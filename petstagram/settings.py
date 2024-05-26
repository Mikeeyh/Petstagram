import os
from pathlib import Path

from django.urls import reverse_lazy

# BASE_DIR should always point to the 'manage.py' directory
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-jmh7*h(np%%k@_-(@=u+%ze*^mkh6encx8x2bwkvmh!!plk^4s'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False  # to see 404.html in browser it should be on debug FALSE
#
# ALLOWED_HOSTS = [
#     'localhost',  # for 404.html we add this too
# ]

# FOR DEPL:
DEBUG = os.environ.get('DEBUG', 1)

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(" ")
CSRF_TRUSTED_ORIGINS = [f"https://{host}" for host in ALLOWED_HOSTS]

INSTALLED_APPS = [
    # Django Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party Apps

    # Project Apps
    "petstagram.photos",
    "petstagram.pets",
    "petstagram.accounts",
    "petstagram.common"
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

ROOT_URLCONF = 'petstagram.urls'

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

WSGI_APPLICATION = 'petstagram.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# URL prefix in the client
STATIC_URL = 'static/'

# Directory on the file system
STATICFILES_DIRS = (
    BASE_DIR / 'staticfiles',
)

MEDIA_ROOT = BASE_DIR / 'mediafiles'  # for our model PetPhoto to upload the photos in 'mediafiles'

MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGGING = {
    'version': 1,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['console'],
        }
    }
}

AUTH_USER_MODEL = 'accounts.PetstagramUser'  # giving the path to the our custom user

LOGIN_REDIRECT_URL = reverse_lazy('index')
LOGIN_URL = reverse_lazy('signin user')

LOGOUT_REDIRECT_URL = reverse_lazy('index')


# FOR EMAIL FUNCTIONALITY
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'in-v3.mailjet.com'
EMAIL_PORT = 587
EMAIL_USE_TSL = True
EMAIL_HOST_USER = 'a9ede7a85c06727b7890c17a236d7be7'  # api key from mailjet website
EMAIL_HOST_PASSWORD = '1137525cb9f4b769663ecc2258384cd0'  # secret key
