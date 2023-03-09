from database.models import Customer, Purchase
from typing import List, Optional
from sqlalchemy.orm import Session

class CustomerDAL:
    def __init__(self, session: Session):
        self.session = session

    def create_customer(self, name: str) -> Customer:
        customer = Customer(name=name)
        self.session.add(customer)
        self.session.commit()
        return customer

    def get_customer_by_id(self, customer_id: int) -> Optional[Customer]:
        return self.session.query(Customer).filter_by(id=customer_id).first()
    
    def get_customer_purchases(self, customer_id: int) -> List[Purchase]:
        return self.session.query(Purchase).filter_by(customer_id=customer_id).all()