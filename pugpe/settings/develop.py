import os

from .base import *  # noqa


DEBUG = True

ALLOWED_HOSTS = ["*"]

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "/static/"

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
