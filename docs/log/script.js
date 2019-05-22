var xhttp=new XMLHttpRequest();

xhttp.onreadystatechange=function(){
  if(this.readyState==4&&this.status==200){
    document.getElementById("terminal").innerHTML = this.responseText;
  }
};

xhttp.open("GET","https://raw.githubusercontent.com/wiki/paramt/MemeAdviser/memeadviser.log");
xhttp.send();
