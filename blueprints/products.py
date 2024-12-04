
from flask import Blueprint, request, jsonify

products_blueprint = Blueprint('products', __name__)

# In-memory data storage for demonstration
products = {}

# Get all products
@products_blueprint.route('/products', methods=['GET'])
def get_products():
    return jsonify(list(products.values())), 200

# Get a product by ID
@products_blueprint.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = products.get(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    return jsonify(product), 200

# Create a new product
@products_blueprint.route('/products', methods=['POST'])
def create_product():
    data = request.json
    product_id = len(products) + 1
    products[product_id] = {'id': product_id, **data}
    return jsonify(products[product_id]), 201

# Update a product by ID
@products_blueprint.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    if product_id not in products:
        return jsonify({'error': 'Product not found'}), 404
    data = request.json
    products[product_id].update(data)
    return jsonify(products[product_id]), 200

# Delete a product by ID
@products_blueprint.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    if product_id not in products:
        return jsonify({'error': 'Product not found'}), 404
    del products[product_id]
    return '', 204
