function readFiles(event)
{
    var fileList = event.target.files;
    var ToDodb = fileList[0];
    var http = new XMLHttpRequest();
    http.open('POST', '/', true);
    http.setRequestHeader('Content-type', 'application/octet-stream');
    http.onreadystatechange = function() {//Call a function when the state changes.
        if(http.readyState == 4 && http.status == 200) {
            alert(http.responseText);
        }
    }
    http.send(ToDodb);
}

function NewToDoDB()
{
    var http = new XMLHttpRequest();
    http.open('POST', '/', true);
    http.send("NewToDoDatabase");
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
        }
    };
    request.send();
    alert("The existing ToDo Database has been exported")
}