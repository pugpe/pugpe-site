"""
WSGI config for pugpe project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""
import os

from django.core.wsgi import get_wsgi_application


DJANGO_ENV = os.environ.get("DJANGO_ENV", "develop")


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pugpe.settings." + DJANGO_ENV)

application = get_wsgi_application()
