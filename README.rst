Shoot
=====

Kick-start your prototype with Django templates


What is it?
-----------

If you want to start prototyping your web app using Django templates,
without needing to setup a complete Django project, *Shoot* does that for you.



Usage
-----

You will need Pip with Python3.

On Ubuntu::

    $ sudo apt-get install python3-setuptools
    $ sudo pip3 install shoot
    $ shoot



Custom Config
-------------


If the file *shootconfig.py* is present in the dir *shoot* is launched from, with contents::

    context = {}

*shoot* will pass this dictionary to Context objects used in rendering templates


If the file *django_settings.py* is present in the dir *shoot* is launched from, *shoot*
will use it as the DJANGO_SETTINGS_MODULE. This file *must* contain the following variables::

    DEBUG = True
    TEMPLATE_DEBUG = True
    TEMPLATE_DIRS = (os.getcwd(),)
    SECRET_KEY = "not-so-secret"
    STATIC_URL = "/static/"
    INSTALLED_APPS = ('django.contrib.staticfiles',)
