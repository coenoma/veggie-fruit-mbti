from flask import render_template, session, redirect, url_for, flash, current_app as app
from app.blueprints.result import bp
from app.mbti_data import personality_types

@bp.route('/result')
def result():
    try:
        answers = session.get('answers', [])
        if not answers:
            flash('診断を最初からやり直してください。', 'error')
            return redirect(url_for('quiz.quiz'))
        
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
            'color': '#f97316'
        })
        
        # セッションをクリア
        session.pop('answers', None)
        
        return render_template('result.html', 
                           mbti_type=mbti_type,
                           personality=personality,
                           personality_types=personality_types)
                           
    except Exception as e:
        app.logger.error(f'Result calculation error: {str(e)}')
        flash('エラーが発生しました。もう一度お試しください。', 'error')
        return redirect(url_for('quiz.quiz'))

@bp.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@bp.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500
