from http.server import BaseHTTPRequestHandler, HTTPServer
import json, configparser

config = configparser.ConfigParser()

config.read('feinstaub.conf')

class PayloadHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        payload = json.loads(post_data)

        for entry in payload['sensordatavalues']:
            print(entry['value_type'])

        self.send_response(200)     #positiven http response senden
        self.end_headers()


def run_http(server_class=HTTPServer, handler_class=PayloadHandler):  #Lässt den http server Laufen
    server_address = ('', int(config['http']['port']))
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

run_http()