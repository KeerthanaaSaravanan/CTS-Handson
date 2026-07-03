"""
WSGI config for coursemanager project.

It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
WSGI.PY PURPOSE:
This file contains the WSGI (Web Server Gateway Interface) application object
used by Django to interface with web servers like Gunicorn or uWSGI for
deploying the application in production.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coursemanager.settings')

application = get_wsgi_application()