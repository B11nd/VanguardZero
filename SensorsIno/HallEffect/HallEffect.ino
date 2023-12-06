#include <WiFi.h>
#include <PubSubClient.h>
#include <Wire.h>

bool soup, notsoup = true;
long sensorid = 0x0000, ownerid = 0x7FFFFFFF;
byte type = 0xf0, payload = 0xF0;
char msg[30];

const char* ssid = "MARKTOP";
const char* password = "catsoupisnice";
const char* mqtt_server = "192.168.137.1";
WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
  Serial.begin(115200);
  pinMode(12, INPUT);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
}

void setup_wifi() {
  delay(10);
  Serial.print("Connecting Wifi");
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println(WiFi.localIP());
}

void reconnect() {
  while (!client.connected()) {
    Serial.print("Connecting MQTT");
    if (client.connect("doorsensor")) {
      Serial.println("connected");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      delay(5000);
    }
  }
}

void loop() {

  if (!client.connected()) {
    reconnect();
  }

  client.loop();
  soup = digitalRead(12);
  
  if(soup != notsoup){
    payload = soup;
    sprintf(msg, "%010d%010d%02x%02X", sensorid, ownerid, type, payload);
    client.publish("sensors", msg);
    notsoup = soup;
  }

}
