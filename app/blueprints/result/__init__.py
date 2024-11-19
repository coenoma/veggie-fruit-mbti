from flask import Blueprint

bp = Blueprint('result', __name__)

from app.blueprints.result import routes
