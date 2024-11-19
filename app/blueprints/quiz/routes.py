from flask import render_template, request, jsonify, session
from app.blueprints.quiz import bp
from app.mbti_data import questions

@bp.route('/')
def quiz():
    session['answers'] = []
    return render_template('quiz.html', questions=questions)

@bp.route('/submit_answer', methods=['POST'])
def submit_answer():
    try:
        answer = request.json.get('answer')
        if not answer:
            return jsonify({'error': '回答が見つかりません'}), 400
            
        session['answers'] = session.get('answers', []) + [answer]
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
