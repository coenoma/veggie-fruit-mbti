from flask import render_template, request, jsonify, session
from app.blueprints.quiz import bp
from app.mbti_data import questions

@bp.route('/quiz')
def quiz():
    session['answers'] = []
    return render_template('quiz.html', questions=questions)

@bp.route('/submit_answer', methods=['POST'])
def submit_answer():
    answer = request.json.get('answer')
    session['answers'] = session.get('answers', []) + [answer]
    return jsonify({'success': True})
