from random import randint
from database.customer_dal import CustomerDAL
from database.item_dal import ItemDAL
from database.purchase_dal import PurchaseDAL
from sqlalchemy.orm import Session

class DatabaseSeeder:
    def __init__(self, session: Session):
        self.session = session
        self.customer_dal = CustomerDAL(session=session)
        self.item_dal = ItemDAL(session=session)
        self.purchase_dal = PurchaseDAL(session=session)

    def run(self):
        # Create 50 customers
        customers = []
        for i in range(50):
            name = f'Customer {i}'
            customer = self.customer_dal.create_customer(name=name)
            customers.append(customer)

        # Create 10 items
        items = []
        for i in range(10):
            name = f'Item {i}'
            price = 10.0 + i
            item = self.item_dal.create_item(name=name, price=price)
            items.append(item)

        # Assign random purchases to customers
        for customer in customers:
            for i in range(10):
                item = items[randint(0, len(items) - 1)]
                self.purchase_dal.create_purchase(
                    customer_id=customer.id,
                    item_id=item.id,
                    price_at_purchase_time=item.price
                )

        self.session.commit()

