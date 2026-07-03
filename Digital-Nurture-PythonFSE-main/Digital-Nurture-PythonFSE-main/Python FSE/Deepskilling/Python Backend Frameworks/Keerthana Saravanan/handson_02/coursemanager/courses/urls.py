from django.urls import path
from .views import hello_view

urlpatterns = [
    path("hello/", hello_view, name="hello"),
]

# COURSES/URLS.PY PURPOSE:
# This file contains URL patterns specific to the courses app.
# It maps URL paths to views within this app, enabling modular URL configuration.

# DJANGO PROJECT VS DJANGO APP
# ----------------------------
# Django Project:
#   - A project is the entire application and its configuration
#   - Contains settings, URLs, WSGI/ASGI config, and other project-level configurations
#   - One project can contain multiple apps
#   - Example: 'coursemanager' is our Django project
#
# Django App:
#   - An app is a self-contained module designed to do one specific thing
#   - Contains models, views, templates, URLs, tests, etc. for a specific functionality
#   - Multiple apps can be combined to create a project
#   - Example: 'courses' is a Django app that handles course management functionality
#
# Key Difference:
#   A project is the entire website/application, while an app is a modular
#   component within that project that provides specific functionality.
