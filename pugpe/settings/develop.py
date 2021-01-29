import os

from .base import *  # noqa


DEBUG = True

ALLOWED_HOSTS = ["*"]

MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware")

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "/static/"

INTERNAL_IPS = [
    "127.0.0.1",
]
