import io
from django.template import Context, Template
import django.template.loader


def gen_response_stream(f):
    context = Context()
    template = Template(f.read())
    content = template.render(context)
    content_in_bytes = bytes(content, 'UTF-8')
    stream = io.BytesIO(content_in_bytes)
    return (stream, len(content_in_bytes))
