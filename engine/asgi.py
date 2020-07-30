"""
ASGI config for engine project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from dotenv import load_dotenv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'engine.settings')

# Initialize .env file
project_folder = os.path.expanduser("./")
load_dotenv(os.path.join(project_folder, ".env"))

application = get_asgi_application()
