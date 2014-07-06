import os
from papylus import app

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager

basedir = os.path.abspath(os.path.dirname(__file__))

try:
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ['DATABASE_URL']
except:
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'app.db')

db = SQLAlchemy(app)
api_manager = APIManager(app, flask_sqlalchemy_db=db)
