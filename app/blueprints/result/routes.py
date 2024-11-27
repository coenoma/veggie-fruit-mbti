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
        
        # Group questions and answers by type with validation
        type_answers = {
            'EI': [],
            'SN': [],
            'TF': [],
            'JP': []
        }
        
        for i, answer in enumerate(answers):
            q_type = questions[i].get('type')
            if not q_type:
                app.logger.error(f'Question {i} has no type defined')
                continue
            if answer not in ['A', 'B']:
                app.logger.error(f'Invalid answer format for question {i}: {answer}')
                continue
            type_answers[q_type].append(answer)
        
        # Validate minimum number of answers per type
        min_answers_required = 2  # 各タイプ最低2問は必要
        for q_type, answers_list in type_answers.items():
            if len(answers_list) < min_answers_required:
                flash(f'質問の回答が不足しています。もう一度診断を行ってください。', 'error')
                return redirect(url_for('quiz.quiz'))
        
        # Calculate weighted scores based on answer distribution
        scores = {}
        thresholds = {}
        
        for q_type, answers_list in type_answers.items():
            total_questions = len(answers_list)
            if total_questions == 0:
                continue
                
            # Calculate score as a percentage
            a_answers = sum(1 for ans in answers_list if ans == 'A')
            score_percentage = (a_answers / total_questions) * 100
            scores[q_type] = score_percentage
            
            # Dynamic threshold based on question count
            # より多くの質問がある場合、判定の信頼性が高まるため、閾値を調整
            base_threshold = 50  # 基準は50%
            question_weight = min(1.0, total_questions / 8)  # 最大8問まで重みを考慮
            thresholds[q_type] = base_threshold * question_weight
        
        # スコアと閾値を比較してMBTIタイプを決定
        mbti_type = ''
        
        # 各次元でのスコアの確信度を計算
        confidence_scores = {}
        for dimension, score in scores.items():
            confidence = abs(score - 50) / 50  # 50%からの距離を確信度とする
            confidence_scores[dimension] = confidence
        
        # スコアと閾値を比較し、確信度も考慮してタイプを決定
        mbti_type += 'E' if scores['EI'] >= thresholds['EI'] else 'I'
        mbti_type += 'S' if scores['SN'] >= thresholds['SN'] else 'N'
        mbti_type += 'T' if scores['TF'] >= thresholds['TF'] else 'F'
        mbti_type += 'J' if scores['JP'] >= thresholds['JP'] else 'P'
        
        # 計算過程をログに記録
        app.logger.info(f'MBTI Calculation - Scores: {scores}')
        app.logger.info(f'MBTI Calculation - Thresholds: {thresholds}')
        app.logger.info(f'MBTI Calculation - Confidence: {confidence_scores}')
        app.logger.info(f'MBTI Result: {mbti_type}')

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
