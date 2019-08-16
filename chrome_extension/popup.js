document.getElementById("submit").addEventListener("click", main);

function main(){
    var obj = [
        {
            "website": document.getElementById("myform").elements["website"].value,
            "ws_uname": document.getElementById("myform").elements["ws_uname"].value,
            "pc_uname": document.getElementById("myform").elements["pc_uname"].value,
            "pc_password": document.getElementById("myform").elements["pc_password"].value
        }
    ]
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            //alert(this.responseText);
        }
    };
    xhttp.open("POST", "http://127.0.0.1:8000/api/getcred/", true);
    xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.send(obj);
    xhttp.onload = function() {
        console.log(xhttp.response)
    }
}