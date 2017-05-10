import BaseHTTPServer
from enum import Enum

class RequestType(Enum):
  PYTHON = 1
  JAVA = 2

class HttpHandler(BaseHTTPServer.BaseHTTPRequestHandler):
  #def __init__(self):
    
  def do_GET(self):
    print("Received GET request for: %s" % (self.path,))

  def do_POST(self):
    print("Received POST request for: %s" % (self.path,))

class RequestTypeWrapper(isJa):

if __name__ = '__main__':
  serverClass = BaseHTTPServer.HTTPServer
  httpd = serverClass(('127.0.0.1', 80), HttpHandler)
  httpd.server_forever()