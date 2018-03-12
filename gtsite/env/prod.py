from .base import *

DEBUG = False
ALLOWED_HOSTS = [".gthockey.com"]

STATIC_ROOT = "/var/www/static"
MEDIA_ROOT = "/var/www/media"

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'georgiatechhockey'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/var/www/django.log',
        }
    },
    'loggers': {
        'django': {
            'level': 'INFO',
            'handlers': ['file'],
            'propagate': True,
        }
    }
}

""" Settings required by local.py:
DATABASES
SECRET_KEY
RECAPTCHA_SECRET_KEY
EMAIL_HOST_PASSWORD
"""