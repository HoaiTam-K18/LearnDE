from library.extension import db
from library.library_ma import AuthorSchema, CategorySchema
from library.model import Author, Category
from flask import jsonify, request
import json

author_schema = AuthorSchema()
authors_schema = AuthorSchema(many = True)

category_schema = CategorySchema()
categories_schema = CategorySchema(many = True)


# Add a author
def add_author_service():
    data = request.json
    if data and "name" in data:
        name = data['name']
    
        try:
            new_author = Author(name)
            db.session.add(new_author)
            db.session.commit()
            return jsonify({"message": "Add Success!"}), 200
        except IndentationError:
            return jsonify({"message" : "Can Not Add"}), 400
    else:
        return jsonify({"message" : "Request Error!"}), 404


# Add a category
def add_category_service():
    data = request.json
    if data and "name" in data:
        name = data['name']
    
        try:
            new_category = Category(name)
            db.session.add(new_category)
            db.session.commit()
            return jsonify({"message": "Add Success!"}), 200
        except IndentationError:
            return jsonify({"message" : "Can Not Add"}), 400
    else:
        return jsonify({"message" : "Request Error!"}), 404
    
# Get author by id
def get_author_by_id_service(id):
    author = Author.query.get(id)
    if author:
        return author_schema.jsonify(author)
    else:
        return jsonify({"message": "Not Found!"}), 400

# Get author by id
def get_category_by_id_service(id):
    category = Category.query.get(id)
    if category:
        return category_schema.jsonify(category)
    else:
        return jsonify({"message": "Not Found!"}), 400


# Get all authors
def get_all_authors_service():
    authors = Author.query.all()
    if authors:
        return authors_schema.jsonify(authors)
    else:
        return jsonify({"message": "Not Found!"}), 400
    

# Get all categories
def get_all_categories_service():
    categories = Category.query.all()
    if categories:
        return categories_schema.jsonify(categories)
    else:
        return jsonify({"message": "Not Found!"}), 400

# Update author by id
def update_author_by_id_service(id):
    author = Author.query.get(id)
    data = request.json
    if data:
        if "name" in data:
            author.name = data['name']
            db.session.commit()
            return jsonify({"message": "Author Updated!"}), 200
        else:
            return jsonify({"message": "Can Not Update This Author"}), 400
    else:
        return jsonify({"message": "Not Found"}), 404
    
# Update category by id
def update_category_by_id_service(id):
    category = Category.query.get(id)
    data = request.json
    if data:
        if "name" in data:
            category.name = data['name']
            db.session.commit()
            return jsonify({"message": "Category Updated!"}), 200
        else:
            return jsonify({"message": "Can Not Update This Category"}), 400
    else:
        return jsonify({"message": "Not Found"}), 404
    

# Delete author by id
def delete_author_by_id_service(id):
    author = Author.query.get(id)
    if author:
        try:
            db.session.delete(author)
            db.session.commit()
            return jsonify({"message": "Author Deleted!"}), 200
        except IndentationError:
            return jsonify({"message": "Can Not Delete This Author!"}), 400
    else:
        return jsonify({"message": "Not Found"}), 404
    

# Delete category by id
def delete_category_by_id_service(id):
    category = Category.query.get(id)
    if category:
        try:
            db.session.delete(category)
            db.session.commit()
            return jsonify({"message": "Category Deleted!"}), 200
        except IndentationError:
            return jsonify({"message": "Can Not Delete This Category!"}), 400
    else:
        return jsonify({"message": "Not Found"}), 404