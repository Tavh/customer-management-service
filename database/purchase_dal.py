from typing import List, Optional
from database.models import Purchase
from sqlalchemy.orm import Session

class PurchaseDAL:
    def __init__(self, session: Session):
        self.session = session

    def create_purchase(self, customer_id: int, item_id: int, price_at_purchase_time: float) -> Purchase:
        purchase = Purchase(
            customer_id=customer_id,
            item_id=item_id,
            price_at_purchase_time=price_at_purchase_time
        )
        self.session.add(purchase)
        self.session.commit()
        return purchase

    def get_purchase_by_id(self, purchase_id: int) -> Optional[Purchase]:
        return self.session.query(Purchase).filter_by(id=purchase_id).first()

    def get_all_purchases(self) -> List[Purchase]:
        return self.session.query(Purchase).all()







