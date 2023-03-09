from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship
from sqlalchemy.sql import func
from flask import jsonify


Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


    def to_json(self):
        return jsonify({
            'id': self.id,
            'name': self.name,
            'purchases': [purchase.to_json() for purchase in self.purchases]
        })


class Item(Base):
    __tablename__ = 'items'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)


    def to_json(self):
        return jsonify({
            'id': self.id,
            'name': self.name,
            'price': self.price
        })

class Purchase(Base):
    __tablename__ = 'purchases'
    
    id = Column(Integer, primary_key=True)
    purchase_time = Column(String, nullable=False, server_default=func.now())
    price_at_purchase_time = Column(Float, nullable=False)

    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    customer = relationship('Customer', backref='purchases')
    
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
    item = relationship('Item', backref='purchases')

    def to_json(self):
        return {
            'id': self.id,
            'purchase_time': self.purchase_time,
            'price_at_purchase_time': self.price_at_purchase_time,
            'customer': {
                'id': self.customer.id,
                'name': self.customer.name
            },
            'item': {
                'id': self.item.id,
                'name': self.item.name,
                'price': self.item.price
            }
        }
