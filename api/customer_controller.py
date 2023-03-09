from flask import Flask, jsonify, request
from sqlalchemy.orm import Session
from database.customer_dal import CustomerDAL

class CustomerController:
    def __init__(self, app: Flask, session: Session):
        self.app = app
        self.customer_dal = CustomerDAL(session=session)

        self.register_endpoints()

    def register_endpoints(self):
        self.app.route('/customers', methods=['POST'])(self.create_customer)
        self.app.route('/customers/<customer_id>', methods=['GET'])(self.get_customer)
        self.app.route('/customers', methods=['GET'])(self.get_customers)
        self.app.route('/customers/<customer_id>', methods=['DELETE'])(self.remove_customer)
        self.app.route('/customers/<customer_id>', methods=['PUT'])(self.update_customer)

    def create_customer(self):
        data = request.get_json()
        customer = self.customer_dal.create_customer(name=data['name'])
        return customer.to_json()

    def get_customer(self, customer_id):
        customer = self.customer_dal.get_customer_by_id(customer_id=customer_id)
        return customer.to_json()

    def get_customers(self):
        customers = self.customer_dal.get_customers()
        return jsonify([c.to_json() for c in customers])

    def remove_customer(self, customer_id):
        self.customer_dal.remove_customer(customer_id=customer_id)
        return '', 204

    def update_customer(self, customer_id):
        data = request.get_json()
        customer = self.customer_dal.update_customer(customer_id=customer_id, name=data['name'])
        return customer.to_json()