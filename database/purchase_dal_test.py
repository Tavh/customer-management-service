from unittest import TestCase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Base, Purchase
from database.purchase_dal import PurchaseDAL


class TestPurchaseDAL(TestCase):
    def setUp(self):
        engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.purchase_dal = PurchaseDAL(session=self.session)

    def tearDown(self):
        self.session.close()

    def test_create_purchase(self):
        # Test that a new purchase can be created
        customer_id = 1
        item_id = 2
        price = 9.99
        purchase = self.purchase_dal.create_purchase(customer_id=customer_id, item_id=item_id, price_at_purchase_time=price)
        self.assertIsNotNone(purchase.id)
        self.assertEqual(purchase.customer_id, customer_id)
        self.assertEqual(purchase.item_id, item_id)
        self.assertEqual(purchase.price_at_purchase_time, price)

    def test_get_purchase_by_id(self):
        # Test that a purchase can be retrieved by its ID
        customer_id = 1
        item_id = 2
        price = 9.99
        purchase = self.purchase_dal.create_purchase(customer_id=customer_id, item_id=item_id, price_at_purchase_time=price)
        retrieved_purchase = self.purchase_dal.get_purchase_by_id(purchase_id=purchase.id)
        self.assertEqual(retrieved_purchase, purchase)

    def test_get_all_purchases(self):
        # Test that all purchases can be retrieved
        purchase_data = [
            {'customer_id': 1, 'item_id': 2, 'price': 9.99},
            {'customer_id': 2, 'item_id': 3, 'price': 19.99},
            {'customer_id': 1, 'item_id': 4, 'price': 4.99},
        ]
        purchases = []
        for data in purchase_data:
            purchase = self.purchase_dal.create_purchase(customer_id=data['customer_id'], item_id=data['item_id'], price_at_purchase_time=data['price'])
            purchases.append(purchase)
        retrieved_purchases = self.purchase_dal.get_all_purchases()
        self.assertEqual(len(retrieved_purchases), len(purchase_data))
        self.assertCountEqual([p.id for p in retrieved_purchases], [p.id for p in purchases])

