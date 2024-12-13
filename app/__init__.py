from flask import Flask
import os

def create_app(config_object=None):
    app = Flask(__name__)
    
    # Default configuration
    app.secret_key = os.environ.get("FLASK_SECRET_KEY") or "a secret key"
    
    # Override with specific configuration if provided
    if config_object:
        app.config.from_object(config_object)
    
    # Register blueprints
    from app.routes import bp as main_bp
    from app.blueprints.quiz import bp as quiz_bp
    from app.blueprints.result import bp as result_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(quiz_bp)
    app.register_blueprint(result_bp)
    
    return app
