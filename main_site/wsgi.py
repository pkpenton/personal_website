"""
WSGI config for main_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main_site.settings")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
application = get_wsgi_application()

# application = WhiteNoise(application, root=os.path.join(BASE_DIR, '/static/'))
# application = DjangoWhiteNoise(application)

