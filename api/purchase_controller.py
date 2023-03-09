from flask import Flask, jsonify, request
from sqlalchemy.orm import Session
from database.purchase_dal import PurchaseDAL

class PurchaseController:
    def __init__(self, app: Flask, session: Session):
        self.app = app
        self.purchase_dal = PurchaseDAL(session=session)

        self.register_endpoints()

    def register_endpoints(self):
        self.app.route('/purchases', methods=['POST'])(self.create_purchase)
        self.app.route('/purchases/<purchase_id>', methods=['GET'])(self.get_purchase)
        self.app.route('/purchases', methods=['GET'])(self.get_all_purchases)

    def create_purchase(self):
        data = request.get_json()
        purchase = self.purchase_dal.create_purchase(
            customer_id=data['customer_id'],
            item_id=data['item_id'],
            price_at_purchase_time=data['price_at_purchase_time']
        )
        return purchase.to_json()

    def get_purchase(self, purchase_id):
        purchase = self.purchase_dal.get_purchase_by_id(purchase_id=purchase_id)
        return purchase.to_json()

    def get_all_purchases(self):
        purchases = self.purchase_dal.get_all_purchases()
        return jsonify([p.to_json() for p in purchases])
