import os
import sys

from django.template import Context
import django.template.loader

CWD = os.getcwd()
sys.path.append(CWD)

if os.path.exists(os.path.join(CWD, 'django_settings.py')):
    django_settings_module = 'django_settings'
    print("found custom django settings...")
else:
    django_settings_module = 'shoot.django_settings'
    print('no custom django settings found, using defaults..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", django_settings_module)

config = {}

try:
    import shootconfig
    print("Custom context found...")
    config['context'] = Context(shootconfig.context)
except ImportError:
    print("No custom context found, using defaults...")
    config['context'] = Context()
