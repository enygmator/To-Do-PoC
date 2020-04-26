var UserInList = 1;
var ToDoDataFrame;

function PageOnLoad()
{
    RefreshList();
}

function DispToDoDataFrame()
{
    var http = new XMLHttpRequest();
    http.open('POST', '/DispToDoDataFrame', true);
    http.send();
    alert("Attempted to display ToDoDBFrame in Terminal");
}

function DispAbout()
{
    str = "Created by GROUP 10:<br>1. Moyank Giri<br>2. Vaibhava Krishna D<br>3. T Tarun Aditya (Lead developer and project manager)<br><br>";
    str+="A Python Project<br>Semester 1 of batch 2019-23<br>UE19CS102 (Introduction to computing using python Lab) - Section M<br>";
    str+="PES University, Bengaluru, Karnataka, India<br><br>";
    str+="For more details or source code click the 'Go to GitHub' button";

    $("#dialog-confirm").html(str);

    // Define the Dialog and its properties.
    $("#dialog-confirm").dialog({
        resizable: false,
        modal: true,
        title: "Modal",
        height: 400,
        width: 500,
        buttons: {
            "Go to GitHub": function () {
                $(this).dialog('close');
                var link = document.createElement('a');
                link.href = 'https://github.com/enygmator/To-Do-PoC/';
                link.setAttribute("target", "_blank");
                document.body.appendChild(link);
                link.click();
                document.body.removeChild(link);
            },
            "Close": function () {
                $(this).dialog('close');
            }
        }
    });
}

function RefreshList()
{
    var request = new XMLHttpRequest();
    request.open('GET', '/ListData', true);

    request.onload = function()
    {
        // Only handle status code 200
        if(request.status === 200)
        {
            ToDoDataFrame = String(request.response);
            if (request.response=="")
            {
                alert("It appears that no lists exist.\n So, the database will be destroyed.")
                DestroyToDoDBFrame();
                return null;
            }
            var groups = ToDoDataFrame.split("DBG:");
            var ListsOL = document.getElementById("ListsOL");
            while (ListsOL.firstChild) {
                ListsOL.removeChild(ListsOL.firstChild);
            }
            for (let j = 1; j < groups.length; j++)
            {
                var li = document.createElement('li');
                var LiButton = document.createElement('button');
                LiButton.id = 'List'+j;
                li.style.top = 48*(j-1)+'px';
                li.style.margin = 'auto';
                li.style.position = 'absolute';
                LiButton.innerHTML = groups[j].split('DBI:')[0];
                LiButton.className = "LiButton";
                LiButton.onclick = function(){ListSelectionChanged(this.innerHTML)};
                li.appendChild(LiButton);
                ListsOL.appendChild(li);
            }
            ListSelectionChanged(document.getElementById("List"+UserInList).innerHTML);
        }
        else if(request.status === 404)
        {
            alert("There was an error in obtaining the Database")
        }
        else
        {
            alert("There was an unknown error")
        }
    };
    request.send();
}

function ListSelectionChanged(text)
{
    document.getElementById('SelectedListName').innerHTML = text;
    var ItemOL = document.getElementById('ItemOL');
    while (ItemOL.firstChild) {
        ItemOL.removeChild(ItemOL.firstChild);
    }
    var groups = ToDoDataFrame.split("DBG:");
    var temp = 0
    groups.forEach(group => {
        if (group.split('DBI:')[0] == text)
        {
            UserInList = temp;
            var Items = group.split("DBI:");
            for (let k = 1; k < Items.length; k++)
            {
                var ItemDiv = document.createElement('div');
                ItemDiv.className = "ItemDiv";
                ItemDiv.style.top = 48*(k-1)+'px';
                var Properties = Items[k].split("DBP:");

                var LiTaskName = document.createElement('p');
                LiTaskName.className = "LiTaskName";

                var LiCheckBox = document.createElement('input');
                LiCheckBox.name = "DBG:"+text+"DBI:"+Properties[1];
                LiCheckBox.type = 'checkbox';
                LiCheckBox.className = "LiCheckBox";
                LiCheckBox.onchange = function(){TaskCheckOrUncheck(this)};
                if (Properties[3] == 1)
                {
                    LiCheckBox.checked = true;
                    LiTaskName.innerHTML = "<strike>"+Properties[2]+"</strike>";
                }
                else{
                    LiCheckBox.checked = false;
                    LiTaskName.innerHTML = Properties[2];
                }
                ItemDiv.appendChild(LiCheckBox);
                ItemDiv.appendChild(LiTaskName);

                var LiEditTask = document.createElement('button');
                LiEditTask.name = "DBG:"+text+"DBI:"+Properties[1];
                LiEditTask.id = Properties[2];
                LiEditTask.className = "LiEditTask";
                LiEditTask.innerHTML = "EDIT";
                LiEditTask.onclick = function(){EditTask(this)};
                ItemDiv.appendChild(LiEditTask);
                
                var LiDeleteTask = document.createElement('button');
                LiDeleteTask.name = "DBG:"+text+"DBI:"+Properties[1];
                LiDeleteTask.className = "LiDeleteTask";
                LiDeleteTask.innerHTML = "DELETE";
                LiDeleteTask.onclick = function(){DeleteTask(this)};
                ItemDiv.appendChild(LiDeleteTask);

                var Itemli = document.createElement('li');
                Itemli.appendChild(ItemDiv)
                ItemOL.appendChild(Itemli);
            }
        }        
        temp+=1;
    });
}

