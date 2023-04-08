from src.connections.db import db


class CategoryModel(db.Model):
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(200), nullable=True)
    is_active = db.Column(db.Boolean, nullable=True)
    tasks = db.relationship("TaskModel", back_populates="category", lazy="dynamic")
