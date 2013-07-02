import os


DEBUG = True
TEMPLATE_DEBUG = True
TEMPLATE_DIRS = (os.getcwd(),)
SECRET_KEY = "not-so-secret"
STATIC_URL = "/static/"
INSTALLED_APPS = ('django.contrib.staticfiles',)
