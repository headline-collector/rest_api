#!/home/wanglei/sand_box/pylab/bin/python
"""
WSGI config for RESTful_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys

root = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(0, root)
site_packages = '/home/wanglei/sand_box/pylab/lib/site-packages'
sys.path.insert(1, site_packages)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "RESTful_api.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
