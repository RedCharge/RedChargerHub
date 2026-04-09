from flask import Blueprint, render_template, request, flash, jsonify, session, redirect, url_for
from flask_login import login_required, current_user
from app.models import QuizAttempt, db
from difflib import SequenceMatcher
import re
from datetime import datetime
import importlib
import random
import traceback
import os
import sys
import json

quizzes_bp = Blueprint('quizzes', __name__)

# ==============================================
# QUIZ COURSE MAPPING
# ==============================================

QUIZ_COURSES = {
    'computer-organization': {
        'course_code': 'BCP 203',
        'name': 'Computer Organization Architecture',
        'image': 'https://images.unsplash.com/photo-1517077304055-6e89abbf09b0?ixlib=rb-4.0.3&auto=format&fit=crop&w=2069&q=80',
        'questions': 50,
        'duration': '60 minutes'
    },
    'logic-critical-thinking': {
        'course_code': 'ATU 203',
        'name': 'Logic and Critical Thinking',
        'image': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?ixlib=rb-4.0.3&auto=format&fit=crop&w=2070&q=80',
        'questions': 50,
        'duration': '60 minutes'
    },
    'data-communication': {
        'course_code': 'BCP 105',
        'name': 'Data Communication and Computer Networks',
        'image': 'https://images.unsplash.com/photo-1544197150-b99a580bb7a8?ixlib=rb-4.0.3&auto=format&fit=crop&w=2070&q=80',
        'questions': 50,
        'duration': '60 minutes'
    },
    'entrepreneurship': {
        'course_code': 'ATU 201',
        'name': 'Introduction to Principles of Entrepreneurship',
        'image': 'https://images.unsplash.com/photo-1552664730-d307ca884978?ixlib=rb-4.0.3&auto=format&fit=crop&w=2070&q=80',
        'questions': 50,
        'duration': '60 minutes'
    },
    'sustainability': {
        'course_code': 'BCB 209',
        'name': 'Principles and Applications in Sustainability',
        'image': 'https://images.unsplash.com/photo-1568992688065-536aad8a12f6?ixlib=rb-4.0.3&auto=format&fit=crop&w=2069&q=80',
        'questions': 50,
        'duration': '60 minutes'
    },
    'web-development': {
        'course_code': 'BCP 207',
        'name': 'Web Development Technologies',
        'image': 'https://images.unsplash.com/photo-1627398242454-45a1465c2479?ixlib=rb-4.0.3&auto=format&fit=crop&w=2074&q=80',
        'questions': 50,
        'duration': '60 minutes'
    },
    'cpp-programming': {
        'course_code': 'BCP 201',
        'name': 'Programming with C++',
        'image': 'https://images.unsplash.com/photo-1542831371-29b0f74f9713?ixlib=rb-4.0.3&auto=format&fit=crop&w=2070&q=80',
        'questions': 50,
        'duration': '60 minutes'
    }
}

# ==============================================
# HELPER FUNCTIONS
# ==============================================

def verify_written_answer(user_answer, correct_answer, keywords=None, min_similarity=0.6):
    """Verify written answer using multiple methods"""
    def clean_text(text):
        return re.sub(r'[^\w\s]', '', text.lower()).strip()
    
    user_clean = clean_text(user_answer)
    correct_clean = clean_text(correct_answer)
    
    similarity = SequenceMatcher(None, user_clean, correct_clean).ratio()
    
    keyword_score = 0
    found_keywords = []
    
    if keywords:
        for keyword in keywords:
            keyword_clean = clean_text(keyword)
            if keyword_clean in user_clean or any(word in user_clean for word in keyword_clean.split()):
                found_keywords.append(keyword)
                keyword_score += 1
        
        keyword_percentage = keyword_score / len(keywords)
    else:
        keyword_percentage = 0
    
    is_correct = similarity >= min_similarity or (keywords and keyword_percentage >= 0.5)
    
    return {
        'is_correct': is_correct,
        'similarity': similarity,
        'found_keywords': found_keywords,
        'keyword_score': keyword_score,
        'keyword_percentage': keyword_percentage if keywords else 0
    }

def calculate_grade(percentage):
    """Calculate grade based on percentage"""
    if percentage >= 90:
        return 'A+', 'Excellent!'
    elif percentage >= 80:
        return 'A', 'Very Good!'
    elif percentage >= 70:
        return 'B', 'Good!'
    elif percentage >= 60:
        return 'C', 'Satisfactory'
    elif percentage >= 50:
        return 'D', 'Pass'
    else:
        return 'F', 'Fail'

