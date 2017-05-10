import BaseHTTPServer
from enum import Enum

class RequestType(Enum):
  PYTHON = 1
  JAVA = 2

class HttpHandler(BaseHTTPServer.BaseHTTPRequestHandler):
  #def __init__(self):
	
	def do_SEND_HEADERS(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
    
  def do_GET(self):
    print("Received GET request for: %s" % (self.path,))
		do_SEND_HEADERS()
		
  def do_POST(self):
    print("Received POST request for: %s" % (self.path,))
		do_SEND_HEADERS()

if __name__ = '__main__':
  serverClass = BaseHTTPServer.HTTPServer
  httpd = serverClass(('127.0.0.1', 80), HttpHandler)
  httpd.server_forever()