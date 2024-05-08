import os
from .common import *

DEBUG = False

SECRET_KEY = os.environ["SECRET_KEY"]

koyeb_host = os.environ["DJANGO_ALLOWED_HOSTS"]

ALLOWED_HOSTS = [koyeb_host]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "storefront",
        "USER": os.environ["DB_USER"],
        "PASSWORD": os.environ["DB_PASSWORD"],
        "HOST": "ep-crimson-wind-a42v1138.us-east-1.pg.koyeb.app",
        "OPTIONS": {"sslmode": "require"},
    }
}