def load_quiz_data_from_module(quiz_slug):
    """Load quiz data from the course module"""
    try:
        print(f"Attempting to load quiz data for: {quiz_slug}")
        
        module_name = quiz_slug.replace('-', '_')
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        app_dir = os.path.dirname(current_dir)
        
        if app_dir not in sys.path:
            sys.path.insert(0, app_dir)
        
        try:
            module_path = f"app.courses.{module_name}"
            print(f"Trying import from: {module_path}")
            module = importlib.import_module(module_path)
            print(f"Successfully imported module: {module_path}")
            
        except ImportError as e:
            print(f"Failed to import {module_path}: {e}")
            module_file = f"{module_name}.py"
            current_files = os.listdir(current_dir)
            
            if module_file in current_files:
                module = importlib.import_module(module_name)
            else:
                parent_dir = os.path.dirname(current_dir)
                if module_file in parent_dir:
                    sys.path.insert(0, parent_dir)
                    module = importlib.import_module(module_name)
                else:
                    raise ImportError(f"Could not find module {module_name}")
        
        possible_names = [
            f"{module_name.upper()}_QUIZ",
            "QUIZ_DATA",
            "QUESTIONS",
            "QUIZ_QUESTIONS",
            "COURSE_QUESTIONS"
        ]
        
        quiz_data = None
        for name in possible_names:
            if hasattr(module, name):
                quiz_data = getattr(module, name)
                print(f"Found quiz data as '{name}' in module")
                break
        
        if quiz_data is None:
            for attr_name in dir(module):
                attr_value = getattr(module, attr_name)
                if isinstance(attr_value, dict) and 'questions' in attr_value:
                    quiz_data = attr_value
                    print(f"Found quiz data in attribute '{attr_name}'")
                    break
        
        if quiz_data is None:
            raise AttributeError(f"No quiz data found in module {module_name}")
        
        print(f"Successfully loaded quiz data with {len(quiz_data.get('questions', []))} questions")
        return quiz_data
        
    except Exception as e:
        print(f"Error loading quiz data for {quiz_slug}: {str(e)}")
        traceback.print_exc()
        return None

def get_course_questions_api(quiz_slug, count=20):
    """Get questions for a specific course"""
    try:
        quiz_data = load_quiz_data_from_module(quiz_slug)
        
        if not quiz_data:
            return {
                'success': False,
                'message': 'Could not load quiz data from module'
            }
        
        if 'questions' not in quiz_data:
            return {
                'success': False,
                'message': 'No questions found in quiz data'
            }
        
        all_questions = quiz_data['questions']
        
        if len(all_questions) < count:
            count = len(all_questions)
        
        if len(all_questions) > count:
            quiz_questions = random.sample(all_questions, count)
        else:
            quiz_questions = all_questions.copy()
        
        for question in quiz_questions:
            if 'options' in question and 'correct_answer' in question:
                try:
                    correct_index = question['correct_answer']
                    if isinstance(correct_index, int) and 0 <= correct_index < len(question['options']):
                        correct_answer_text = question['options'][correct_index]
                        random.shuffle(question['options'])
                        question['correct_answer'] = question['options'].index(correct_answer_text)
                except Exception as e:
                    print(f"Error shuffling options: {e}")
        
        return {
            'success': True,
            'questions': quiz_questions,
            'total_questions': len(all_questions),
            'quiz_count': len(quiz_questions),
            'course_code': quiz_data.get('course_code', QUIZ_COURSES.get(quiz_slug, {}).get('course_code', '')),
            'course_name': quiz_data.get('course_name', QUIZ_COURSES.get(quiz_slug, {}).get('name', '')),
            'passing_score': quiz_data.get('passing_score', 60)
        }
        
    except Exception as e:
        print(f"Error getting questions for {quiz_slug}: {str(e)}")
        traceback.print_exc()
        return {
            'success': False,
            'message': f'Error retrieving questions: {str(e)}'
        }

# ==============================================
# MAIN ROUTES
# ==============================================

@quizzes_bp.route('/')
@login_required
def index():
    return redirect(url_for('quizzes.quizzes'))

@quizzes_bp.route('/quiz-results')
@login_required
def quiz_results():
    return render_template('/quizzes/quiz_result.html')

@quizzes_bp.route('/quizzes')
@login_required
def quizzes():
    user_attempts = {}
    attempts = QuizAttempt.query.filter_by(user_id=current_user.id).all()
    for attempt in attempts:
        user_attempts[attempt.quiz_type] = {
            'score': attempt.score,
            'percentage': attempt.percentage,
            'grade': attempt.grade,
            'attempt_date': attempt.attempt_date.strftime('%Y-%m-%d'),
            'quiz_name': attempt.quiz_name
        }
    
    courses_data = []
    for slug, quiz_info in QUIZ_COURSES.items():
        course_info = {
            'slug': slug,
            'code': quiz_info['course_code'],
            'name': quiz_info['name'],
            'image': quiz_info['image'],
            'questions': quiz_info['questions'],
            'duration': quiz_info['duration'],
            'has_attempt': slug in user_attempts
        }
        
        if slug in user_attempts:
            course_info.update(user_attempts[slug])
        
        courses_data.append(course_info)
    
    total_courses = len(QUIZ_COURSES)
    total_questions = sum(quiz['questions'] for quiz in QUIZ_COURSES.values())
    
    return render_template('quizzes/quizzes.html', 
                         courses=courses_data,
                         total_courses=total_courses,
                         total_questions=total_questions)

