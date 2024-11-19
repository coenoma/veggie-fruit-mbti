from flask import Blueprint

bp = Blueprint('quiz', __name__)

from app.blueprints.quiz import routes
