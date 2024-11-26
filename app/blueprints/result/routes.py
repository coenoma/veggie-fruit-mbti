from flask import render_template, session, redirect, url_for, flash, current_app as app
from app.blueprints.result import bp
from app.mbti_data import personality_types, questions

@bp.route('/result')
def result():
    try:
        answers = session.get('answers', [])
        if not answers or len(answers) != len(questions):
            flash('診断を最初からやり直してください。', 'error')
            return redirect(url_for('quiz.quiz'))
        
        # Group questions and answers by type
        type_answers = {
            'EI': [],
            'SN': [],
            'TF': [],
            'JP': []
        }
        
        for i, answer in enumerate(answers):
            q_type = questions[i].get('type')
            if q_type:
                type_answers[q_type].append(answer)
        
        # Calculate scores based on proportion for each dimension
        scores = {
            'EI': sum(1 for ans in type_answers['EI'] if ans == 'A'),
            'SN': sum(1 for ans in type_answers['SN'] if ans == 'A'),
            'TF': sum(1 for ans in type_answers['TF'] if ans == 'A'),
            'JP': sum(1 for ans in type_answers['JP'] if ans == 'A')
        }
        
        # 各タイプの質問数に基づいて判定基準を設定
        thresholds = {
            'EI': len(type_answers['EI']) / 2,
            'SN': len(type_answers['SN']) / 2,
            'TF': len(type_answers['TF']) / 2,
            'JP': len(type_answers['JP']) / 2
        }
        
        # スコアと閾値を比較してMBTIタイプを決定
        mbti_type = ''
        mbti_type += 'E' if scores['EI'] >= thresholds['EI'] else 'I'
        mbti_type += 'S' if scores['SN'] >= thresholds['SN'] else 'N'
        mbti_type += 'T' if scores['TF'] >= thresholds['TF'] else 'F'
        mbti_type += 'J' if scores['JP'] >= thresholds['JP'] else 'P'

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