@quizzes_bp.route('/take/<quiz_slug>')
@login_required
def take_quiz(quiz_slug):
    """Take an interactive quiz - supports cyclic mode"""
    print(f"take_quiz called with slug: {quiz_slug}")
    
    if quiz_slug not in QUIZ_COURSES:
        flash('Quiz not found', 'error')
        return redirect(url_for('quizzes.quizzes'))
    
    quiz_info = QUIZ_COURSES[quiz_slug]
    
    quiz_data = load_quiz_data_from_module(quiz_slug)
    
    if not quiz_data:
        flash('Could not load quiz questions from course module.', 'error')
        return redirect(url_for('quizzes.quizzes'))
    
    if 'passing_score' not in quiz_data:
        quiz_data['passing_score'] = 60
    
    if 'course_code' not in quiz_data:
        quiz_data['course_code'] = quiz_info['course_code']
    
    if 'course_name' not in quiz_data:
        quiz_data['course_name'] = quiz_info['name']
    
    questions = quiz_data.get('questions', [])
    total_questions = len(questions)
    mc_questions = len([q for q in questions if q.get('type') == 'multiple_choice'])
    written_questions = len([q for q in questions if q.get('type') == 'written'])
    
    last_attempt = QuizAttempt.query.filter_by(
        user_id=current_user.id, 
        quiz_type=quiz_slug
    ).order_by(QuizAttempt.attempt_date.desc()).first()
    
    # NEW: Initialize cyclic quiz session if not exists
    if f'cyclic_quiz_{quiz_slug}' not in session:
        # Select random questions for this session
        question_count = min(20, len(questions))
        if len(questions) > question_count:
            session_questions = random.sample(questions, question_count)
        else:
            session_questions = questions.copy()
        
        # Create pending queue (questions that need to be answered correctly)
        pending_questions = []
        for q in session_questions:
            pending_questions.append({
                'question_data': q,
                'attempts': 0,
                'last_answer': None
            })
        
        session[f'cyclic_quiz_{quiz_slug}'] = {
            'pending': pending_questions,
            'completed': [],
            'total_questions': len(session_questions),
            'original_questions': session_questions
        }
        session.modified = True
    
    return render_template('quizzes/quiz_template.html',
                         quiz_data=quiz_data,
                         quiz_info=quiz_info,
                         quiz_slug=quiz_slug,
                         course_name=quiz_info['name'],
                         course_code=quiz_info['course_code'],
                         quiz_type=quiz_slug,
                         total_questions=total_questions,
                         mc_questions=mc_questions,
                         written_questions=written_questions,
                         passing_score=quiz_data['passing_score'],
                         last_attempt=last_attempt,
                         cyclic_mode=True)  # Flag for frontend

# ==============================================
# CYCLIC QUIZ API (NEW)
# ==============================================

