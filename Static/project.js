function changeText(id) {
    id.innerHTML = "you have changed this text with an 'onclick' event"
}


function displayDate(id) {
    document.getElementById("date").innerHTML = Date();
}


function checkCookies() {
    let text = ""
    if (navigator.cookiesEnabled == true) {
        text = "cookies are enabled";
    } else {
        text = "cookies are not enabled";
    }
    document.getElementById("cookie").innerHTML = text;
}


function mOver(obj) {
   obj.innerHTML = "<br> HELLO"
}

function mOut(obj) {
    obj.innerHTML = ""
}


function sendAlert() {
    alert(location.hostname);
}

function myToggle ( ) {
    let element = document.body;
    element.classList.toggle("dark-mode");
    let mainBox = document.getElementsByClassName("main-box");
    element.classList.toggle("dark-mode");

    for (const i of mainBox) {
        i.classList.toggle("dark-modeb")
    }
}