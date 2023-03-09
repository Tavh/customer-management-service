from kafka import KafkaConsumer
from json import loads
from database.purchase_dal import PurchaseDAL
from threading import Thread


class KafkaPurchaseConsumer:
    def __init__(self, purchase_dal: PurchaseDAL, topic: str, bootstrap_servers: str):
        self.purchase_dal = purchase_dal
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=bootstrap_servers,
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            value_deserializer=lambda x: loads(x.decode('utf-8'))
        )

    def consume(self):
        for message in self.consumer:
            print(message)
            message = message.value
            if message['event_type'] == 'purchase':
                customer_id = message['customer_id']
                item_id = message['item_id']
                purchase = self.purchase_dal.create_purchase(customer_id=customer_id, item_id=item_id)
                print(f"Created purchase: {purchase.to_json()}")

    def start(self):
        thread = Thread(target=self.consume)
        thread.start()