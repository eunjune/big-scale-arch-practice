import pika
params = pika.URLParameters('amqps://dphldeck:Ep9eWiO_Im1y0IjeuKFsUwbqLkXPaHLa@dingo.rmq.cloudamqp.com/dphldeck')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='boss', body='hello')