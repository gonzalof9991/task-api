"""
Blueprint en Flask Smallest se utiliza para dividir una API en multiples segmentos
"""
from flask import abort
from flask.views import MethodView
from flask_smorest import Blueprint
from sqlalchemy.exc import SQLAlchemyError

from src.connections.db import db
from src.models.task_model import TaskModel

from src.request.squemas import TaskSchema

blp = Blueprint("Tasks", "task", description="Operations on items")

"""
MethodView -> Podemos crear una clase cuyos métodos se dirijan a un punto final específico.
"""


@blp.route("/tasks")
class Task(MethodView):
    @blp.response(200, TaskSchema(many=True))
    def get(self):
        return TaskModel.query.all()


@blp.route("/task")
class TaskList(MethodView):
    # Decorador para Schema
    @blp.arguments(TaskSchema)
    @blp.response(201, TaskSchema)
    def post(self, task_data):
        print(task_data)
        task = TaskModel(**task_data)
        try:
            db.session.add(task)
            db.session.commit()
        except SQLAlchemyError:
            return ''
            abort(500, message="An error ocurred whilte inserting the task.")
        return task
