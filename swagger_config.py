
from flasgger import Swagger
from flask import Flask

def configure_swagger(app):
    app.config['SWAGGER'] = {
        'title': 'Factory Management System API',
        'uiversion': 3,
    }
    Swagger(app, template_file='swagger.yaml')
