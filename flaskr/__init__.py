from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app(config_class='flaskr.config.Config'):
    app = Flask(__name__, instance_relative_config=True)
    
    app.config.from_object(config_class)
    app.config.from_pyfile('config.py', silent=True)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    with app.app_context():
        db.create_all()  
   
    from .auth import auth_bp
    from .projects import projects_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(projects_bp)

    return app
