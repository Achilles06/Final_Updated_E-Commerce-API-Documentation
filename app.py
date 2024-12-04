from flask import Flask
from swagger_config import configure_swagger
from flask_sqlalchemy import SQLAlchemy
from swagger_config import configure_swagger
from flask_limiter import Limiter
from swagger_config import configure_swagger
from flask_limiter.util import get_remote_address
from swagger_config import configure_swagger
from models import db
from blueprints.employee import employee_bp
from blueprints.products import product_bp
from blueprints.order import order_bp
from blueprints.customer import customer_bp
from blueprints.production import production_bp

# Initialize Limiter
limiter = Limiter(key_func=get_remote_address)

def create_app():
    app = Flask(__name__)

from blueprints.production import production_blueprint
from blueprints.employee import employee_blueprint

app.register_blueprint(production_blueprint)
app.register_blueprint(employee_blueprint)

from blueprints.customers import customers_blueprint

app.register_blueprint(customers_blueprint)

from blueprints.products import products_blueprint
from blueprints.orders import orders_blueprint

app.register_blueprint(products_blueprint)
app.register_blueprint(orders_blueprint)
    configure_swagger(app)
    
    # Configuration settings
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/factory.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    limiter.init_app(app)

    # Register Blueprints
    app.register_blueprint(employee_bp, url_prefix='/employees')
    app.register_blueprint(product_bp, url_prefix='/products')
    app.register_blueprint(order_bp, url_prefix='/orders')
    app.register_blueprint(customer_bp, url_prefix='/customers')
    app.register_blueprint(production_bp, url_prefix='/production')

    return app


from flask_swagger_ui import get_swaggerui_blueprint

# Swagger configuration
SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI
API_URL = '/static/swagger.yaml'  # Path to the Swagger YAML file

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "E-Commerce API"
    }
)

# Register the blueprint
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

from flask_swagger_ui import get_swaggerui_blueprint

# Swagger configuration
SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI
API_URL = '/static/swagger.yaml'  # Path to the Swagger YAML file

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "E-Commerce API"
    }
)

# Register the blueprint
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
