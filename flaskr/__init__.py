from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_talisman import Talisman
from dotenv import load_dotenv

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
bcrypt = Bcrypt()

def create_app(config_class='flaskr.config.Config'):
    app = Flask(__name__, instance_relative_config=True)    
    
    app.config.from_object(config_class)
    app.config.from_pyfile('config.py', silent=True)

    cors = CORS(app, resources={r"/api/*": {"origins": app.config['ALLOWED_ORIGINS']}},
            supports_credentials=True,
            methods=["GET", "POST", "PUT", "DELETE"],
            allow_headers=["Content-Type", "Authorization"])

    if app.config.get('TALISMAN_ENABLED', True):
        Talisman(app, content_security_policy=app.config['CSP'])           

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    bcrypt.init_app(app)

    with app.app_context():
        from . import auth, models
        db.create_all() 
   
    from .auth import auth_bp
    from .projects import projects_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(projects_bp)

    return app