@quizzes_bp.route('/api/cyclic-submit', methods=['POST'])
@login_required
def cyclic_submit():
    """Submit one answer in cyclic mode - wrong answers go back to queue"""
    try:
        data = request.json
        quiz_slug = data.get('quiz_type')
        question_id = data.get('question_id')
        user_answer = data.get('user_answer', '')
        
        if not quiz_slug or question_id is None:
            return jsonify({'success': False, 'error': 'Missing required fields'}), 400
        
        # Get session data
        session_key = f'cyclic_quiz_{quiz_slug}'
        if session_key not in session:
            return jsonify({'success': False, 'error': 'Quiz session expired. Please restart.'}), 400
        
        quiz_session = session[session_key]
        pending = quiz_session.get('pending', [])
        
        # Find the question in pending queue
        question_index = None
        question_data = None
        for idx, item in enumerate(pending):
            q_data = item['question_data']
            q_id = str(q_data.get('id', idx))
            if str(question_id) == q_id:
                question_index = idx
                question_data = q_data
                break
        
        if question_data is None:
            return jsonify({'success': False, 'error': 'Question not found in pending queue'}), 404
        
        # Grade the answer
        is_correct = False
        explanation = question_data.get('explanation', '')
        correct_answer_display = ''
        
        question_type = question_data.get('type', 'multiple_choice')
        
        if question_type == 'multiple_choice':
            correct_answer = question_data.get('correct_answer')
            options = question_data.get('options', [])
            
            if correct_answer is None:
                is_correct = False
                correct_answer_display = 'Not specified'
            else:
                user_ans_str = str(user_answer).strip().upper()
                correct_ans_str = str(correct_answer).strip().upper()
                
                # Normalize true/false
                if user_ans_str in ['TRUE', 'T', 'YES', 'Y']:
                    user_normalized = '1'
                elif user_ans_str in ['FALSE', 'F', 'NO', 'N']:
                    user_normalized = '0'
                else:
                    user_normalized = user_ans_str
                
                if correct_ans_str in ['TRUE', 'T', 'YES', 'Y']:
                    correct_normalized = '1'
                elif correct_ans_str in ['FALSE', 'F', 'NO', 'N']:
                    correct_normalized = '0'
                elif isinstance(correct_answer, bool):
                    correct_normalized = '1' if correct_answer else '0'
                else:
                    correct_normalized = correct_ans_str
                
                # Compare
                if user_normalized == correct_normalized:
                    is_correct = True
                elif user_normalized in ['A', 'B', 'C', 'D'] and correct_normalized in ['0', '1', '2', '3']:
                    letter_to_index = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
                    if letter_to_index.get(user_normalized) == int(correct_normalized):
                        is_correct = True
                elif user_normalized in ['0', '1', '2', '3'] and user_normalized == correct_normalized:
                    is_correct = True
                
                # Format correct answer for display
                try:
                    if isinstance(correct_answer, int) and options:
                        correct_answer_display = options[correct_answer]
                    else:
                        correct_answer_display = str(correct_answer)
                except:
                    correct_answer_display = str(correct_answer)
        
        elif question_type == 'written':
            verification = verify_written_answer(
                user_answer,
                question_data.get('correct_answer', ''),
                question_data.get('keywords', []),
                question_data.get('min_similarity', 0.6)
            )
            is_correct = verification['is_correct']
            correct_answer_display = question_data.get('correct_answer', '')
        
        # Update pending queue
        if is_correct:
            # Move to completed
            completed_item = pending.pop(question_index)
            completed_item['completed_at'] = datetime.now().isoformat()
            quiz_session['completed'].append(completed_item)
        else:
            # Increment attempts and keep in pending
            pending[question_index]['attempts'] += 1
            pending[question_index]['last_answer'] = user_answer
        
        # Check if quiz is complete
        is_complete = len(pending) == 0
        quiz_session['pending'] = pending
        session[session_key] = quiz_session
        session.modified = True
        
        # Prepare next question if any
        next_question = None
        if not is_complete and len(pending) > 0:
            next_item = pending[0]
            next_q = next_item['question_data'].copy()
            # Don't send correct answer in next question
            if 'correct_answer' in next_q:
                del next_q['correct_answer']
            next_question = next_q
        
        # If complete, save to database
        attempt_id = None
        if is_complete:
            total_questions = quiz_session['total_questions']
            correct_count = len(quiz_session['completed'])
            percentage = (correct_count / total_questions) * 100 if total_questions > 0 else 0
            grade_letter, grade_message = calculate_grade(percentage)
            quiz_info = QUIZ_COURSES.get(quiz_slug, {})
            
            # Build results for storage
            results = []
            for item in quiz_session['completed']:
                q = item['question_data']
                results.append({
                    'id': q.get('id'),
                    'question': q.get('question'),
                    'user_answer': item.get('last_answer', ''),
                    'is_correct': True,
                    'attempts': item.get('attempts', 1)
                })
            
            combined_data = {
                'quiz_data': {
                    'correct_answers': correct_count,
                    'incorrect_answers': 0,
                    'passing_score': 60,
                    'course_name': quiz_info.get('name', ''),
                    'course_code': quiz_info.get('course_code', ''),
                    'cyclic_mode': True,
                    'total_attempts_per_question': [
                        {'id': q['question_data'].get('id'), 'attempts': q.get('attempts', 1)}
                        for q in quiz_session['completed']
                    ]
                },
                'results_summary': {
                    'total_questions': total_questions,
                    'correct_answers': correct_count,
                    'score': correct_count,
                    'percentage': percentage
                }
            }
            
            try:
                quiz_attempt = QuizAttempt(
                    user_id=current_user.id,
                    quiz_type=quiz_slug,
                    quiz_name=quiz_info.get('name', ''),
                    score=correct_count,
                    total_questions=total_questions,
                    percentage=round(percentage, 2),
                    grade=grade_letter,
                    answers=json.dumps(combined_data),
                    results=json.dumps(results),
                    attempt_date=datetime.now()
                )
                db.session.add(quiz_attempt)
                db.session.commit()
                attempt_id = quiz_attempt.id
            except Exception as db_error:
                print(f"Database error: {db_error}")
                db.session.rollback()
            
            # Clear session
            del session[session_key]
            session.modified = True
        
        return jsonify({
            'success': True,
            'is_correct': is_correct,
            'is_complete': is_complete,
            'correct_answer': correct_answer_display if not is_correct else None,
            'explanation': explanation if not is_correct else None,
            'next_question': next_question,
            'progress': {
                'completed': len(quiz_session['completed']),
                'remaining': len(pending),
                'total': quiz_session['total_questions']
            },
            'attempt_id': attempt_id,
            'percentage': (len(quiz_session['completed']) / quiz_session['total_questions']) * 100 if quiz_session['total_questions'] > 0 else 0
        })
        
    except Exception as e:
        print(f"Error in cyclic_submit: {e}")
        traceback.print_exc()
        return jsonify({'success': False, 'error': str(e)}), 500

# ==============================================
# EXISTING API ROUTES (UNCHANGED)
# ==============================================

