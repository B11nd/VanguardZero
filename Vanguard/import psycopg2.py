from paho.mqtt import client as mqtt_client
import os, django 

PROJECT_NAME = 'Vanguard'

broker = '10.0.0.232'
port = 1883
topic = "sensors"
client_id = f'django'

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        payload = msg.payload.decode()
        global sensorid, ownerid, sensortype, sensorpayload
        sensorid = payload[0:10]
        ownerid = payload[10:20]
        sensortype = int(payload[20:22], 16)
        sensorpayload = int(payload[22:24], 16)
        sensorimport = sensor(SensorId=sensorid, OwnerId=ownerid, type=sensortype, payload=sensorpayload)
        sensorimport.save()
    client.subscribe(topic)
    client.on_message = on_message

def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', '%s.settings' % PROJECT_NAME)
    django.setup()
    from localviewer.models import sensor

    run()