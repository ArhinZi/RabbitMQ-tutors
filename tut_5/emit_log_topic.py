#!/usr/bin/env python
import pika
import sys
from random import randint

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

for i in range(50):
    routing_key = "{0}.{1}.{2}.{3}".format(randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5))
    message = "Msg#{0}".format(i)
    channel.basic_publish(
        exchange='topic_logs', routing_key=routing_key, body=message)
    print(" [x] Sent %r:%r" % (routing_key, message))
connection.close()