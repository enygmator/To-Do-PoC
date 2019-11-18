from .Models import ToDoData
import os

DatabaseInOperation = False

def ImportToDoData(CurrentDir,rfile,contentLength):
    with open(os.path.join(CurrentDir,'Models/Temp.db'),mode='wb') as file: # b is important -> binary
        file.seek(0)
        file.truncate()
        file.write(rfile.read(contentLength))
        if ToDoData.InitTodoFrame():
            global DatabaseInOperation
            DatabaseInOperation = True
            return "The Database was imported successfully"
        else:
            return "There was an error importing the database"

def NewToDoDatabase(CurrentDir):
    ToDoFileData = None
    with open(os.path.join(CurrentDir,'Models/ToDo.db'), mode='rb') as ToDofile: # b is important -> binary
        ToDoFileData = ToDofile.read()
    with open(os.path.join(CurrentDir,'Models/Temp.db'),mode='wb') as Tempfile: # b is important -> binary
        Tempfile.seek(0)
        Tempfile.truncate()
        Tempfile.write(ToDoFileData)
    if ToDoData.InitTodoFrame():
        global DatabaseInOperation
        DatabaseInOperation = True
        return "New Todo database created successfully"
    else:
        return "There was an error in creating the database"

def GetListDataAsString():
    fileContent = ""
    for x in ToDoData.TF.todoList:
        if x[2] == 31 or x[2] == 30:
            continue
        if x[2] == 2:
            fileContent+="DBG:"+str(x[1])
        else:
            fileContent+="DBI:"+"DBP:"+str(x[0])+"DBP:"+str(x[1])+"DBP:"+str(x[2])+"DBP:"+str(x[3])
    return fileContent

def AddItemToList(Data):
    try:
        group = int(str(Data).split('ITEM:')[0].split('DBG:')[1])
        grpStartNO = 1 #temporary assignment
        grp = 0
        for i in ToDoData.TF.todoList:
            if int(i[2])==2:
                grp+=1
            if grp == group:
                ToDoData.TF.todoList.insert(i[0]+1,[0,str(Data).split('ITEM:')[1],0,grp-1]) #the 0 in the list is arbitrary
                break
        for i in range(len(ToDoData.TF.todoList)):
            ToDoData.TF.todoList[i][0] = i
        return "True"
    except:
        return "False"

def DeleteItem(Data):
    try:
        ToDoData.TF.todoList.pop(int(str(Data).split('DBI:')[1]))
        for i in range(len(ToDoData.TF.todoList)):
            ToDoData.TF.todoList[i][0] = i
        return "True"
    except:
        return "False"

def EditItem(Data):
    try:
        tempVar = str(Data).split('DBI:')[1].split('EDIT:')
        ToDoData.TF.todoList[int(tempVar[0])][1] = str(tempVar[1])
        return "True"
    except:
        return "False"

def DoneOrUndone(Data):
    try:
        tempVar = str(Data).split('DBI:')[1].split('DONE:')
        ToDoData.TF.todoList[int(tempVar[0])][2] = int(tempVar[1])
        return "True"
    except:
        return "False"

def EditListName(Data):
    try:
        group = int(str(Data).split('EDIT:')[0])
        grpStartNO = 1 #temporary assignment
        grp = 0
        for i in ToDoData.TF.todoList:
            if int(i[2])==2:
                grp+=1
            if grp == group:
                i[1] = (str(Data).split('EDIT:')[1]) #the 0 in the list is arbitrary
                break
        return "True"
    except:
        return "False"

def DeleteList(Data):
    try:
        delete = int(Data)-1
        for i in ToDoData.TF.todoList:
            if int(i[3])==delete:
                start = i[0]
                break
        while True:
            if ToDoData.TF.todoList[start][3]!=delete:
                break
            ToDoData.TF.todoList.pop(start)
        for i in range(len(ToDoData.TF.todoList)):
            ToDoData.TF.todoList[i][0] = i
        grp = -1
        for i in range(1,len(ToDoData.TF.todoList)-1):
            if ToDoData.TF.todoList[i][2]==2:
                grp+=1
            ToDoData.TF.todoList[i][3] = grp
        return "True"
    except:
        return "False"

def AddList(Data):
    try:
        grp = -1
        for i in ToDoData.TF.todoList:
            if int(i[2])==2:
                grp+=1
        ToDoData.TF.todoList.insert(len(ToDoData.TF.todoList)-1,[0,str(Data),2,grp+1])
        for i in range(len(ToDoData.TF.todoList)):
            ToDoData.TF.todoList[i][0] = i
        return "True"
    except:
        return "False"

def DispToDoDataFrame():
    print("~~~~~~~~~~~~~~~~~~~~~~~~")
    for x in ToDoData.TF.todoList:
        print(x)
    print("~~~~~~~~~~~~~~~~~~~~~~~~")

def DestroyToDoDBFrame(CurrentDir):
    try:
        with open(os.path.join(CurrentDir,'Models/Temp.db'),mode='wb') as file: # b is important -> binary
            file.seek(0)
            file.truncate()
        global DatabaseInOperation
        if DatabaseInOperation:
            ToDoData.CloseToDoFrame()
            DatabaseInOperation = False
        return "True"
    except:
        return "False"

def Shutdown(CurrentDir):
    with open(os.path.join(CurrentDir,'Models/Temp.db'),mode='wb') as file: # b is important -> binary
        file.seek(0)
        file.truncate()
    global DatabaseInOperation
    if DatabaseInOperation:
        ToDoData.CloseToDoFrame()
        DatabaseInOperation = False
    return "Cleared Trash."

def WriteToTempDB():
    #sqldba.dbCursor.execute("INSERT INTO TODO VALUES(1, '{Task}', {Listno})".format(Task = TaskName,Listno = Listno))
    ToDoData.ExecuteCommandOnToDoDB('DROP TABLE TODO')
    ToDoData.ExecuteCommandOnToDoDB('''CREATE TABLE TODO (ID INT PRIMARY KEY NOT NULL,
    TASK TEXT NOT NULL, DONE INT NOT NULL, LISTNO INT NOT NULL);''')
    for i in ToDoData.TF.todoList:
        ToDoData.ExecuteCommandOnToDoDB("INSERT INTO TODO VALUES({id}, '{Task}',{Done}, {Listno})"\
            .format(id = i[0],Task = i[1],Done = i[2],Listno = i[3]))
    print("~Data successfully written from python list to Temp.db")