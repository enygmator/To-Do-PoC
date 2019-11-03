function ImportToDoDB(event)
{
    var fileList = event.target.files;
    var ToDodb = fileList[0];
    var http = new XMLHttpRequest();
    http.open('POST', '/Temp.db', true);
    http.setRequestHeader('Content-type', 'application/octet-stream');
    http.onreadystatechange = function() {
        if(http.readyState == 4 && http.status == 200) {
            if (http.responseText == "There was an error importing the database" || http.responseText == "There was an error in creating the database")
            {
                alert(http.responseText);	
                //Reload the page and ignore the browser cache.
                window.location.reload(true);
            }
            else
            {
                alert(http.responseText);
                GoToTODOHTML();
            }
        }
    }
    http.send(ToDodb);
}

function NewToDoDB()
{
    var http = new XMLHttpRequest();
    http.open('POST', '/NewToDoDataBase', true);
    http.onreadystatechange = function()
    {
        if(http.readyState == 4 && http.status == 200) {
            alert(http.responseText);
            GoToTODOHTML();
        }
    }
    http.send();
}

function GoToTODOHTML()
{
    var link = document.createElement('a');
    link.href = '/ToDo.html';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}