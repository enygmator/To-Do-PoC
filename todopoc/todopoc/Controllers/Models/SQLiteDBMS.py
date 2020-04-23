import sqlite3
from pathlib import Path
import os

CurrentDir = Path(os.path.dirname(__file__))
sqldba = None

class sqldb:
    '''This is the main SQLite DBMS class'''
    __tododb = None
    dbCursor = None
    def InitiateConnection(self):
        self.__tododb = sqlite3.connect(os.path.join(CurrentDir,'Temp.db'))
        print("~Connected to the ToDo database successfully")
        self.dbCursor = self.__tododb.cursor()
    def Commit(self):
        self.__tododb.commit()
    def CloseConnection(self):
        self.__tododb.close()
        __tododb = None
        dbCursor = None

#MAIN EXECUTION
def InitToDoDB():
    global sqldba
    sqldba = sqldb()
    sqldba.InitiateConnection()
    sqldba.dbCursor.execute('''CREATE TABLE if not exists TODO (ID INT PRIMARY KEY NOT NULL, TASK TEXT NOT NULL, DONE INT NOT NULL, LISTNO INT NOT NULL);''')
    print("Todo table creation attempted, If not exists")
    sqldba.Commit()

def ExecuteCommandOnToDoDB(command):
    #print('~Command requested: ', str(command))
    sqldba.dbCursor.execute(command)
    sqldba.Commit()
    return sqldba.dbCursor.fetchall()

def CloseToDoDB():
    print("~ToDoDB in sqlite3 has been closed")
    sqldba.CloseConnection()

#DEVELOPMENT CODE (DISABLE DURING PRODUCTION)