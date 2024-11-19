from app import db
from datetime import datetime

class TestResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mbti_type = db.Column(db.String(4), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
