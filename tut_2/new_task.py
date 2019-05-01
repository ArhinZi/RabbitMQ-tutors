#!/usr/bin/env python
import pika
import sys
import random

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

for i in range(10):
    message = "Msg#{0} ".format(i)
    for k in range(random.randint(0, 10)):
        message += "."

    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=2,  # make message persistent
        ))
    print(" [x] Sent %r" % message)
connection.close()