"""
WSGI config for lab200 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import sys

from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application


# path = "/Users/brandon/PycharmProjects/lab200/lab200"
# if path not in sys.path:
#   sys.path.insert(0, path)

# os.environ["DJANGO_SETTINGS_MODULE"] = "lab200.settings"
# /Users/brandon/.conda/envs/lab200/lib/python3.10/site-packages
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lab200.settings')

application = get_wsgi_application()
application = WhiteNoise(application)
