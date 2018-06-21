from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import parse_qs, urlparse

class testHTTPServer_RequestHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        url=self.path
        form= parse_qs(urlparse(url).query)
        if(form != {}):
            self.process_form(form)
        super().do_GET()
        print("do_get")

    def process_form(self,form):
        if 'food' in form :
            if form['food']=='Pizza' :
                print(form['firstname'])+", go to Dominos tonight!"
            elif form['food']=='Tacos' :
                print(form['firstname'])+", go to Tacobell tonight!"
            elif form['food']=='Salad'
                print(form['firstname'])+", go to Caesar Salad tonight!"

port=8090
server_address=("",port)
httpd=HTTPServer(server_address,testHTTPServer_RequestHandler)
print("Starting simple_httpdon port: " + str(httpd.server_port))
httpd.serve_forever()