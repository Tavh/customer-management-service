from database.models import Customer
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

    def get_customers(self) -> List[Customer]:
        return self.session.query(Customer).all()

    def remove_customer(self, customer_id: int):
        customer = self.get_customer_by_id(customer_id)
        if customer:
            self.session.delete(customer)
            self.session.commit()

    def update_customer(self, customer_id: int, name: str) -> Optional[Customer]:
        customer = self.get_customer_by_id(customer_id)
        if customer:
            customer.name = name
            self.session.commit()
        return customer