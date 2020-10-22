#!/usr/bin/env python3

from http.server import HTTPServer, BaseHTTPRequestHandler
import requests


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path:
            url = self.path[1:]
            response = requests.get(f'http://{url}', headers=self.headers, payload={})
            self.send_response(200)
            self.end_headers()
            self.wfile.write(response.text.encode('utf8'))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'No URL Entered')


if __name__ == '__main__':
    httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
    httpd.serve_forever()
