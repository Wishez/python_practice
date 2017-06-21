import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

def runserver(number):

    webdir = '.'
    port = int(number) #8888

    os.chdir(webdir)
    srvraddr = ("", port)
    srvrobj = HTTPServer(srvraddr, CGIHTTPRequestHandler)
    srvrobj.serve_forever()

runserver(input('Server number: '))