"""
WSGI config for ciis project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application


# If WEBSITE_HOSTNAME is defined as an environment variable, then we're running
# on Azure App Service and should use the production settings in production.py.

print("################--", os.environ)
settings_module = "settings.production" if 'WEBSITE_HOSTNAME' in os.environ else 'settings.local'

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings_local")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)


application = get_wsgi_application()

