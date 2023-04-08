"""
Blueprint en Flask Smallest se utiliza para dividir una API en multiples segmentos
"""
from flask import abort
from flask.views import MethodView
from flask_smorest import Blueprint
from sqlalchemy.exc import SQLAlchemyError

from src.connections.db import db

from src.request.squemas import CategorySchema

from src.models.category_model import CategoryModel

blp = Blueprint("Categories", "category", description="Operations on Categories")

"""
MethodView -> Podemos crear una clase cuyos métodos se dirijan a un punto final específico.
"""


@blp.route("/categories")
class Category(MethodView):
    @blp.response(200, CategorySchema(many=True))
    def get(self):
        return CategoryModel.query.all()


@blp.route("/category")
class CategoryList(MethodView):
    @blp.arguments(CategorySchema)
    @blp.response(201, CategorySchema)
    def post(self, category_data):
        print(category_data)
        category = CategoryModel(**category_data)
        try:
            db.session.add(category)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error ocurred whilte inserting the task.")
        return category
