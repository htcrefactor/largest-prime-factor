import socketserver
import math
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, urlsplit, parse_qs
from urllib.parse import urlparse, parse_qsl

from primality import Primality_test

primality = Primality_test()

PORT = 80

class Request_handler(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type','text/html')
    self.end_headers()

    candidate_number = int(self.path.strip("/?number="))

    initial_number = candidate_number / 2
    initial_number = math.floor(initial_number)

    message = ""
    while initial_number > 0: 
      if ((int(candidate_number)) % initial_number) == 0:
        prime = primality.isPrime(initial_number)
        if prime: 
          message += "Largest prime factor is " + str(initial_number) + "."
          
          break

        else:
          initial_number = initial_number - 1

      else: 
        initial_number = initial_number - 1

    self.wfile.write(bytes(message, "utf8"))
    return

class Server():
  def __init__(self):
    pass

  def run(self):
    with socketserver.TCPServer(("", PORT), Request_handler) as httpd:
      print("Serving at port", PORT)
      httpd.serve_forever()
