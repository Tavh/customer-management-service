from unittest import TestCase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Base
from database.customer_dal import CustomerDAL


class TestCustomerDAL(TestCase):
    def setUp(self):
        engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.customer_dal = CustomerDAL(session=self.session)

    def tearDown(self):
        self.session.close()

    def test_create_customer(self):
        customer_name = 'John Doe'
        customer = self.customer_dal.create_customer(name=customer_name)
        self.assertIsNotNone(customer.id)
        self.assertEqual(customer.name, customer_name)

    def test_get_customer_by_id(self):
        customer_name = 'John Doe'
        customer = self.customer_dal.create_customer(name=customer_name)
        retrieved_customer = self.customer_dal.get_customer_by_id(customer_id=customer.id)
        self.assertEqual(retrieved_customer, customer)

    def test_get_customers(self):
        customer_names = ['John Doe', 'Jane Smith', 'Bob Johnson']
        for name in customer_names:
            self.customer_dal.create_customer(name=name)
        customers = self.customer_dal.get_customers()
        self.assertEqual(len(customers), len(customer_names))
        self.assertCountEqual([c.name for c in customers], customer_names)

    def test_remove_customer(self):
        customer = self.customer_dal.create_customer(name='John Doe')
        self.customer_dal.remove_customer(customer_id=customer.id)
        retrieved_customer = self.customer_dal.get_customer_by_id(customer_id=customer.id)
        self.assertIsNone(retrieved_customer)

def test_update_customer(self):
        customer = self.customer_dal.create_customer(name='John Doe')
        new_name = 'Jane Smith'
        updated_customer = self.customer_dal.update_customer(customer_id=customer.id, name=new_name)
        self.assertEqual(updated_customer.name, new_name)
