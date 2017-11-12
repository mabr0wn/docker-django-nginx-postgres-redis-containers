"""
WSGI config for web project.

It exposes the WSGI callable as a module-level variable named ``application``,

for more information on this filem see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_docker.settings")

application = get_wsgi_application()
