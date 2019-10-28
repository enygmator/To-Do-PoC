#DOCS FOR THE CODE IN THIS PAGE ARE AT: https://docs.python.org/3/library/http.server.html

#import statements
from http.server import *
import os
from pathlib import Path

#Variables
PORT = 8182
CurrentDir = Path(os.path.dirname(__file__))
TempDB = None

#Classes
class WebServer(BaseHTTPRequestHandler):
    #This class inherits the BaseHTTPRequestHandler class to implement custom code for web page requests
    def do_GET(self):
        print("Request:", self.path)
        #self refers to the class in which we are curerently. thus path is a variable of THIS class
        #region HTML
        if 'html' in str(self.path) or str(self.path) == '/':
            try:
                if str(self.path).endswith('/'):
                    file_to_open = open(os.path.join(CurrentDir.parent,'Views\wwwRoot\index.html')).read()
                else:
                    file_to_open = open(os.path.join(CurrentDir.parent,"Views\wwwRoot", str(self.path).split('/')[-1])).read()
                self.send_response(200)
                self.send_header('Content-type','text/html')
            except:
                file_to_open = "File not found"
                self.send_response(404)
            self.end_headers()
            self.wfile.write(bytes(file_to_open, 'utf-8'))
        #endregion
        #region JS
        if '/JS' in self.path:
            try:
                file_to_open = open(os.path.join(CurrentDir.parent,"Views\wwwRoot\JS", str(self.path).split('/')[-1])).read()
                self.send_response(200)
                self.send_header('Content-type','application/javascript')
            except:
                file_to_open = "File not found"
                self.send_response(404)
            self.end_headers()
            self.wfile.write(bytes(file_to_open, 'utf-8'))
        #endregion
        #region CSS
        if '/CSS' in self.path:
            try:
                file_to_open = open(os.path.join(CurrentDir.parent,"Views\wwwRoot\CSS", str(self.path).split('/')[-1])).read()
                self.send_response(200)
                self.send_header('Content-type','text/css')
            except:
                file_to_open = "File not found"
                self.send_response(404)
            self.end_headers()
            self.wfile.write(bytes(file_to_open, 'utf-8'))
        #endregion
        if self.path.endswith("Temp.db"):
            self.path = 'Models\Temp.db'
            try:
                with open(os.path.join(CurrentDir.parent,self.path), mode='rb') as file: # b is important -> binary
                    fileContent = file.read()
                self.send_response(200)
                self.send_header('Content-type','application/octet-stream')
            except:
                fileContent = "File not found"
                self.send_response(404)
            self.end_headers()
            self.wfile.write(fileContent)
        return

    def do_POST(self):
        contentLength = int(self.headers['Content-Length']) # <--- Gets the size of data
        Data = self.rfile.read(contentLength) # <--- Gets the data itself
        if str(self.rfile.) == "NewToDoDatabase": ###THere is a problem here
            ToDoFileData = None
            with open(os.path.join(CurrentDir.parent,'Models\ToDo.db'), mode='rb') as ToDofile: # b is important -> binary
                ToDoFileData = ToDofile.read()
            with open(os.path.join(CurrentDir.parent,'Models\Temp.db'),mode='wb') as Tempfile: # b is important -> binary
                Tempfile.seek(0)
                Tempfile.truncate()
                Tempfile.write(ToDoFileData)
                print("New Todo database created successfully")
        if str(self.headers()).endswith("Temp.db"):
            with open(os.path.join(CurrentDir.parent,'Models\Temp.db'),mode='wb') as file: # b is important -> binary
                file.seek(0)
                file.truncate()
                file.write(Data)
            self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

#MAIN Execuion
def Start():
    with open(os.path.join(CurrentDir.parent,'Models\Temp.db'),mode='wb') as file: # b is important -> binary
        file.seek(0)
        file.truncate()
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
if __name__ == "__main__":
    Start()