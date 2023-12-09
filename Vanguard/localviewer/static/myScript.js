let weather_api_url = 'https://api.openweathermap.org/data/2.5/weather?lat=49.882114&lon=-119.477829&appid=4aca2fb11185391c6d2e069116b60f57&units=metric'; 

const getweather = async () => {
  const response = await fetch(weather_api_url);
  notsoup = await response.json();
  if (response.ok) {
    let apic = notsoup.main.temp.toPrecision(1);
    let maxC = notsoup.main.temp_max.toPrecision(1);
    let minC = notsoup.main.temp_min.toPrecision(1);
    let weather = notsoup.weather[0].main;
    let weatherimg = notsoup.weather[0].icon;

    document.getElementById('weatherimg').src = "http://openweathermap.org/img/wn/"+weatherimg+"@2x.png";

    document.getElementById('apiC').innerHTML = apic;
    document.getElementById('maxC').innerHTML = maxC;
    document.getElementById('minC').innerHTML = minC;
    document.getElementById('weather').innerHTML = weather;
    return
  }
}
addEventListener("load", getweather)
setInterval(getweather, 120000);


let url = 'ws://127.0.0.1:8000/ws/socket-server/';
const chatSocket = new WebSocket(url);
chatSocket.onopen = function(e) {
  console.log("Websocket Open");
  chatSocket.send("FCPV")
}
chatSocket.onmessage = function(event){
  console.log("client says server message received:")
}







let serverlocation = 'localhost'
let serverport = 9001
client = new Paho.MQTT.Client(serverlocation, serverport, "clientId");

client.onConnectionLost = onConnectionLost;
client.onMessageArrived = onMessageArrived;

client.connect({onSuccess:onConnect});
function onConnect() {
  client.subscribe("esp32/output");
  client.subscribe("sensors");
}

function onConnectionLost(responseObject) {
  if (responseObject.errorCode !== 0) {
    console.log("onConnectionLost:"+responseObject.errorMessage);
  }
}

function onMessageArrived(message) {
  if(message.payloadString=="on"){
    document.getElementById('Bedroom').style.backgroundColor = "#071739";
    document.getElementById('lightdot').style.display = "none";
    console.log(message.payloadString);
  }
  else if(message.payloadString=="off"){BedroomLight
    document.getElementById('Bedroom').style.backgroundColor = "#709fdc";
    document.getElementById('lightdot').style.display = "inline";
    console.log(message.payloadString);
  }

  else if(message.payloadBytes[0]==48){
    if (message.payloadBytes[23]==48){
      document.getElementById('BedroomLight').style.backgroundColor = "#071739";
      document.getElementById('LockTop').style.borderColor = "#63a583";
      document.getElementById('LockBottom').style.borderColor = "#63a583";
    }
    else if(message.payloadBytes[23]==49){
      document.getElementById('BedroomLight').style.backgroundColor = "#709fdc";
      document.getElementById('LockTop').style.borderColor = "red";
      document.getElementById('LockBottom').style.borderColor = "red";
    }
  }
}

function ShowNav(){  
  var mainmenubutton = document.getElementById('mainmenubnt');
  var menubutton = document.getElementsByClassName('submenu');
  
  mainmenubutton.src =  mainmenubutton.src == 'http://127.0.0.1:8000/static/menu.svg' ? 'http://127.0.0.1:8000/static/x.svg' : 'http://127.0.0.1:8000/static/menu.svg';
  
  menubutton[0].classList.toggle('active');
  menubutton[1].classList.toggle('active'); 
  menubutton[2].classList.toggle('active'); 
}

function AddAddMenu(){  
  addmenu = document.getElementById('addmenu');
  addmenu.classList.toggle('menuactive');
}

function AddEditMenu(){  
}

function AddSettingMenu(){  
}

function eventadd(){
  eventaddmenu = document.getElementById("eventaddform");
  eventaddmenu.classList.toggle('menuactive');
}