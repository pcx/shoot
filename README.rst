Shoot
=====

Kick-start your prototype with Django templates


What is it?
-----------

If you want to start prototyping your web app using Django templates,
without needing to setup a complete Django project, *Shoot* does that for you.

*Shoot* is a minimal web server which maps *.html files to URLs, i.e.
server_root/path/to.file.html is served at http://host:port/path/to/file.

HTML files are mapped to URLs and rendered as Django templates. You can use
all the usual Django template goodness, i.e. extending & including other templates,
template tags like *{% static %}* etc.

It is like developing with PHP. You can later drop these templates directly into
your Django project.

*Shoot* is known to work with Python 3.2 and Django 1.5.

Stuff *Shoot* does for you:

- Map .html files to URLs and renders them while serving
- List dirs and serve static files like any good web server would do
- Let you pass custom context while rendering templates
- Lets you pass custom Django settings module


Installation
------------

On Ubuntu:

You will need Pip with Python3::

    $ sudo apt-get install python3-setuptools
    $ sudo pip3 install shoot
    $ shoot


Using git::

    $ git clone https://github.com/pcx/shoot.git
    $ python3 shoot/setup.py install


Usage
-----

Run '*shoot*' in the directory you want to serve from.


Custom Config
-------------


If the file *shootconfig.py* is present in the dir *shoot* is launched from, with contents::

    context = {}

*shoot* will pass this dictionary to Context objects used in rendering templates. You can use this
to expose a 'user' object in templates, etc.


If the file *django_settings.py* is present in the dir *shoot* is launched from, *shoot*
will use it as the DJANGO_SETTINGS_MODULE. You can use this for setting a custom static URL, etc.
This file *must* contain the following variables::

    DEBUG = True
    TEMPLATE_DEBUG = True
    SECRET_KEY = "not-so-secret"
    # helps *shoot* find templates
    TEMPLATE_DIRS = (os.getcwd(),)
    # adds support for '*static*' template tag
    STATIC_URL = "/static/"
    INSTALLED_APPS = ('django.contrib.staticfiles',)