@quizzes_bp.route('/api/submit', methods=['POST'])
@login_required
def submit_quiz():
    """API endpoint to submit and grade quiz - SIMPLIFIED VERSION"""
    try:
        data = request.json
        print(f"SUBMIT QUIZ: Received data for user {current_user.id}")
        print(f"Quiz type: {data.get('quiz_type')}")
        
        if not data:
            return jsonify({'success': False, 'error': 'No data provided'}), 400
            
        quiz_type = data.get('quiz_type')
        answers = data.get('answers', {})
        adaptive_metrics = data.get('adaptive_metrics', {})
        
        if not quiz_type:
            return jsonify({'success': False, 'error': 'Quiz type is required'}), 400
        
        if quiz_type not in QUIZ_COURSES:
            return jsonify({'success': False, 'error': 'Quiz not found'}), 404
        
        quiz_info = QUIZ_COURSES[quiz_type]
        
        quiz_data = load_quiz_data_from_module(quiz_type)
        
        if not quiz_data:
            return jsonify({'success': False, 'error': 'Quiz data could not be loaded from module'}), 500
        
        if 'questions' not in quiz_data:
            return jsonify({'success': False, 'error': 'No questions found in quiz data'}), 500
        
        all_questions = quiz_data.get('questions', [])
        
        question_map = {}
        for i, question in enumerate(all_questions):
            q_id = str(question.get('id', i+1))
            question_map[q_id] = question
        
        questions_asked = []
        answered_ids = []
        
        for q_id, user_answer in answers.items():
            if q_id in question_map:
                questions_asked.append(question_map[q_id])
                answered_ids.append(q_id)
            else:
                try:
                    idx = int(q_id) - 1
                    if 0 <= idx < len(all_questions):
                        questions_asked.append(all_questions[idx])
                        answered_ids.append(q_id)
                except:
                    pass
        
        if len(questions_asked) < len(answers):
            questions_asked = all_questions[:min(len(answers), len(all_questions))]
        
        results = []
        total_score = 0
        total_questions = len(questions_asked)
        correct_answers = 0
        incorrect_answers = 0
        
        for i, question in enumerate(questions_asked):
            q_id = str(question.get('id', i+1))
            user_answer = answers.get(q_id, '')
            
            if user_answer == '':
                user_answer = answers.get(str(i+1), '')
            
            result = {
                'id': question.get('id', i+1),
                'type': question.get('type', 'multiple_choice'),
                'question': question.get('question', f'Question {i+1}'),
                'user_answer': user_answer,
                'is_correct': False,
                'points': 0,
                'explanation': question.get('explanation', '')
            }
            
            question_type = question.get('type', 'multiple_choice')
            
            if question_type == 'multiple_choice':
                correct_answer = question.get('correct_answer')
                options = question.get('options', [])
                
                if correct_answer is None:
                    result['correct_answer'] = 'Not specified'
                    result['is_correct'] = False
                    incorrect_answers += 1
                else:
                    if user_answer is None or str(user_answer).strip() == '':
                        result['is_correct'] = False
                        incorrect_answers += 1
                    else:
                        user_ans_str = str(user_answer).strip().upper()
                        correct_ans_str = str(correct_answer).strip().upper()
                        
                        user_normalized = user_ans_str
                        correct_normalized = correct_ans_str
                        
                        if user_normalized in ['TRUE', 'T', 'YES', 'Y']:
                            user_normalized = '1'
                        elif user_normalized in ['FALSE', 'F', 'NO', 'N']:
                            user_normalized = '0'
                        
                        if correct_normalized in ['TRUE', 'T', 'YES', 'Y']:
                            correct_normalized = '1'
                        elif correct_normalized in ['FALSE', 'F', 'NO', 'N']:
                            correct_normalized = '0'
                        elif isinstance(correct_answer, bool):
                            correct_normalized = '1' if correct_answer else '0'
                        
                        if user_normalized == correct_normalized:
                            is_correct = True
                        elif user_normalized in ['A', 'B', 'C', 'D'] and correct_normalized in ['0', '1', '2', '3']:
                            letter_to_index = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
                            is_correct = (letter_to_index.get(user_normalized) == int(correct_normalized))
                        elif user_normalized in ['0', '1', '2', '3'] and user_normalized == correct_normalized:
                            is_correct = True
                        else:
                            is_correct = False
                        
                        if is_correct:
                            result['is_correct'] = True
                            result['points'] = 1
                            total_score += 1
                            correct_answers += 1
                        else:
                            incorrect_answers += 1
                    
                    try:
                        if isinstance(correct_answer, int) and options:
                            result['correct_answer'] = options[correct_answer]
                        else:
                            result['correct_answer'] = str(correct_answer)
                    except:
                        result['correct_answer'] = str(correct_answer)
            
            elif question_type == 'written':
                verification = verify_written_answer(
                    user_answer,
                    question.get('correct_answer', ''),
                    question.get('keywords', []),
                    question.get('min_similarity', 0.6)
                )
                
                if verification['is_correct']:
                    result['is_correct'] = True
                    result['points'] = 1
                    total_score += 1
                    correct_answers += 1
                else:
                    incorrect_answers += 1
                
                result['similarity'] = verification['similarity']
                result['found_keywords'] = verification['found_keywords']
                result['correct_answer'] = question.get('correct_answer', '')
                result['expected_keywords'] = question.get('keywords', [])
            
            results.append(result)
        
        percentage = (total_score / total_questions) * 100 if total_questions > 0 else 0
        grade_letter, grade_message = calculate_grade(percentage)
        
        time_taken = data.get('time_taken', 0)
        passing_score = quiz_data.get('passing_score', 60)
        
        metadata = {
            'correct_answers': correct_answers,
            'incorrect_answers': incorrect_answers,
            'time_taken': time_taken,
            'passing_score': passing_score,
            'adaptive_metrics': adaptive_metrics,
            'course_name': quiz_info['name'],
            'course_code': quiz_info['course_code'],
            'passed': percentage >= passing_score,
            'total_score': total_score,
            'total_questions': total_questions
        }
        
        combined_data = {
            'quiz_data': metadata,
            'user_answers': answers,
            'results_summary': {
                'total_questions': total_questions,
                'correct_answers': correct_answers,
                'incorrect_answers': incorrect_answers,
                'score': total_score,
                'percentage': percentage
            }
        }
        
        try:
            quiz_attempt = QuizAttempt(
                user_id=current_user.id,
                quiz_type=quiz_type,
                quiz_name=quiz_info['name'],
                score=total_score,
                total_questions=total_questions,
                percentage=round(percentage, 2),
                grade=grade_letter,
                answers=json.dumps(combined_data),
                results=json.dumps(results),
                attempt_date=datetime.now()
            )
            
            db.session.add(quiz_attempt)
            db.session.commit()
            attempt_id = quiz_attempt.id
        except Exception as db_error:
            print(f"DATABASE ERROR: {db_error}")
            attempt_id = None
            db.session.rollback()
        
        return jsonify({
            'success': True,
            'total_score': total_score,
            'total_questions': total_questions,
            'percentage': round(percentage, 2),
            'grade': grade_letter,
            'grade_message': grade_message,
            'passing_score': passing_score,
            'passed': percentage >= passing_score,
            'results': results,
            'quiz_name': quiz_info['name'],
            'course_code': quiz_info['course_code'],
            'correct_answers': correct_answers,
            'incorrect_answers': incorrect_answers,
            'time_taken': time_taken,
            'attempt_id': attempt_id
        })
        
    except Exception as e:
        print(f"ERROR in submit_quiz: {e}")
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': 'Internal server error',
            'message': str(e)
        }), 500

