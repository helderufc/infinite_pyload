from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class H(BaseHTTPRequestHandler):
    def do_GET(self):
        data = json.dumps({'x': 'CRASH'*10_000_000})
        self.send_response(200)
        self.send_header('Content-Type','application/json')
        self.end_headers()
        self.wfile.write(data.encode())

HTTPServer(('0.0.0.0',8888), H).serve_forever()