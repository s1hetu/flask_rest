from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import app_config
from flask import Flask
import os
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
migrate = Migrate()
marshmallow = Marshmallow()
jwt = JWTManager()

def create_app(env_name=os.environ.get('env', 'dev')):
    app = Flask(__name__)
    app.config.from_object(app_config[env_name])
    db.init_app(app)
    migrate.init_app(app, db)
    marshmallow.init_app(app)
    jwt.init_app(app)
    with app.app_context():
        from QA.User.routes import user_blueprint
        from QA.Question.routes import question_blueprint
        app.register_blueprint(user_blueprint, url_prefix="/user")
        app.register_blueprint(question_blueprint)

        db.create_all()

        return app
