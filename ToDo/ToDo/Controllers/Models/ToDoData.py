from .SQLiteDBMS import InitToDoDB, CloseToDoDB, ExecuteCommandOnToDoDB
TF = None

#CLASSES
class TodoFrame:
    '''Implements the todo frame'''
    todoList = []

    def InitTodoFrame(self):
        InitToDoDB()
        self.todoList.clear()
        rows = ExecuteCommandOnToDoDB('SELECT * FROM TODO')        
        if rows==[]:
            return False
        else:
            for row in rows:
                self.todoList.append(list(row))
            if self.todoList[0][3]!=-3:
                self.todolist = []
                CloseToDoDB()
                return False
            else:
                return True

#MAIN EXECUTION
def InitTodoFrame():
    global TF
    TF = TodoFrame()
    return TF.InitTodoFrame()
def CloseToDoFrame():
    global TF
    TF = None
    CloseToDoDB()