from flask_sqlalchemy import SQLAlchemy
import warnings

with warnings.catch_warnings():
     from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()