import os
import sys
# put the Django project on sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(1, os.path.abspath("data/vhost/muralist/releases/current/muralist")))
os.environ["DJANGO_SETTINGS_MODULE"] = "muralist.settings"
from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()