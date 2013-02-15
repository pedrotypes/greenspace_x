from mongoengine import *
from core import *
import pika

# Mongo
connect('stargame')

# RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='greenspace_fleet')


def on_request(ch, method, props, body):
    print body
    response = body

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id, content_type='text/plain'),
                     body=response)
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='greenspace_fleet')

print " [x] Awaiting fleet commands"
channel.start_consuming()
