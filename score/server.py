#!/usr/bin/env python

from http.server import  HTTPServer,CGIHTTPRequestHandler

import cgitb;

error=cgitb.enable()  ## This line enables CGI error reporting

server = HTTPServer
handler = CGIHTTPRequestHandler
port=8090
server_address = ("", port)
handler.cgi_directories = ["/cgi-bin"]
httpd = server(server_address, handler)
print("Starting simple_httpdon port: " + str(httpd.server_port))
print("localhost:8090 접속하기!")
httpd.serve_forever()