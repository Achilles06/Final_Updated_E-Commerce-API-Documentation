
from flask import Blueprint, request, jsonify

production_blueprint = Blueprint('production', __name__)

# In-memory data storage for demonstration
production_entries = {}

# Get all production entries
@production_blueprint.route('/production', methods=['GET'])
def get_production():
    return jsonify(list(production_entries.values())), 200

# Get a production entry by ID
@production_blueprint.route('/production/<int:entry_id>', methods=['GET'])
def get_production_entry(entry_id):
    entry = production_entries.get(entry_id)
    if not entry:
        return jsonify({'error': 'Production entry not found'}), 404
    return jsonify(entry), 200

# Create a new production entry
@production_blueprint.route('/production', methods=['POST'])
def create_production_entry():
    data = request.json
    entry_id = len(production_entries) + 1
    production_entries[entry_id] = {'id': entry_id, **data}
    return jsonify(production_entries[entry_id]), 201

# Update a production entry by ID
@production_blueprint.route('/production/<int:entry_id>', methods=['PUT'])
def update_production_entry(entry_id):
    if entry_id not in production_entries:
        return jsonify({'error': 'Production entry not found'}), 404
    data = request.json
    production_entries[entry_id].update(data)
    return jsonify(production_entries[entry_id]), 200

# Delete a production entry by ID
@production_blueprint.route('/production/<int:entry_id>', methods=['DELETE'])
def delete_production_entry(entry_id):
    if entry_id not in production_entries:
        return jsonify({'error': 'Production entry not found'}), 404
    del production_entries[entry_id]
    return '', 204
