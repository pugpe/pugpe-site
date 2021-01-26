import os

import dj_database_url
from decouple import config

from .base import *  # noqa


INSTALLED_APPS = [app for app in INSTALLED_APPS if app not in DEV_APPS]

ALLOWED_HOSTS = ["*"]  # TODO: Colocar hosts em variavel de ambiente

DEBUG = False

DATABASES = {
    "default": dj_database_url.config(
        default="sqlite:///{0}".format(os.path.join(BASE_DIR, "pugpe_site.sqlite3")),
    )
}


# STATICS
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "/static/"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# DATABASE
DATABASES = {"default": dj_database_url.config(default=config("DATABASE_URL"))}
