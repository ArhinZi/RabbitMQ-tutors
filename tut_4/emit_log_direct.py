#!/usr/bin/env python
import pika
import sys
from random import randint

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

for i in range(50):

    s = randint(0, 2)
    if(s == 0):
        severity = 'error'
    elif(s == 1):
        severity = 'warning'
    elif(s == 2):
        severity = 'info'

    message = "[{0}] Message".format(severity)
    channel.basic_publish(
        exchange='direct_logs', routing_key=severity, body=message)
    print(" [x] Sent %r:%r" % (severity, message))

connection.close()
