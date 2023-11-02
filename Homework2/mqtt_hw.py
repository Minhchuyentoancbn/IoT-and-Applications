import random
import time
import json

from paho.mqtt import client as mqtt_client


broker = 'broker.hivemq.com'
port = 1883
topic = "python/mqtt/minh-iot"
# Generate a Client ID with the publish prefix.
# client_id = f'publish-{random.randint(0, 1000)}'
client_id = f'subscribe-{random.randint(0, 1000)}'

PUBLISH_MESSAGE = {"id":11, "packet_no":126, "temperature":30, "humidity":60, "tds":1100, "pH":5.0}


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client):
    # msg = f"messages: {msg_count}"
    msg = json.dumps(PUBLISH_MESSAGE)
    result = client.publish(topic, msg)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)
    client.loop_stop()


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        for key, value in json.loads(msg.payload.decode()).items():
            print(f"{key}: {value}")

    client.subscribe(topic)
    client.on_message = on_message


def run2():
    client = connect_mqtt()
    client.loop_start()
    subscribe(client)
    publish(client)
    time.sleep(10)
    # client.loop_forever()



if __name__ == '__main__':
    # run()
    run2()
