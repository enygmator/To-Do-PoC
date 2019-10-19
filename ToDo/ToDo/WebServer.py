#This is an example code to test th eoython module packaging.
#once the module packaging part is completed, I will branch off this commit.
#DOCS FOR THE CODE IN THIS PAGE ARE AT: https://docs.python.org/3/library/http.server.html

#import statements
from http.server import *
import os

#Variables
PORT = 8182
CurrentDir = os.path.dirname(__file__)

#Classes
class WebServer(BaseHTTPRequestHandler):
    #This class inherits the BaseHTTPRequestHandler class to implement custom code for web page requests
    def do_GET(self):
        print("Request:", self.path)
        #self refers to the class in which we are curerently. thus path is a variable of THIS class
        if self.path == '/' or self.path=='':
            self.path = 'wwwRoot\index.html'
        try:
            #Reading the file (index.html)
            file_to_open = open(os.path.join(CurrentDir,self.path)).read()
            self.send_response(200)
            self.send_header('Content-type','text/html')
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))
        return

#MAIN Execuion
def Start():
    httpd = HTTPServer(('localhost', PORT), WebServer)
    print("\n~The server, ",httpd.server_name," is Destined to run at: ",httpd.server_address," : ",httpd.server_port)
    print("~To shutdown the web sever use the keyboard interrupt (Ctrl + C)")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt: #this is the ctrl + C interrupt
    	print('~STOP Command received, shutting down the web server')
    	httpd.socket.close()
    except: #This is the deafualt exception, i.e. not specific to a particular "error", thus it must be at last
        print("~There was an error in running the server")

#DEVELOPMENT CODE (DISABLE DURING PRODUCTION)
#Start()