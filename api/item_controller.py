from flask import Flask, jsonify, request
from sqlalchemy.orm import Session
from database.item_dal import ItemDAL


class ItemController:
    def __init__(self, app: Flask, session: Session):
        self.app = app
        self.item_dal = ItemDAL(session=session)

        self.register_endpoints()

    def register_endpoints(self):
        self.app.route('/items', methods=['POST'])(self.create_item)
        self.app.route('/items/<item_id>', methods=['GET'])(self.get_item)
        self.app.route('/items', methods=['GET'])(self.get_items)
        self.app.route('/items/<item_id>', methods=['PUT'])(self.update_item)
        self.app.route('/items/<item_id>', methods=['DELETE'])(self.delete_item)

    def create_item(self):
        data = request.get_json()
        item = self.item_dal.create_item(name=data['name'], price=data['price'])
        return item.to_json()

    def get_item(self, item_id):
        item = self.item_dal.get_item_by_id(item_id=item_id)
        return item.to_json()

    def get_items(self):
        items = self.item_dal.get_all_items()
        return jsonify([i.to_json() for i in items])

    def update_item(self, item_id):
        data = request.get_json()
        item = self.item_dal.update_item(item_id=item_id, name=data['name'], price=data['price'])
        if item:
            return item.to_json()
        else:
            return '', 404

    def delete_item(self, item_id):
        self.item_dal.remove_item(item_id=item_id)
        return '', 204
