import os
from flask import Flask
from flask_cors import CORS, cross_origin
from werkzeug.security import generate_password_hash, check_password_hash

## REST API
from flask_restful import Resource, Api




app = Flask(__name__)

# app.config['SECRET_KEY'] = 'mysecretkey'
# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')   
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False   
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)

# from todoApp.core.routes import core
# from todoApp.users.routes import users
# from todoApp.todos.routes import todos

# app.register_blueprint(core)
# app.register_blueprint(users)
# app.register_blueprint(todos)

from guhitApp import rest
