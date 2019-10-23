function Update()
{
    for (let i = 0; i < 3; i++)
    {        
        var ll = document.createElement('li');
        ll.innerHTML = "New"+i;
        document.getElementById("ListBarOL").appendChild(ll);
    }
}