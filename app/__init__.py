from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
import os

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

def create_app(config_object=None):
    app = Flask(__name__)
    
    # Default configuration
    app.secret_key = os.environ.get("FLASK_SECRET_KEY") or "a secret key"
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///mbti.db")
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
        "pool_recycle": 300,
        "pool_pre_ping": True,
    }
    
    # Override with specific configuration if provided
    if config_object:
        app.config.from_object(config_object)
    
    db.init_app(app)
    
    # Register blueprints
    from app.routes import bp as main_bp
    from app.blueprints.quiz import bp as quiz_bp
    from app.blueprints.result import bp as result_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(quiz_bp)
    app.register_blueprint(result_bp)
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    return app
