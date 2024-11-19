import os
from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from mbti_data import personality_types, questions

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY") or "a secret key"
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///mbti.db")
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    session['answers'] = []
    return render_template('quiz.html', questions=questions)

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    answer = request.json.get('answer')
    session['answers'] = session.get('answers', []) + [answer]
    return jsonify({'success': True})

@app.route('/result')
def result():
    answers = session.get('answers', [])
    if len(answers) < len(questions):
        return redirect(url_for('quiz'))
    
    # Calculate MBTI type
    e_score = sum(1 for i, ans in enumerate(answers) if i % 4 == 0 and ans == 'A')
    s_score = sum(1 for i, ans in enumerate(answers) if i % 4 == 1 and ans == 'A')
    t_score = sum(1 for i, ans in enumerate(answers) if i % 4 == 2 and ans == 'A')
    j_score = sum(1 for i, ans in enumerate(answers) if i % 4 == 3 and ans == 'A')

    mbti_type = ''
    mbti_type += 'E' if e_score >= 3 else 'I'
    mbti_type += 'S' if s_score >= 3 else 'N'
    mbti_type += 'T' if t_score >= 3 else 'F'
    mbti_type += 'J' if j_score >= 3 else 'P'

    personality = personality_types.get(mbti_type, {
        'fruit': '不明',
        'description': '申し訳ありません。結果を計算できませんでした。',
        'color': '#f97316'  # primary-500のオレンジ
    })
    
    return render_template('result.html', 
                         mbti_type=mbti_type,
                         personality=personality)

with app.app_context():
    import models
    db.create_all()
