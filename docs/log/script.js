red = "<span style='color: red'>";
orange = "<span style='color: orange'>";
yellow = "<span style='color: yellow'>";
white = "<span style='color: white'>";
gray = "<span style='color: gray'>";

coloredEntries = []

function highlightText(log){
  log = log.split("\n");

  log.forEach(function(entry){
    if(entry.includes("CRITICAL ")){
      coloredEntry = red + entry + "</span>";
    }

    if(entry.includes("ERROR ")){
      coloredEntry = orange + entry + "</span>";
    }

    if(entry.includes("WARNING ")){
      coloredEntry = yellow + entry + "</span>";
    }

    if(entry.includes("INFO ")){
      coloredEntry = white + entry + "</span>";
    }

    if(entry.includes("DEBUG ")){
      coloredEntry = gray + entry + "</span>";
    }

    coloredEntries.push(coloredEntry);
  });

  coloredEntries.pop();
  coloredEntries.reverse();
  document.getElementById("terminal").innerHTML = coloredEntries.join("\n");
}

var xhttp=new XMLHttpRequest();

xhttp.onreadystatechange=function(){
  if(this.readyState==4&&this.status==200){
    document.getElementById("terminal").innerHTML = this.responseText;
    highlightText(this.responseText)
  }
};

xhttp.open("GET","https://raw.githubusercontent.com/wiki/paramt/MemeAdviser/memeadviser.log");
xhttp.send();
