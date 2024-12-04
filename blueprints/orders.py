
from flask import Blueprint, request, jsonify

orders_blueprint = Blueprint('orders', __name__)

# In-memory data storage for demonstration
orders = {}

# Get all orders
@orders_blueprint.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(list(orders.values())), 200

# Get an order by ID
@orders_blueprint.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = orders.get(order_id)
    if not order:
        return jsonify({'error': 'Order not found'}), 404
    return jsonify(order), 200

# Create a new order
@orders_blueprint.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    order_id = len(orders) + 1
    orders[order_id] = {'id': order_id, **data}
    return jsonify(orders[order_id]), 201

# Update an order by ID
@orders_blueprint.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    if order_id not in orders:
        return jsonify({'error': 'Order not found'}), 404
    data = request.json
    orders[order_id].update(data)
    return jsonify(orders[order_id]), 200

# Delete an order by ID
@orders_blueprint.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    if order_id not in orders:
        return jsonify({'error': 'Order not found'}), 404
    del orders[order_id]
    return '', 204
