from flask import Blueprint
from library.books.services import (add_book_service, get_book_by_id_service, 
                                    get_all_book_service, update_book_by_id_service, 
                                    delete_book_by_id_service, get_books_by_author_name_service)

books = Blueprint("books", __name__)


# Add a new book
@books.route("/book-management/book", methods = ['POST'])
def add_book():
    return add_book_service()

# Get a book by id
@books.route("/book-management/book/<int:id>", methods = ['GET'])
def get_book_by_id(id):
    return get_book_by_id_service(id)

# Get all book
@books.route("/book-management/books", methods = ['GET'])
def get_all_books():
    return get_all_book_service()

# Update a book by id
@books.route("/book-management/book/<int:id>", methods = ['PUT'])
def update_book(id):
    return update_book_by_id_service(id)

# Delete a book by id
@books.route("/book-management/book/<int:id>", methods = ['DELETE'])
def delete_book_by_id(id):
    return delete_book_by_id_service(id)

# Get books by author name
@books.route("/book-management/book/<string:author>", methods = ['GET'])
def get_book_by_author_name(author):
    return get_books_by_author_name_service(author)