import os
import io
import http.server
from django.template import Template

from shoot import config


class ShootServer(http.server.SimpleHTTPRequestHandler):
    """Handler to deal with incoming requests.
    """

    def gen_response_stream(self, f):
        template = Template(f.read())
        content = template.render(config.get('context'))
        content_in_bytes = bytes(content, 'UTF-8')
        stream = io.BytesIO(content_in_bytes)
        return (stream, len(content_in_bytes))

    def send_head(self):
        """Builds response headers and in process renders templates, if any.

        This method overrides SimpleHTTPRequestHandlet.send_head()
        """
        path = self.translate_path(self.path)
        f = None
        to_render = False
        if os.path.isdir(path):
            if not self.path.endswith('/'):
                # redirect browser - doing basically what apache does
                self.send_response(301)
                self.send_header("Location", self.path + "/")
                self.end_headers()
                return None
        else:
            # check if URL corresponds to a template to render
            if path.endswith("/"):
                index = path[:-1]
            else:
                index = path
            for ext in '.html', '.htm':
                if os.path.exists(index + ext):
                    to_render = True
                    realpath = index + ext
                    break
        if os.path.isdir(path):
            # if dir, check for existence of index.htm*
            for index in "index.html", "index.htm":
                index = os.path.join(path, index)
                if os.path.exists(index):
                    realpath = index
                    to_render = True
                    break
            else:
                return self.list_directory(path)
        # deny if URL directly requests for *.html file, allow if dir
        file_extension = os.path.splitext(path)[1]
        if file_extension in ('.html', '.htm') and not os.path.isdir(path):
            self.send_error(404, "File not found")
            return None
        if to_render:
            path = realpath
        ctype = self.guess_type(path)
        try:
            f = open(path, 'rb')
        except IOError:
            self.send_error(404, "File not found")
            return None
        fs = os.fstat(f.fileno())
        if to_render:
            stream, length = self.gen_response_stream(f)
        else:
            length = fs[6]
        self.send_response(200)
        self.send_header("Content-type", ctype)
        self.send_header("Content-Length", str(length))
        self.send_header("Last-Modified", self.date_time_string(
            fs.st_mtime))
        self.end_headers()
        if to_render:
            return stream
        return f
