import sqlite3
from pathlib import Path
import os

CurrentDir = Path(os.path.dirname(__file__))
sqldba = None

class sqldb:
    '''This is the main SQLite DBMS class'''
    tododb = None
    dbCursor = None
    validity = False
    def InitiateConnection(self):
        self.tododb = sqlite3.connect(os.path.join(CurrentDir,'Temp.db'))
        print("Connected to the ToDo database successfully")
        self.dbCursor = self.tododb.cursor()
    def CloseConnection(self):
        self.tododb.close()

#MAIN EXECUTION
def InitToDoDB():
    sqldba = sqldb()
    sqldba.InitiateConnection()
    #MAKE THIS ALRIGHT!!!!!!!
    sqldba.dbCursor.execute('''CREATE TABLE if not exists TODO (ID INT PRIMARY KEY NOT NULL, TASK TEXT NOT NULL, DONE INT NOT NULL);''')
    print("Todo table creation attempted, If not exists")
    sqldba.dbCursor.execute('SELECT * FROM TODO')
    rows = sqldba.dbCursor.fetchall()
    for row in rows:
        todoList.append(row)
        if todoList[0][3]==1:
            validity = True


#DEVELOPMENT CODE (DISABLE DURING PRODUCTION)