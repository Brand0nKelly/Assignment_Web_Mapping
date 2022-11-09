"""
ASGI config for lab200 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from whitenoise import WhiteNoise
from django.core.asgi import get_asgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lab200.settings')

application = get_asgi_application()
application = WhiteNoise(application)



