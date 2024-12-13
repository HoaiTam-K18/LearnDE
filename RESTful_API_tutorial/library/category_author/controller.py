from flask import Blueprint
from .services import (add_author_service, add_category_service,
                       get_author_by_id_service, get_category_by_id_service,
                       get_all_authors_service, get_all_categories_service,
                       update_author_by_id_service, update_category_by_id_service,
                       delete_author_by_id_service, delete_category_by_id_service)

category_author = Blueprint("category_author", __name__)

# Add a author
@category_author.route("/category-author-management/author", methods = ['POST'])
def add_author():
    return add_author_service()

# Add a category
@category_author.route("/category-author-management/category", methods = ['POST'])
def add_category():
    return add_category_service()

# Get a author by id
@category_author.route("/category-author-management/author/<int:id>", methods = ['GET'])
def get_author_by_id(id):
    return get_author_by_id_service(id)

# Get a category by id
@category_author.route("/category-author-management/category/<int:id>", methods = ['GET'])
def get_category_by_id(id):
    return get_category_by_id_service(id)

# Get all authors
@category_author.route("/category-author-management/authors", methods = ['GET'])
def get_all_authors():
    return get_all_authors_service()

# Get all categories
@category_author.route("/category-author-management/categories", methods = ['GET'])
def get_all_categories():
    return get_all_categories_service()\
    
# Update author by id
@category_author.route("/category-author-management/author/<int:id>", methods = ['PUT'])
def update_author_by_id(id):
    return update_author_by_id_service(id)

# Update category by id
@category_author.route("/category-author-management/category/<int:id>", methods = ['PUT'])
def update_category_by_id(id):
    return update_category_by_id_service(id)

# Delete author by id
@category_author.route("/category-author-management/author/<int:id>", methods = ['DELETE'])
def delete_author_by_id(id):
    return delete_author_by_id_service(id)

# Delete category by id
@category_author.route("/category-author-management/category/<int:id>", methods = ['DELETE'])
def delete_category_by_id(id):
    return delete_category_by_id_service(id)