from library.extension import db
from library.library_ma import StudentSchema
from library.model import Students
from datetime import datetime
from flask import request, jsonify
import json

student_schema = StudentSchema()
students_schema = StudentSchema(many = True)

# Add a student
def add_student_service():
    data = request.json
    if data:
        if "name" in data and "birth_day" in data and "gender" in data and "class_name" in data:
            data['birth_day'] = datetime.strptime(data['birth_day'], '%d/%m/%Y').date()
            name = data["name"]
            birth_day = data["birth_day"]
            gender = data["gender"]
            class_name = data["class_name"]
        
        try:
            new_student = Students(name, birth_day, gender, class_name)
            db.session.add(new_student)
            db.session.commit()
            return jsonify({"message" : "Add Success!"}), 200
        except IndentationError:
            db.session.rollback()
            return jsonify({"message" : "Add Error!"}), 400
    else:
        return jsonify({"message" : "Request Error!"}), 400
    
# Get a student by id
def get_student_by_id_service(id):
    student = Students.query.get(id)
    if student:
        return student_schema.jsonify(student)
    else:
        return jsonify({'message': "Not Found!"}), 400
    
# Get all students
def get_all_students_service():
    students = Students.query.all()
    if students:
        return students_schema.jsonify(students)
    else:
        return jsonify({'message': "Not Found!"}), 400
    
# Update student by id
def update_student_by_id_service(id):
    student = Students.query.get(id)
    data = request.json
    if student:
        try:
            if "name" in data:
                student.name = data['name']
            if "birth_day" in data:
                data['birth_day'] = datetime.strptime(data['birth_day'], "%d/%m/%Y").date()
                student.name = data['birth_day']
            if "gender" in data:
                student.name = data['gender']
            if "class_name" in data:
                student.name = data['class_name']
            db.session.commit()
            return jsonify({"message": "Student Updated!"}), 200
        except IndentationError:
            return jsonify({"message": "Update Error!"}), 400
    else:
        return jsonify({"message": "Not Found!"}), 404
    
# Delete a student by id
def delete_student_by_id_service(id):
    student = Students.query.get(id)
    if student:
        try:
            db.session.delete(student)
            db.session.commit()
            return jsonify({"message": "Student Deleted"}), 200
        except IndentationError:
            return jsonify({"message": "Can Not Delete This Student!"}), 400
    else:
        return jsonify({"message": "Not Found"}), 404
