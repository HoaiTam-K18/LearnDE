from .extension import db

class Students(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    birth_day = db.Column(db.Date)
    gender = db.Column(db.String(10))
    class_name = db.Column(db.String(10))

    def __init__(self, name, birth_day, gender, class_name):
        self.name = name
        self.birth_day = birth_day
        self.gender = gender
        self.class_name = class_name
        

class Books(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    page_count = db.Column(db.Integer)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    def __init__(self, name, page_count, author_id, category_id):
        self.name = name
        self.page_count = page_count
        self.author_id = author_id
        self.category_id = category_id


class Borrow(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    borrow_date = db.Column(db.Date)
    return_date = db.Column(db.Date)

    def __init__(self, book_id, student_id, borrow_date, return_date):
        self.book_id = book_id
        self.student_id = student_id
        self.borrow_date = borrow_date
        self.return_date = return_date


class Category(db.Model):
    id  = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)

    def __init__(self, name):
        self.name = name


class Author(db.Model):
    id  = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)

    def __init__(self, name):
        self.name = name