
from http.server import HTTPServer, CGIHTTPRequestHandler,SimpleHTTPRequestHandler

port = 8080

httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
print("Starting simple_httpd on port: " + str(httpd.server_port))
httpd.serve_forever()

