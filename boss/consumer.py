import pika
import json

from boss.main import db, Shop, Order

params = pika.URLParameters('')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='boss')

def callback(ch,method,proerties,body):
    print('Received in boss')
    data = json.loads(body)
    print(data)

    if proerties.content_typ == 'shop_created':
        shop = Shop(id=data['id'], shop_name=data['shop_name'], shop_address=data['shop_address'])
        db.session.add(shop)
        db.session.commit()
    elif proerties.content_typ == 'shop_updated':
        shop = Shop.query.get(data['id'])
        shop.shop_name = data['shop_name']
        shop.shop_address = data['shop_address']
        db.session.commit()

    elif proerties.content_typ == 'shop_deleted':
        shop = Shop.query.get(data)
        db.session.delete(shop)
        db.session.commit()
    elif proerties.content_typ == 'order_created':
        order = Order(id=data['id'],shop=data['shop'],address=data['address'])
        db.session.add(order)
        db.session.commit()
    elif proerties.content_typ == 'order_updated':
        order = Order.query.get(data['id'])
        order.order_name = data['order_name']
        order.order_address = data['order_address']
        db.session.commit()
    elif proerties.content_typ == 'order_deleted':
        order = Order.query.get(data)
        db.session.delete(order)
        db.session.commit()

channel.basic_consume(queue='boss', on_message_callback=callback, auto_ack=True)

print('Started consuming')

channel.start_consuming()

channel.close()
