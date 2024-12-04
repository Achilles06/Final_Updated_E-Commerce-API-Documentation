
from flask import Blueprint, request, jsonify

employee_blueprint = Blueprint('employee', __name__)

# In-memory data storage for demonstration
employees = {}

# Get all employees
@employee_blueprint.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(list(employees.values())), 200

# Get an employee by ID
@employee_blueprint.route('/employees/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    employee = employees.get(employee_id)
    if not employee:
        return jsonify({'error': 'Employee not found'}), 404
    return jsonify(employee), 200

# Create a new employee
@employee_blueprint.route('/employees', methods=['POST'])
def create_employee():
    data = request.json
    employee_id = len(employees) + 1
    employees[employee_id] = {'id': employee_id, **data}
    return jsonify(employees[employee_id]), 201

# Update an employee by ID
@employee_blueprint.route('/employees/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    if employee_id not in employees:
        return jsonify({'error': 'Employee not found'}), 404
    data = request.json
    employees[employee_id].update(data)
    return jsonify(employees[employee_id]), 200

# Delete an employee by ID
@employee_blueprint.route('/employees/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    if employee_id not in employees:
        return jsonify({'error': 'Employee not found'}), 404
    del employees[employee_id]
    return '', 204
