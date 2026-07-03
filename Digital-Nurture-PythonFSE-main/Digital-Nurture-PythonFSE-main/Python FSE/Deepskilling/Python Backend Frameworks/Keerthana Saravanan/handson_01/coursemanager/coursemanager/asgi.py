"""
ASGI config for coursemanager project.

It exposes the ASGI callable as a module-level variable named ``.
For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
ASGI.PY PURPOSE:
This file contains the ASGI (Asynchronous Server Gateway Interface) application
object used by Django to interface with async-capable web servers like Daphne or
Uvicorn for deploying the application with async support.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coursemanager.settings')

application = get_asgi_application()