@quizzes_bp.route('/api/<quiz_slug>/questions')
@login_required
def get_quiz_questions_api(quiz_slug):
    if quiz_slug not in QUIZ_COURSES:
        return jsonify({'success': False, 'error': 'Quiz not found'}), 404
    
    try:
        count = int(request.args.get('count', 20))
        result = get_course_questions_api(quiz_slug, count)
        
        if result and result.get('success'):
            return jsonify(result)
        else:
            error_msg = result.get('message', 'Could not load quiz questions') if result else 'No result returned'
            return jsonify({
                'success': False,
                'message': error_msg
            }), 500
            
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error retrieving questions: {str(e)}'
        }), 500

# ==============================================
# RESULTS API ENDPOINTS (UNCHANGED)
# ==============================================

@quizzes_bp.route('/api/results')
@login_required
def get_all_results():
    try:
        attempts = QuizAttempt.query.filter_by(
            user_id=current_user.id
        ).order_by(QuizAttempt.attempt_date.desc()).all()
        
        results = []
        for attempt in attempts:
            course_info = QUIZ_COURSES.get(attempt.quiz_type, {})
            
            correct_answers = attempt.score
            incorrect_answers = attempt.total_questions - correct_answers if attempt.total_questions else 0
            time_taken = 0
            passing_score = 60
            adaptive_metrics = {}
            course_name = attempt.quiz_name
            course_code = course_info.get('course_code', '')
            passed = attempt.percentage >= passing_score
            
            try:
                if attempt.answers:
                    answers_data = json.loads(attempt.answers)
                    if isinstance(answers_data, dict) and 'quiz_data' in answers_data:
                        quiz_metadata = answers_data['quiz_data']
                        correct_answers = quiz_metadata.get('correct_answers', attempt.score)
                        incorrect_answers = quiz_metadata.get('incorrect_answers', incorrect_answers)
                        time_taken = quiz_metadata.get('time_taken', 0)
                        passing_score = quiz_metadata.get('passing_score', 60)
                        adaptive_metrics = quiz_metadata.get('adaptive_metrics', {})
                        course_name = quiz_metadata.get('course_name', attempt.quiz_name)
                        course_code = quiz_metadata.get('course_code', course_info.get('course_code', ''))
                        passed = quiz_metadata.get('passed', attempt.percentage >= passing_score)
            except:
                pass
            
            results.append({
                'id': attempt.id,
                'quiz_type': attempt.quiz_type,
                'quiz_name': attempt.quiz_name,
                'course_name': course_name,
                'course_code': course_code,
                'score': attempt.score,
                'total_questions': attempt.total_questions,
                'percentage': float(attempt.percentage),
                'grade': attempt.grade,
                'passed': passed,
                'passing_score': passing_score,
                'completed_at': attempt.attempt_date.isoformat() if attempt.attempt_date else None,
                'time_taken': time_taken,
                'correct_answers': correct_answers,
                'incorrect_answers': incorrect_answers,
                'adaptive_metrics': adaptive_metrics
            })
        
        return jsonify({
            'success': True,
            'results': results
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error retrieving results: {str(e)}'
        }), 500

