from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1ik70l(p7ylwj0^$aj1$aa*95b6y%-0_%ds-&u*1o0=o9rg1#6'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS = INSTALLED_APPS +[
    'debug_toolbar'
]
MIDDLEWARE = MIDDLEWARE +[

    'debug_toolbar.middleware.DebugToolbarMiddleware',

]
try:
    from .local import *
except ImportError:
    pass

INTERNAL_IPS=["127.0.0.1"]