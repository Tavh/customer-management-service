from flask import Flask, jsonify, request
from sqlalchemy.orm import Session
from database.customer_dal import CustomerDAL


class RestController:
    def __init__(self, app: Flask, session: Session, customer_dal: CustomerDAL):
        self.app = app
        self.customer_dal = customer_dal

        self.register_endpoints()

    def register_endpoints(self):
        self.app.route('/customers/<customer_id>/purchases', methods=['GET'])(self.get_customer_purchases)

    def get_customer_purchases(self, customer_id):
        purchases = self.customer_dal.get_customer_purchases(customer_id=customer_id)
        print(purchases)
        return jsonify([p.to_json() for p in purchases])
