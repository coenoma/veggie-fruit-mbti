from flask import Blueprint

bp = Blueprint('quiz', __name__, url_prefix='/quiz')

from app.blueprints.quiz import routes
