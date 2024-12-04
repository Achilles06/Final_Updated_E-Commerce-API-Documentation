
from flask import Blueprint, request, jsonify

customers_blueprint = Blueprint('customers', __name__)

# In-memory data storage for demonstration
customers = {}

# Get all customers
@customers_blueprint.route('/customers', methods=['GET'])
def get_customers():
    return jsonify(list(customers.values())), 200

# Get a customer by ID
@customers_blueprint.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    customer = customers.get(customer_id)
    if not customer:
        return jsonify({'error': 'Customer not found'}), 404
    return jsonify(customer), 200

# Create a new customer
@customers_blueprint.route('/customers', methods=['POST'])
def create_customer():
    data = request.json
    customer_id = len(customers) + 1
    customers[customer_id] = {'id': customer_id, **data}
    return jsonify(customers[customer_id]), 201

# Update a customer by ID
@customers_blueprint.route('/customers/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    if customer_id not in customers:
        return jsonify({'error': 'Customer not found'}), 404
    data = request.json
    customers[customer_id].update(data)
    return jsonify(customers[customer_id]), 200

# Delete a customer by ID
@customers_blueprint.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    if customer_id not in customers:
        return jsonify({'error': 'Customer not found'}), 404
    del customers[customer_id]
    return '', 204
