from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS
import os

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    # Additional quiz-specific config
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'redcharger-dev-secret-2024')
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['PERMANENT_SESSION_LIFETIME'] = 1800  # 30 minutes
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB
    
    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    CORS(app)  # Enable CORS if needed
    
    # Register blueprints
    from app.routes.auth import auth_bp
    from app.routes.courses import courses_bp
    from app.routes.resources import resources_bp
    from app.routes.quizzes import quizzes_bp
    
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(courses_bp)
    app.register_blueprint(resources_bp)
    app.register_blueprint(quizzes_bp, url_prefix='/quizzes')
   
    
    # Create tables
    with app.app_context():
        db.create_all()
    
    return app