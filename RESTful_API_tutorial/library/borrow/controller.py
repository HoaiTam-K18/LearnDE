from flask import Blueprint
from library.borrow.services import (add_borrow_service, get_borrow_by_id_service, 
                                     get_all_borrows_service, update_borrow_by_id_service,
                                     delete_borrow_by_id_service,
                                     get_borrowed_books_by_student_name)

borrow = Blueprint("borrow", __name__)

# Add a new borrow
@borrow.route("/borrow-management/borrow", methods = ['POST'])
def add_borrow():
    return add_borrow_service()

# Get a borrow by id
@borrow.route("/borrow-management/borrow/<int:id>", methods = ['GET'])
def get_borrow_by_id(id):
    return get_borrow_by_id_service(id)

# Get all borrow
@borrow.route("/borrow-management/borrows", methods = ['GET'])
def get_all_borrow():
    return get_all_borrows_service()

# Update a borrow by id
@borrow.route("/borrow-management/borrow/<int:id>", methods = ['PUT'])
def update_borrow_by_id(id):
    return update_borrow_by_id_service(id)
    
# Delete a borrow by id
@borrow.route("/borrow-management/borrow/<int:id>", methods = ['DELETE'])
def delete_borrow_by_id(id):
    return delete_borrow_by_id_service(id)

# Get borrow_id, book_name, category_name, author_name by student_name
@borrow.route("/borrow-management/borrow/<string:student_name>", methods = ['GET'])
def get_borrow_book_category_author_by_student_name(student_name):
    return get_borrowed_books_by_student_name(student_name)