@quizzes_bp.route('/api/results/<int:attempt_id>')
@login_required
def get_quiz_attempt_details(attempt_id):
    try:
        attempt = QuizAttempt.query.filter_by(
            id=attempt_id,
            user_id=current_user.id
        ).first()
        
        if not attempt:
            return jsonify({
                'success': False,
                'message': 'Attempt not found'
            }), 404
        
        course_info = QUIZ_COURSES.get(attempt.quiz_type, {})
        
        correct_answers = attempt.score
        incorrect_answers = attempt.total_questions - correct_answers if attempt.total_questions else 0
        time_taken = 0
        passing_score = 60
        adaptive_metrics = {}
        course_name = attempt.quiz_name
        course_code = course_info.get('course_code', '')
        passed = attempt.percentage >= passing_score
        
        try:
            if attempt.answers:
                answers_data = json.loads(attempt.answers)
                if isinstance(answers_data, dict) and 'quiz_data' in answers_data:
                    quiz_metadata = answers_data['quiz_data']
                    correct_answers = quiz_metadata.get('correct_answers', attempt.score)
                    incorrect_answers = quiz_metadata.get('incorrect_answers', incorrect_answers)
                    time_taken = quiz_metadata.get('time_taken', 0)
                    passing_score = quiz_metadata.get('passing_score', 60)
                    adaptive_metrics = quiz_metadata.get('adaptive_metrics', {})
                    course_name = quiz_metadata.get('course_name', attempt.quiz_name)
                    course_code = quiz_metadata.get('course_code', course_info.get('course_code', ''))
                    passed = quiz_metadata.get('passed', attempt.percentage >= passing_score)
        except:
            pass
        
        questions_data = []
        try:
            if attempt.results:
                results_data = json.loads(attempt.results)
                if isinstance(results_data, list):
                    questions_data = results_data
        except:
            pass
        
        result_data = {
            'id': attempt.id,
            'quiz_type': attempt.quiz_type,
            'quiz_name': attempt.quiz_name,
            'course_name': course_name,
            'course_code': course_code,
            'score': attempt.score,
            'percentage': float(attempt.percentage),
            'total_questions': attempt.total_questions,
            'correct_answers': correct_answers,
            'incorrect_answers': incorrect_answers,
            'time_taken': time_taken,
            'passed': passed,
            'passing_score': passing_score,
            'completed_at': attempt.attempt_date.isoformat() if attempt.attempt_date else None,
            'questions': questions_data,
            'adaptive_metrics': adaptive_metrics
        }
        
        return jsonify({
            'success': True,
            'result': result_data
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error retrieving attempt details: {str(e)}'
        }), 500

# ==============================================
# DEBUG ROUTES (UNCHANGED)
# ==============================================

