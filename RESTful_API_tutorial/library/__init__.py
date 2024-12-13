from flask import Flask, request, Blueprint
from .books.controller import books
from .borrow.controller import borrow
from .students.controller import students
from .category_author.controller import category_author
from .extension import db, ma
import os

def create_db(app):
    if not os.path.exists('instance/library.db'):
        from . import model
        with app.app_context():
            db.create_all()
        print("Created DB!")
        return app

def create_app(config_file = "config.py"):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    db.init_app(app)
    ma.init_app(app)
    create_db(app)
    app.register_blueprint(books)
    app.register_blueprint(borrow)
    app.register_blueprint(students)
    app.register_blueprint(category_author)
    return app
