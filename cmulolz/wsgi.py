import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "cmulolz.settings.development")

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

application = Cling(get_wsgi_application())
