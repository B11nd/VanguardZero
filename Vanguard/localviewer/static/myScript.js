let weather_api_url = 'https://api.openweathermap.org/data/2.5/weather?lat=49.882114&lon=-119.477829&appid=4aca2fb11185391c6d2e069116b60f57&units=metric'; 

const getweather = async () => {
  const response = await fetch(weather_api_url);
  notsoup = await response.json();
  if (response.ok) {
    console.log(notsoup.main.temp.toPrecision(2)); // Get JSON value from the response body
    console.log(notsoup.main.temp_min.toPrecision(2)); // Get JSON value from the response body
    console.log(notsoup.main.temp_max.toPrecision(2)); // Get JSON value from the response body
    console.log(notsoup.weather[0].main); // Get JSON value from the response body
    console.log(notsoup.weather[0].icon); // Get JSON value from the response body
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
chatSocket.onmessage = function(e) {
  let data = JSON.parse(e.data);
  console.log(data);
}







let serverlocation = '10.0.0.232'
let serverport = 9001
client = new Paho.MQTT.Client(serverlocation, serverport, "clientId");

client.onConnectionLost = onConnectionLost;
client.onMessageArrived = onMessageArrived;

client.connect({onSuccess:onConnect});

function onConnect() {
  client.subscribe("sensorstate");
}

function onConnectionLost(responseObject) {
  if (responseObject.errorCode !== 0) {
    console.log("onConnectionLost:"+responseObject.errorMessage);
  }
}

function onMessageArrived(message) {
  console.log(message);
}