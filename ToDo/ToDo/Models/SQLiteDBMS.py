import sqlite3
from pathlib import Path
import os

CurrentDir = Path(os.path.dirname(__file__))

class sqldb:
    '''This is the main SQLite DBMS class'''
    tododb = None
    dbCursor = None
    def InitiateConnection(self):
        self.tododb = sqlite3.connect(os.path.join(CurrentDir,'Temp.db'))
        print("Connected to the ToDo database successfully")
        self.existing = True
        self.dbCursor = self.tododb.cursor()
    def CloseConnection(self):
        self.tododb.close()

#MAIN EXECUTION
def Test():
    sqldba = sqldb()
    sqldba.InitiateConnection()
    sqldba.dbCursor.execute('''CREATE TABLE if not exists TODO (ID INT PRIMARY KEY NOT NULL, TASK TEXT NOT NULL, DONE INT NOT NULL);''')
    #print("Table created successfully")
    #sqldba.dbCursor.execute("INSERT INTO TODO VALUES(1, 'new task', 1)")
    #sqldba.tododb.commit()
    sqldba.dbCursor.execute('SELECT * FROM TODO')
    rows = sqldba.dbCursor.fetchall()
    for row in rows:
        print(row)
    sqldba.CloseConnection()

#DEVELOPMENT CODE (DISABLE DURING PRODUCTION)
Test()