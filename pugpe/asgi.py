"""
ASGI config for pugpe project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""
import os

from django.core.asgi import get_asgi_application


DJANGO_ENV = os.environ.get("DJANGO_ENV", "develop")


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pugpe.settings." + DJANGO_ENV)

application = get_asgi_application()