@quizzes_bp.route('/api/debug-latest-attempt')
@login_required
def debug_latest_attempt():
    try:
        attempt = QuizAttempt.query.filter_by(
            user_id=current_user.id
        ).order_by(QuizAttempt.attempt_date.desc()).first()
        
        if not attempt:
            return jsonify({'success': False, 'message': 'No attempts found'})
        
        raw_data = {
            'id': attempt.id,
            'quiz_type': attempt.quiz_type,
            'quiz_name': attempt.quiz_name,
            'score': attempt.score,
            'total_questions': attempt.total_questions,
            'percentage': attempt.percentage,
            'grade': attempt.grade,
            'answers_raw': attempt.answers,
            'results_raw': attempt.results[:500] + '...' if attempt.results and len(attempt.results) > 500 else attempt.results
        }
        
        parsed_data = {}
        if attempt.answers:
            try:
                parsed = json.loads(attempt.answers)
                parsed_data['parsed_answers_keys'] = list(parsed.keys()) if isinstance(parsed, dict) else type(parsed)
                
                if isinstance(parsed, dict):
                    if 'quiz_data' in parsed:
                        quiz_data = parsed['quiz_data']
                        parsed_data['quiz_data'] = {
                            'correct_answers': quiz_data.get('correct_answers', 'NOT FOUND'),
                            'incorrect_answers': quiz_data.get('incorrect_answers', 'NOT FOUND'),
                            'score_in_json': quiz_data.get('correct_answers', 'NOT FOUND'),
                            'match_with_db_score': quiz_data.get('correct_answers', 0) == attempt.score
                        }
                    else:
                        parsed_data['warning'] = 'NO quiz_data key found!'
                        parsed_data['full_structure'] = parsed
            except Exception as e:
                parsed_data['parse_error'] = str(e)
        
        return jsonify({
            'success': True,
            'raw': raw_data,
            'parsed': parsed_data
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@quizzes_bp.route('/api/debug-answer-matching')
@login_required
def debug_answer_matching():
    test_cases = [
        {'user': 'A', 'correct': 0, 'expected': True, 'desc': 'Letter A -> index 0'},
        {'user': 'B', 'correct': 1, 'expected': True, 'desc': 'Letter B -> index 1'},
        {'user': 'C', 'correct': 2, 'expected': True, 'desc': 'Letter C -> index 2'},
        {'user': 'D', 'correct': 3, 'expected': True, 'desc': 'Letter D -> index 3'},
        {'user': '0', 'correct': 0, 'expected': True, 'desc': 'String 0 -> index 0'},
        {'user': '1', 'correct': 1, 'expected': True, 'desc': 'String 1 -> index 1'},
        {'user': '2', 'correct': 2, 'expected': True, 'desc': 'String 2 -> index 2'},
        {'user': '3', 'correct': 3, 'expected': True, 'desc': 'String 3 -> index 3'},
        {'user': 'a', 'correct': 0, 'expected': True, 'desc': 'Lowercase a -> index 0'},
        {'user': 'Option A', 'correct': 0, 'expected': False, 'desc': 'Full option text'},
        {'user': 'True', 'correct': 'True', 'expected': True, 'desc': 'True string match'},
        {'user': 'true', 'correct': 'True', 'expected': True, 'desc': 'Lowercase true -> True'},
        {'user': 'T', 'correct': 'True', 'expected': True, 'desc': 'T -> True'},
        {'user': 'False', 'correct': 'False', 'expected': True, 'desc': 'False string match'},
        {'user': 'false', 'correct': 'False', 'expected': True, 'desc': 'Lowercase false -> False'},
        {'user': 'F', 'correct': 'False', 'expected': True, 'desc': 'F -> False'},
    ]
    
    results = []
    for test in test_cases:
        user_ans_str = str(test['user']).strip().upper()
        correct_ans_str = str(test['correct'])
        is_correct = False
        
        if user_ans_str in ['A', 'B', 'C', 'D']:
            letter_to_index = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
            user_index = letter_to_index.get(user_ans_str)
            is_correct = user_index == int(correct_ans_str)
        elif user_ans_str == correct_ans_str:
            is_correct = True
        elif user_ans_str in ['0', '1', '2', '3'] and user_ans_str == correct_ans_str:
            is_correct = True
        else:
            user_normalized = user_ans_str
            correct_normalized = correct_ans_str
            
            if user_normalized in ['TRUE', 'T', '1']:
                user_normalized = 'TRUE'
            elif user_normalized in ['FALSE', 'F', '0']:
                user_normalized = 'FALSE'
            
            if correct_normalized in ['TRUE', 'T', '1']:
                correct_normalized = 'TRUE'
            elif correct_normalized in ['FALSE', 'F', '0']:
                correct_normalized = 'FALSE'
            
            is_correct = (user_normalized == correct_normalized)
        
        results.append({
            'test': test['desc'],
            'user_input': test['user'],
            'correct_answer': test['correct'],
            'result': is_correct,
            'expected': test['expected'],
            'match': is_correct == test['expected']
        })
    
    return jsonify({
        'success': True,
        'tests': results,
        'note': 'This tests the answer matching logic including true/false questions.'
    })

@quizzes_bp.route('/api/debug-db-state')
@login_required
def debug_db_state():
    try:
        total_attempts = QuizAttempt.query.filter_by(user_id=current_user.id).count()
        
        attempts = QuizAttempt.query.filter_by(user_id=current_user.id).all()
        
        attempts_data = []
        for attempt in attempts:
            attempts_data.append({
                'id': attempt.id,
                'quiz_type': attempt.quiz_type,
                'quiz_name': attempt.quiz_name,
                'score': attempt.score,
                'total_questions': attempt.total_questions,
                'percentage': attempt.percentage,
                'grade': attempt.grade,
                'attempt_date': attempt.attempt_date.isoformat() if attempt.attempt_date else None,
                'has_answers': bool(attempt.answers),
                'has_results': bool(attempt.results)
            })
        
        return jsonify({
            'success': True,
            'user_id': current_user.id,
            'total_attempts_in_db': total_attempts,
            'attempts': attempts_data
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

# ==============================================
# ERROR HANDLERS
# ==============================================

@quizzes_bp.errorhandler(404)
def not_found_error(error):
    if request.path.startswith('/api/'):
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return f"<h1>Page Not Found</h1><p>The page you requested could not be found.</p>", 404

@quizzes_bp.errorhandler(500)
def internal_error(error):
    traceback.print_exc()
    if request.path.startswith('/api/'):
        return jsonify({'success': False, 'error': 'Internal server error', 'details': str(error)}), 500
    return f"<h1>Internal Server Error</h1><p>An error occurred. Please try again later.</p><pre>{error}</pre>", 500