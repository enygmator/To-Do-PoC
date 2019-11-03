#DOCS FOR THE CODE IN THIS PAGE ARE AT: https://docs.python.org/3/library/http.server.html

#import statements
if __name__ == "__main__":    
    import MasterControl
else:
    from . import MasterControl

from sys import exit as ExitProgram
from http.server import *
import os
from pathlib import Path

#Variables
httpd = None
PORT = 8182
CurrentDir = Path(os.path.dirname(__file__))

#Classes
class WebServer(BaseHTTPRequestHandler):
    #This class inherits the BaseHTTPRequestHandler class to implement custom code for web page requests
    def do_GET(self):
        #self refers to the class in which we are curerently. thus path is a variable of THIS class
        #region HTML
        if 'html' in self.path or self.path == '/':
            try:
                if self.path == '/':
                    if (MasterControl.DatabaseInOperation==True):
                        file_to_open = "The database is already initiated. Go To <a href=\"/ToDo.html\">\
                            ToDo App Page</a> to manage your todo lists, or to Destroy existing database and start afresh."
                    else:
                        file_to_open = open(os.path.join(CurrentDir.parent,'Views\wwwRoot\index.html')).read()
                else:
                    if self.path.endswith('/'):
                        self.path = self.path[:-1]
                    if 'ToDo.html' in self.path and (MasterControl.DatabaseInOperation==False):
                        file_to_open = "The database is not initiated. Go To <a href=\"/index.html\">Homepage</a> to solve issue."
                    elif 'index.html' in self.path and (MasterControl.DatabaseInOperation==True):
                        file_to_open = "The database is already initiated. Go To <a href=\"/ToDo.html\">\
                            ToDo App Page</a> to manage your todo lists, or to Destroy existing database and start afresh."
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
                MasterControl.WriteToTempDB()
                with open(os.path.join(CurrentDir,self.path), mode='rb') as file: # b is important -> binary
                    fileContent = file.read()
                self.send_response(200)
                self.send_header('Content-type','application/octet-stream')
            except:
                fileContent = "File not found"
                self.send_response(404)
            self.end_headers()
            self.wfile.write(fileContent)
        if self.path.endswith("ListData"):
            try:
                fileContent = MasterControl.GetListDataAsString()
                self.send_response(200)
            except:
                fileContent = "Somethings is wrong. Sorry!"
                self.send_response(404)
            self.end_headers()
            self.wfile.write(bytes(fileContent,'utf-8'))
        return

    def do_POST(self):
        responseText = "Ignore this message!"
        contentLength = int(self.headers['Content-Length']) # <-- Gets the size of data
        #Data = self.rfile.read(contentLength).decode('utf-8') # <-- Gets the data itself
        if self.path.endswith("NewToDoDataBase"):
            responseText = MasterControl.NewToDoDatabase(CurrentDir)
            print(responseText)
        if self.path.endswith("Temp.db"):
            responseText = MasterControl.ImportToDoData(CurrentDir, self.rfile, contentLength)
        if self.path.endswith("Edit"):
            Data = self.rfile.read(contentLength).decode('utf-8')
            print("~Request string: "+Data)
            responseText = MasterControl.EditItem(Data)
        if self.path.endswith("Delete"):
            Data = self.rfile.read(contentLength).decode('utf-8')
            print("~Request string: "+Data)
            responseText = MasterControl.DeleteItem(Data)
        if self.path.endswith("Done"):
            Data = self.rfile.read(contentLength).decode('utf-8')
            print("~Request string: "+Data)
            responseText = MasterControl.DoneOrUndone(Data)
        if self.path.endswith("Add"):
            Data = self.rfile.read(contentLength).decode('utf-8')
            print("~Request string: "+Data)
            responseText = MasterControl.AddItemToList(Data)
        if self.path.endswith("EditListName"):
            Data = self.rfile.read(contentLength).decode('utf-8')
            print("~Request string: "+Data)
            responseText = MasterControl.EditListName(Data)
        if self.path.endswith("DeleteList"):
            Data = self.rfile.read(contentLength).decode('utf-8')
            print("~Request string: "+Data)
            responseText = MasterControl.DeleteList(Data)
        if self.path.endswith("AddList"):
            Data = self.rfile.read(contentLength).decode('utf-8')
            print("~Request string: "+Data)
            responseText = MasterControl.AddList(Data)
        if self.path.endswith("DestroyToDoDBFrame"):
            responseText = MasterControl.DestroyToDoDBFrame(CurrentDir)
        if self.path.endswith("ShutDownServer"):
            print("Shutdown command received from webpage")
            ExitProgram()
        if self.path.endswith("DispToDoDataFrame"):
            MasterControl.DispToDoDataFrame()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes(responseText,'utf-8'))

#MAIN Execuion
def Start():
    global httpd
    httpd = HTTPServer(('localhost', PORT), WebServer)
    print("\n~The server, ",httpd.server_name," is Destined to run at: ",httpd.server_address," : ",httpd.server_port)
    print("~To shutdown the web sever use the keyboard interrupt (Ctrl + C)")
    try:
        httpd.serve_forever()
    except (KeyboardInterrupt,SystemExit): #this is the ctrl + C interrupt
    	print('~STOP Command received.',MasterControl.Shutdown(CurrentDir), "Shutting down the web server.")
    	httpd.socket.close()
    except: #This is the deafualt exception, i.e. not specific to a particular "error", thus it must be at last
        print("~There was an error in running the server")

#DEVELOPMENT CODE (DISABLE DURING PRODUCTION)
if __name__ == "__main__":
    Start()