from unittest import TestCase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Base
from database.item_dal import ItemDAL


class TestItemDAL(TestCase):
    def setUp(self):
        engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.item_dal = ItemDAL(session=self.session)

    def tearDown(self):
        self.session.close()

    def test_create_item(self):
        # Test that a new item can be created
        item_name = 'Widget'
        item_price = 9.99
        item = self.item_dal.create_item(name=item_name, price=item_price)
        self.assertIsNotNone(item.id)
        self.assertEqual(item.name, item_name)
        self.assertEqual(item.price, item_price)

    def test_get_item_by_id(self):
        # Test that an item can be retrieved by its ID
        item_name = 'Widget'
        item_price = 9.99
        item = self.item_dal.create_item(name=item_name, price=item_price)
        retrieved_item = self.item_dal.get_item_by_id(item_id=item.id)
        self.assertEqual(retrieved_item, item)

    def test_get_all_items(self):
        # Test that all items can be retrieved
        item_data = [
            {'name': 'Widget', 'price': 9.99},
            {'name': 'Gizmo', 'price': 19.99},
            {'name': 'Doodad', 'price': 4.99},
        ]
        items = []
        for data in item_data:
            item = self.item_dal.create_item(name=data['name'], price=data['price'])
            items.append(item)
        retrieved_items = self.item_dal.get_all_items()
        self.assertEqual(len(retrieved_items), len(item_data))
        self.assertCountEqual([i.id for i in retrieved_items], [i.id for i in items])
