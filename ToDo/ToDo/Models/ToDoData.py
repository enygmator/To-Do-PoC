from SQLiteDBMS import *
TF = None

#CLASSES
class TodoFrame:
    '''Implements the todo frame'''
    todolist = None

    def InitTodoFrame():
        todoList = []
        sqldba.ini
        sqldba.dbCursor.execute('SELECT * FROM TODO')
        rows = sqldba.dbCursor.fetchall()
        for row in rows:
            todoList.append(row)
        del todoList[0]
    sqldba.CloseConnection()
    def InsertTaskIntoDB(TaskName,Listno):
        sqldba.dbCursor.execute("INSERT INTO TODO VALUES(1, '{Task}', {Listno})".format(Task = TaskName,Listno = Listno))
        sqldba.tododb.commit()

#MAIN EXECUTION
def InitTodoFrame():
    global.TF = TodoFrame()
    global.TF.InitTodoFrame()
