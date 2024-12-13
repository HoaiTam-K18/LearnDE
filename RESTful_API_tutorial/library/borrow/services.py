from library.extension import db
from library.library_ma import BorrowSchema
from library.model import Borrow, Books, Students, Category, Author
from flask import request, jsonify
from datetime import datetime
from sqlalchemy import func
import json

borrow_schema = BorrowSchema()
borrows_schema = BorrowSchema(many = True)

# Add a borrow
def add_borrow_service():
    data = request.json
    if data and ("book_id" in data ) and ("student_id" in data ) and ("borrow_date" in data ) and ("return_date" in data):
        data['borrow_date'] = datetime.strptime(data['borrow_date'], '%d/%m/%Y').date()
        data['return_date'] = datetime.strptime(data['return_date'], '%d/%m/%Y').date()
        book_id = data["book_id"]
        student_id = data["student_id"]
        borrow_date = data["borrow_date"]
        return_date = data["return_date"]
        
        try:
            new_borrow = Borrow(book_id, student_id, borrow_date, return_date)
            db.session.add(new_borrow)
            db.session.commit()
            return jsonify({"message" : "Add Success!"}), 200
        except IndentationError:
            db.session.rollback()
            return jsonify({"message" : "Add Error!"}), 400
    else:
        return jsonify({"message" : "Request Error!"}), 404
    
# Get a borrow by id
def get_borrow_by_id_service(id):
    borrow = Borrow.query.get(id)
    if borrow:
        return borrow_schema.jsonify(borrow)
    else:
        return jsonify({"message": "Not Found Book!"}), 404
    
# Get all borrows
def get_all_borrows_service():
    borrows = Borrow.query.all()
    if borrows:
        return borrows_schema.jsonify(borrows)
    else:
        return jsonify({"message": "Not Found Book!"}), 404
    

# Update a borrow by id
def update_borrow_by_id_service(id):
    borrow = Borrow.query.get(id)
    data = request.json
    if borrow:
        try:
            if "book_id" in data:
                borrow.book_id = data['book_id']
            if "student_id" in data:
                borrow.student_id = data['student_id']
            if "borrow_date" in data:
                data['borrow_date'] = datetime.strptime(data['borrow_date'], '%d/%m/%Y').date()
                borrow.borrow_date = data['borrow_date']
            if "return_date" in data:
                data['return_date'] = datetime.strptime(data['return_date'], '%d/%m/%Y').date()
                borrow.return_date = data['return_date']
            db.session.commit()
            return jsonify({"message": "Borrow Updated!"}), 200
        except IndentationError:
            db.session.rollback()
            return jsonify({'message': "Update Error!"}), 400
    else:
        return jsonify({'message': "Not Found!"}), 404


# Delete a borrow by id 
def delete_borrow_by_id_service(id):
    borrow = Borrow.query.get(id)
    if borrow:
        try:
            db.session.delete(borrow)
            db.session.commit()
            return jsonify({'message': "Borrow Deleted!"}), 200
        except IndentationError:
            return jsonify({'message': "Delete Error!"}), 400
    else:
        return jsonify({'message': "Not Found!"}), 404
    

# Get borrow_id, book_name, category_name, author_name by student_name
def get_borrowed_books_by_student_name(student_name):
    try:
        # Query to fetch borrowed book details
        borrows = (
            db.session.query(
                Borrow.id, 
                Books.name.label("book_name"), 
                Category.name.label("category_name"), 
                Author.name.label("author_name")
            )
            .join(Books, Books.id == Borrow.book_id)
            .join(Category, Category.id == Books.category_id)
            .join(Author, Author.id == Books.author_id)
            .join(Students, Students.id == Borrow.student_id)
            .filter(func.lower(Students.name) == student_name.lower())
            .all()
        )
        
        # Check if results are found
        if borrows:
            borrow_list = [
                {
                    "borrow_id": borrow[0],
                    "book_name": borrow[1],
                    "category_name": borrow[2],
                    "author_name": borrow[3],
                }
                for borrow in borrows
            ]
            return jsonify({f"{student_name} borrowed": borrow_list}), 200
        else:
            return jsonify({"message": "Not Found"}), 404
    
    except Exception as e:
        # Log the exception if necessary
        return jsonify({"error": "An error occurred", "details": str(e)}), 500