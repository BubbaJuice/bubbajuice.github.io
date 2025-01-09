import os
import posixpath
import urllib
from http.server import HTTPServer, SimpleHTTPRequestHandler

# modify this to add additional routes
ROUTES = (
    # (url_prefix, directory_path)
    ('/', '.')
)

class RequestHandler(SimpleHTTPRequestHandler):

    def translate_path(self, path):
        """Translate path given routes"""

        # set default root to cwd
        root = os.getcwd()

        # look up routes and set root directory accordingly
        for route in ROUTES:
            if len(route) == 1:  # If only one element is present in the tuple
                pattern = route[0]
                rootdir = '.'
            else:
                pattern, rootdir = route

            if path.startswith(pattern):
                # found match!
                path = path[len(pattern):]  # consume path up to pattern len
                root = rootdir
                break

        # normalize path and prepend root directory
        path = path.split('?', 1)[0]
        path = path.split('#', 1)[0]
        path = posixpath.normpath(urllib.parse.unquote(path))

        # If path does not have an extension, append .html
        if not os.path.splitext(path)[1]:
            path += ".html"

        return os.path.join(root, path)

    def do_GET(self):
        """Serve a GET request."""
        # Redirect root URL to /index
        if self.path == '/':
            self.send_response(301)
            self.send_header('Location', '/index')
            self.end_headers()
            return

        # Redirect if path ends with a slash but it's not a directory
        if self.path.endswith('/') and not os.path.isdir(self.translate_path(self.path)):
            self.send_response(301)
            self.send_header('Location', self.path.rstrip('/'))
            self.end_headers()
            return

        # Serve files as usual
        try:
            return SimpleHTTPRequestHandler.do_GET(self)
        except Exception as e:
            self.send_error(404, "File not found")
            self.path = '/404.html'
            return SimpleHTTPRequestHandler.do_GET(self)

    def send_error(self, code, message=None):
        """Override send_error to serve custom 404 page."""
        if code == 404:
            self.path = '/404.html'
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open(self.translate_path(self.path), 'rb') as file:
                self.wfile.write(file.read())
        else:
            super().send_error(code, message)

if __name__ == '__main__':
    myServer = HTTPServer(('0.0.0.0', 8000), RequestHandler)
    print("Ready to begin serving files.")
    try:
        myServer.serve_forever()
    except KeyboardInterrupt:
        pass

    myServer.server_close()
    print("Exiting.")