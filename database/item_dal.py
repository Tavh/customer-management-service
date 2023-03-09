from typing import List, Optional
from database.models import Item
from sqlalchemy.orm import Session

class ItemDAL:
    def __init__(self, session: Session):
        self.session = session

    def create_item(self, name: str, price: float) -> Item:
        item = Item(name=name, price=price)
        self.session.add(item)
        self.session.commit()
        return item

    def get_item_by_id(self, item_id: int) -> Optional[Item]:
        return self.session.query(Item).filter_by(id=item_id).first()

    def get_all_items(self) -> List[Item]:
        return self.session.query(Item).all()

