from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import csv

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            html = '<h1>Hello, World!</h1>'
            self.wfile.write(html.encode())
        elif self.path == '/xml':
            self.send_response(200)
            self.send_header('Content-type', 'application/xml')
            self.end_headers()
            xml = '<?xml version="1.0" encoding="UTF-8"?><data>Hello, World!</data>'
            self.wfile.write(xml.encode())
        elif self.path == '/json':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {'message': 'Hello, World!'}
            json_data = json.dumps(data)
            self.wfile.write(json_data.encode())
        elif self.path == '/csv':
            self.send_response(200)
            self.send_header('Content-type', 'text/csv')
            self.end_headers()
            csv_data = 'Name,Email\nJohn Doe,john@example.com'
            self.wfile.write(csv_data.encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'404 Not Found')

def run():
    address = ('', 8000)
    httpd = HTTPServer(address, SimpleHTTPRequestHandler)
    print('Starting server...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
