import sys

from ._base import *  # pylint: disable=wildcard-import,unused-wildcard-import

SECRET_KEY = env('SECRET_KEY', default='test')
DEBUG = env.bool('DEBUG', default=True)
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('POSTGRES_DB'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('POSTGRES_HOST'),
        'PORT': env('POSTGRES_PORT'),
    }
}

if 'test' in sys.argv:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME_TEST', default=""),
        'USER': env('DB_USER_TEST', default=""),
        'PASSWORD': env('DB_PASS_TEST', default=""),
        'HOST': env('DB_SERVICE_TEST', default=""),
        'PORT': env('DB_PORT_TEST', default=""),
    }

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST', default="")
EMAIL_USE_TLS = env('EMAIL_USE_TLS', default="")
EMAIL_PORT = env('EMAIL_PORT', default="")
EMAIL_HOST_USER = env('EMAIL_HOST_USER', default="")
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', default="")
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL', default="")