function AddNewTask()
{
    var item = document.getElementById("NewItemBox");
    var http = new XMLHttpRequest();
    http.open('POST', '/Add', true);
    if (item.value == "")
    {
        alert("You didn't enter any task")
    }
    else
    {
        http.onreadystatechange = function() {
            if(http.readyState == 4 && http.status == 200)
            {
                if (http.response == "False")
                {
                    alert("Something went wrong")
                }
            }
            RefreshList();
        }
        http.send('DBG:'+UserInList+"ITEM:"+item.value);
    }
}

function AddList()
{
    var http = new XMLHttpRequest();
    http.open('POST', '/AddList', true);
    var str = prompt("Enter List Name:");
    if (str == "")
    {
        alert("You didn't enter any name")
    }
    else
    {
        http.onreadystatechange = function() {
            if(http.readyState == 4 && http.status == 200)
            {
                if (http.response == "False")
                {
                    alert("Something went wrong")
                }
            }
            RefreshList();
        }
        http.send(str);
    }
}

function DeleteTask(task)
{
    var http = new XMLHttpRequest();
    http.open('POST', '/Delete', true);
    http.onreadystatechange = function() {
        if(http.readyState == 4 && http.status == 200)
        {
            if (http.response == "False")
            {
                alert("Something went wrong")
            }
        }
        RefreshList();
    }
    http.send(task.name);
}

function DeleteList()
{
    var http = new XMLHttpRequest();
    http.open('POST', '/DeleteList', true);
    http.onreadystatechange = function() {
        if(http.readyState == 4 && http.status == 200)
        {
            if (http.response == "False")
            {
                alert("Something went wrong")
            }
        }
        UserInList = 1;
        RefreshList();
    }
    http.send(UserInList);
}

function EditTask(task)
{
    var http = new XMLHttpRequest();
    http.open('POST', '/Edit', true);
    http.onreadystatechange = function() {        
        if(http.readyState == 4 && http.status == 200)
        {
            if (http.response == "False")
            {
                alert("Something went wrong")
            }
        }
        RefreshList();
    }
    var str = prompt("Edit the Task:",task.id);
    if (str==null)
    {
        str = task.id;
    }
    http.send(task.name+"EDIT:"+str);
}

function EditListName()
{
    var http = new XMLHttpRequest();
    http.open('POST', '/EditListName', true);
    http.onreadystatechange = function() {        
        if(http.readyState == 4 && http.status == 200)
        {
            if (http.response == "False")
            {
                alert("Something went wrong")
            }
        }
        RefreshList();
    }
    initStr = document.getElementById('SelectedListName').innerHTML;
    var str = prompt("Edit the List Name:",initStr);
    if (str==null)
    {
        str = initStr;
    }
    http.send(UserInList+"EDIT:"+str);
}

function TaskCheckOrUncheck(checkbox)
{
    var http = new XMLHttpRequest();
    http.open('POST', '/Done', true);
    http.onreadystatechange = function() {        
        if(http.readyState == 4 && http.status == 200)
        {
            if (http.response == "False")
            {
                alert("Something went wrong")
            }
        }
        RefreshList();
    }
    if (checkbox.checked)
    {
        http.send(checkbox.name+"DONE:"+1);
    }
    else
    {
        http.send(checkbox.name+"DONE:"+0);
    }
}

function ExportToDoDB()
{
    var request = new XMLHttpRequest();
    request.open('GET', '/Temp.db', true);
    request.responseType = 'blob';

    request.onload = function()
    {
        // Only handle status code 200
        if(request.status === 200)
        {
            // The actual download
            var blob = new Blob([request.response], { type: 'application/octet-stream' });
            var link = document.createElement('a');
            link.href = window.URL.createObjectURL(blob);
            link.download = "ToDo.db";
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
            alert("The existing ToDo Database has been exported")
        }
        else if(request.status === 404)
        {
            alert("There was an error in obtaining the Database")
        }
        else
        {
            alert("There was an unknown error")
        }
    };
    request.send();
}

function DestroyToDoDBFrame()
{
    var http = new XMLHttpRequest();
    http.open('POST', '/DestroyToDoDBFrame', true);
    http.onreadystatechange = function() {        
        if(http.readyState == 4 && http.status == 200)
        {
            if (http.response == "True")
            {
                alert("ToDoDBFrame has been destroyed. you will be redirected to Homepage.")
                var link = document.createElement('a');
                link.href = '\index.html';
                document.body.appendChild(link);
                link.click();
                document.body.removeChild(link);
            }
            else
            {
                alert("There was an error. The server shall stop.");
                ShutDownServer();
            }
        }
    }
    http.send();
}

function ShutDownServer()
{
    var http = new XMLHttpRequest();
    alert("Attempting to shutdown the Webserver")
    http.open('POST', '/ShutDownServer', false);
    http.send();
}