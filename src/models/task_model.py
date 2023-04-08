from src.connections.db import db


class TaskModel(db.Model):
    __tablename__ = "task"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    is_active = db.Column(db.Boolean, nullable=True)
    expected_time = db.Column(db.Float,nullable=True)
    time_finished = db.Column(db.Float, nullable=True)
    # Enl_ace entre dos tablas -> 1 a muchos one-to-many
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), unique=False, nullable=False)
    category = db.relationship("CategoryModel", back_populates="tasks")

