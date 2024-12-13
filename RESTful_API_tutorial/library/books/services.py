from library.extension import db
from library.library_ma import BookSchema
from library.model import Books, Author
from flask import request, jsonify
from sqlalchemy import func
import json

book_schema = BookSchema()
books_schema = BookSchema(many = True)

# Add a book
def add_book_service():
    data = request.json
    if (data and ('name' in data) and ('page_count' in data) and ('author_id' in data) and ('category_id' in data)):
        name = data['name']
        page_count = data['page_count']
        author_id = data['author_id']
        category_id = data['category_id']

        try:
            new_book = Books(name, page_count, author_id, category_id)
            db.session.add(new_book)
            db.session.commit()
            return jsonify({"message": "Add Success!"}), 200
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Can Not Add Book!"}), 400
    else:
        return jsonify({"message": "Request Error!"}), 400
    
# Get a book by id
def get_book_by_id_service(id):
    book = Books.query.get(id)
    if book:
        return book_schema.jsonify(book)
    else:
        return jsonify({"message": "Not Found Book!"}), 404
    
# Get all books
def get_all_book_service():
    books = Books.query.all()
    if books:
        return books_schema.jsonify(books)
    else:
        return jsonify({"message": "Not Found Book!"}), 404
    
# Update a book by id
def update_book_by_id_service(id):
    book = Books.query.get(id)
    data = request.json
    if book:
        if data:
            try:
                if "author_id" in data:
                    book.author_id = data["author_id"]
                if "category_id" in data:
                    book.category_id = data["category_id"]
                if "page_count" in data:
                    book.page_count = data["page_count"]
                if "name" in data:
                    book.name = data["name"]
                db.session.commit()
                return jsonify({"message": "Book Updated!"}), 200
            except IndentationError:
                db.session.rollback()
                return jsonify({"message": "Update Failed!"}), 400
    else:
        return jsonify({"message": "Not Found Book!"}), 404

# Delete a book by id
def delete_book_by_id_service(id):
    book = Books.query.get(id)
    if book:
        try:
            db.session.delete(book)
            db.session.commit()
            return jsonify({"message": "Book Deleted!"}), 200
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Can not deleted book!"}), 400
    else:
        return jsonify({"message": "Not Found Book!"}), 404
    

# Get books by author name
def get_books_by_author_name_service(author):
    books = Books.query.join(Author).filter(func.lower(Author.name) == author.lower())
    if books:
        return books_schema.jsonify(books)
    else:
        return jsonify({"message": "Not Found Book!"}), 404