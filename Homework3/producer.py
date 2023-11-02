import pika
import json

MESSAGE = {
    "id":11, 
    "packet_no":126, 
    "temperature":30, 
    "humidity":60, 
    "tds":1100, 
    "pH":5.0
}
EXCHANGE_NAME = 'sensor_data'

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type='fanout')
message = json.dumps(MESSAGE)
channel.basic_publish(exchange=EXCHANGE_NAME, routing_key='', body=message)

print(" [x] Sent %r" % message)
connection.close()