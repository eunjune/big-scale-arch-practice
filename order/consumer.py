import pika
import json
import os,django
from order.user_order.models import Order,Shop

os.environ.setdefault("DJANGO_SETTINGS_MODULE",'order.settings')
django.setup()

params = pika.URLParameters('')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='order')

def callback(ch,method,pro,body):
    print('Received in order')
    id = json.loads(body)
    print(id)
    order = Order.objects.get(id=id)
    order.deliver_finish = 1
    order.save()
    print('order deliver finished')

channel.basic_consume(queue='order', on_message_callback=callback, auto_ack=True)

print('Started consuming')

channel.start_consuming()

channel.close()
