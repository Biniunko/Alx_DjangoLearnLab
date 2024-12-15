"""
WSGI config for social_media_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_media_api.settings')

application = get_wsgi_application()
import sys
import os

# Add your project directory to the sys.path
project_home = '/home/yourusername/yourproject'
if project_home not in sys.path:
    sys.path.append(project_home)

os.environ['DJANGO_SETTINGS_MODULE'] = 'yourproject.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()