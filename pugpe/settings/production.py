import os

import dj_database_url
from decouple import config

from .base import *  # noqa


INSTALLED_APPS = [app for app in INSTALLED_APPS if app not in DEV_APPS]

ALLOWED_HOSTS = ["*"]

DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# STATICS
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "/static/"

# STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# DATABASE
DATABASES = {"default": dj_database_url.config(default=config("DATABASE_URL"))}
