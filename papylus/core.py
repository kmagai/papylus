import os
from papylus import app

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ['DATABASE_URL'] or 'sqlite:///' + os.path.join(basedir, 'app.db')

db = SQLAlchemy(app)
api_manager = APIManager(app, flask_sqlalchemy_db=db)
