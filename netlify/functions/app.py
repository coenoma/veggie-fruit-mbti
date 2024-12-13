import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from flask import Flask
from flask.helpers import send_from_directory
from netlify_lambda_wsgi import make_handler

# あなたのFlaskアプリケーションをインポート
from app import app

# 静的ファイルの提供
@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

# Netlify Functions用のハンドラー作成
wsgi_handler = make_handler(app)

def handler(event, context):
    return wsgi_handler(event, context)