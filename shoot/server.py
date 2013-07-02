import os
import posixpath
import http.server

from shoot.util import gen_response_stream


class ShootServer(http.server.SimpleHTTPRequestHandler):
    """Handler to deal with incoming requests.
    """

    def send_head(self):
        """Builds response headers and in process renders templates, if any.

        This method overrides SimpleHTTPRequestHandlet.send_head()
        with minor modifications
        """
        path = self.translate_path(self.path)
        f = None
        if os.path.isdir(path):
            if not self.path.endswith('/'):
                # redirect browser - doing basically what apache does
                self.send_response(301)
                self.send_header("Location", self.path + "/")
                self.end_headers()
                return None
            for index in "index.html", "index.htm":
                index = os.path.join(path, index)
                if os.path.exists(index):
                    path = index
                    break
            else:
                return self.list_directory(path)
        ctype = self.guess_type(path)
        try:
            f = open(path, 'rb')
        except IOError:
            self.send_error(404, "File not found")
            return None
        file_ext = posixpath.splitext(path)[1]
        if file_ext == '.html':
            stream, length = gen_response_stream(f)
        self.send_response(200)
        self.send_header("Content-type", ctype)
        self.send_header("Content-Length", str(length))
        self.send_header("Last-Modified", self.date_time_string(
            os.fstat(f.fileno()).st_mtime))
        self.end_headers()
        if file_ext == '.html':
            return stream
        return f
