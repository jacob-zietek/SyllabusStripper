function runFile() {

}

var shown = false;
function dropShow() {
    if(shown == true)
    { dropHide(); }else{
        shown = true;
        document.getElementById('dropdown-content').style.display = 'block';
    }
}
function dropHide() {
    document.getElementById('dropdown-content').style.display = 'none';
    shown = false;
}
function onAboutUs() {
    document.getElementById("overlay1").style.display = "block";
}
function onWhatThis() {
    document.getElementById("overlay2").style.display = "block";
}
function off() {
    document.getElementById("overlay1").style.display = "none";
    document.getElementById("overlay2").style.display = "none";
}

function dotdotdot() {
    for(var i = 0; i < 6; i++) {
        document.getElementById("confirm2").textContent = "Downloading"
        sleep(500);
        document.getElementById("confirm2").textContent = "Downloading."
        sleep(500);
        document.getElementById("confirm2").textContent = "Downloading.."
        sleep(500);
        document.getElementById("confirm2").textContent = "Downloading..."
        sleep(500);
    }

}

function log() {
    document.getElementById("confirm").style.display = "block"
    document.getElementById("confirm2").style.display = "block"
    dotdotdot();
    document.getElementById("confirm2").textContent = "Click Below for the Calendar File!"
}

function sleep(ms)
{
    return new Promise(resolve => setTimeout(resolve, ms));
}