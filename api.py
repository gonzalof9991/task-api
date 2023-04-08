import os

from flask import Flask
from flask_smorest import Api

# Importamos las rutas
from src.routes.task_routes import blp as TaskBlueprint
from src.routes.category_routes import blp as CategoryBlueprint
# Import BD
from src.connections.db import db
from flask_migrate import Migrate
import src.models

app = Flask(__name__)
# Configuración de Flask
app.config["API_TITLE"] = "Tasks REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
# Configuración DB -> SQLITE
#app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///data.db")
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/task-bd'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config['SECRET_KEY'] = 'secret!'
db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)

# Crear todas las tablas de la bd antes de la consulta
@app.before_first_request
def create_tables():
    db.create_all()


# Registramos las rutas
api.register_blueprint(TaskBlueprint)
api.register_blueprint(CategoryBlueprint)

if __name__ == '__main__':
    app.run()
