from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test_db',
    }
}

DEBUG = True
SECRET_KEY = "WE_DON'T_CARE"
ALLOWED_HOSTS = ["localhost"]
