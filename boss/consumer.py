import pika
params = pika.URLParameters('amqps://dphldeck:Ep9eWiO_Im1y0IjeuKFsUwbqLkXPaHLa@dingo.rmq.cloudamqp.com/dphldeck')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='boss')

def callback(ch,method,pro,body):
    print('Received in order')
    print(body)

channel.basic_consume(queue='boss', on_message_callback=callback)

print('Started consuming')

channel.start_consuming()

channel.close()
