from django.template import Context
import django.template.loader


config = {}


try:
    import shootconfig
    print("Custom context found...")
    config['context'] = Context(shootconfig.context)
except ImportError:
    print("No custom context found...")
    config['context'] = Context()
