from typing import List, Optional
from database.models import Purchase, Item, Customer
from sqlalchemy.orm import Session

class PurchaseDAL:
    def __init__(self, session: Session):
        self.session = session

    def create_purchase(self, customer_id: int, item_id: int) -> Purchase:
        # Get the customer and item objects from the database
        customer = self.session.query(Customer).get(customer_id)
        item = self.session.query(Item).get(item_id)

        # If either the customer or the item is not found, return None
        if not customer or not item:
            return None

        price_at_purchase_time = item.price

        purchase = Purchase(
            customer_id=customer_id,
            item_id=item_id,
            price_at_purchase_time=price_at_purchase_time
        )
    
        self.session.add(purchase)
        self.session.commit()
        return purchase








