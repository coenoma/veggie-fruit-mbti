import os

class Config:
    SECRET_KEY = os.environ.get("FLASK_SECRET_KEY") or "a secret key"
