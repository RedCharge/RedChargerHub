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
    
    # Text similarity
    similarity = SequenceMatcher(None, user_clean, correct_clean).ratio()
    
    # Keyword matching
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
    
    # Consider answer correct if similarity is high OR keywords are found
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
        
        # Convert slug to module name
        module_name = quiz_slug.replace('-', '_')
        
        # Add current directory to Python path
        current_dir = os.path.dirname(os.path.abspath(__file__))
        app_dir = os.path.dirname(current_dir)
        
        if app_dir not in sys.path:
            sys.path.insert(0, app_dir)
        
        try:
            # Try direct import from courses folder
            module_path = f"app.courses.{module_name}"
            print(f"Trying import from: {module_path}")
            module = importlib.import_module(module_path)
            print(f"Successfully imported module: {module_path}")
            
        except ImportError as e:
            print(f"Failed to import {module_path}: {e}")
            print("Checking current directory structure...")
            
            # Check if module exists in current directory
            module_file = f"{module_name}.py"
            current_files = os.listdir(current_dir)
            print(f"Files in current directory: {current_files}")
            
            if module_file in current_files:
                print(f"Found {module_file} in current directory")
                module = importlib.import_module(module_name)
            else:
                # Try parent directory
                parent_dir = os.path.dirname(current_dir)
                parent_files = os.listdir(parent_dir)
                print(f"Files in parent directory: {parent_files}")
                
                if module_file in parent_files:
                    print(f"Found {module_file} in parent directory")
                    sys.path.insert(0, parent_dir)
                    module = importlib.import_module(module_name)
                else:
                    raise ImportError(f"Could not find module {module_name} in any expected location")
        
        # Look for quiz data in the module
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
            # Look for any variable that might contain questions
            print(f"Searching for quiz data in module attributes...")
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
        # Load quiz data from module
        quiz_data = load_quiz_data_from_module(quiz_slug)
        
        if not quiz_data:
            print(f"No quiz data returned for {quiz_slug}")
            return {
                'success': False,
                'message': 'Could not load quiz data from module'
            }
        
        if 'questions' not in quiz_data:
            print(f"No 'questions' key in quiz data for {quiz_slug}")
            return {
                'success': False,
                'message': 'No questions found in quiz data'
            }
        
        all_questions = quiz_data['questions']
        print(f"Found {len(all_questions)} total questions for {quiz_slug}")
        
        # Check if we have enough questions
        if len(all_questions) < count:
            print(f"Warning: Only {len(all_questions)} questions available, requested {count}")
            count = len(all_questions)
        
        # Select random questions
        if len(all_questions) > count:
            quiz_questions = random.sample(all_questions, count)
        else:
            quiz_questions = all_questions.copy()
        
        print(f"Selected {len(quiz_questions)} questions for quiz")
        
        # Randomize answer positions for multiple choice questions
        for question in quiz_questions:
            if 'options' in question and 'correct_answer' in question:
                try:
                    # Store the correct answer text
                    correct_index = question['correct_answer']
                    if isinstance(correct_index, int) and 0 <= correct_index < len(question['options']):
                        correct_answer_text = question['options'][correct_index]
                        # Shuffle options
                        random.shuffle(question['options'])
                        # Find new position of correct answer
                        question['correct_answer'] = question['options'].index(correct_answer_text)
                except Exception as e:
                    print(f"Error shuffling options for question {question.get('id')}: {e}")
        
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
    """Redirect to quizzes main page"""
    return redirect(url_for('quizzes.quizzes'))

@quizzes_bp.route('/quiz-results')
@login_required
def quiz_results():
    """Show comprehensive quiz results page"""
    return render_template('/quizzes/quiz_result.html')

@quizzes_bp.route('/quizzes')
@login_required
def quizzes():
    """Main quizzes page - shows all available quiz courses"""
    # Get user's quiz attempts to show progress
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
    
    # Prepare course data for template
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
        
        # Add user attempt data if exists
        if slug in user_attempts:
            course_info.update(user_attempts[slug])
        
        courses_data.append(course_info)
    
    # Calculate stats
    total_courses = len(QUIZ_COURSES)
    total_questions = sum(quiz['questions'] for quiz in QUIZ_COURSES.values())
    
    return render_template('quizzes/quizzes.html', 
                         courses=courses_data,
                         total_courses=total_courses,
                         total_questions=total_questions)

@quizzes_bp.route('/take/<quiz_slug>')
@login_required
def take_quiz(quiz_slug):
    """Take an interactive quiz"""
    print(f"take_quiz called with slug: {quiz_slug}")
    
    if quiz_slug not in QUIZ_COURSES:
        flash('Quiz not found', 'error')
        return redirect(url_for('quizzes.quizzes'))
    
    quiz_info = QUIZ_COURSES[quiz_slug]
    print(f"Quiz info loaded: {quiz_info['name']}")
    
    # Try to load quiz data from module
    quiz_data = load_quiz_data_from_module(quiz_slug)
    
    if not quiz_data:
        flash('Could not load quiz questions from course module. Please contact administrator.', 'error')
        return redirect(url_for('quizzes.quizzes'))
    
    print(f"Quiz data loaded successfully. Questions found: {len(quiz_data.get('questions', []))}")
    
    # Add defaults if not present
    if 'passing_score' not in quiz_data:
        quiz_data['passing_score'] = 60
    
    if 'course_code' not in quiz_data:
        quiz_data['course_code'] = quiz_info['course_code']
    
    if 'course_name' not in quiz_data:
        quiz_data['course_name'] = quiz_info['name']
    
    # Calculate question counts for template
    questions = quiz_data.get('questions', [])
    total_questions = len(questions)
    mc_questions = len([q for q in questions if q.get('type') == 'multiple_choice'])
    written_questions = len([q for q in questions if q.get('type') == 'written'])
    
    # Get the last attempt for this quiz
    last_attempt = QuizAttempt.query.filter_by(
        user_id=current_user.id, 
        quiz_type=quiz_slug
    ).order_by(QuizAttempt.attempt_date.desc()).first()
    
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
                         last_attempt=last_attempt)

# ==============================================
# API ROUTES
# ==============================================

@quizzes_bp.route('/api/submit', methods=['POST'])
@login_required
def submit_quiz():
    """API endpoint to submit and grade quiz - PROPERLY HANDLES BOTH MULTIPLE CHOICE AND TRUE/FALSE"""
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
        
        # Load quiz data from module
        quiz_data = load_quiz_data_from_module(quiz_type)
        
        if not quiz_data:
            return jsonify({'success': False, 'error': 'Quiz data could not be loaded from module'}), 500
        
        if 'questions' not in quiz_data:
            return jsonify({'success': False, 'error': 'No questions found in quiz data'}), 500
        
        all_questions = quiz_data.get('questions', [])
        
        # Create a mapping of question IDs to questions
        question_map = {}
        for i, question in enumerate(all_questions):
            q_id = str(question.get('id', i+1))
            question_map[q_id] = question
        
        print(f"DEBUG: Loaded {len(all_questions)} questions")
        print(f"DEBUG: Answers received: {list(answers.keys())}")
        
        # Find questions that were answered
        questions_asked = []
        answered_ids = []
        
        # First, try to match by exact question ID
        for q_id, user_answer in answers.items():
            if q_id in question_map:
                questions_asked.append(question_map[q_id])
                answered_ids.append(q_id)
                print(f"DEBUG: Matched answer for question ID {q_id}")
            else:
                # Try to find by index if ID is numeric
                try:
                    idx = int(q_id) - 1
                    if 0 <= idx < len(all_questions):
                        questions_asked.append(all_questions[idx])
                        answered_ids.append(q_id)
                        print(f"DEBUG: Matched answer for numeric index {q_id}")
                except:
                    print(f"DEBUG: Could not match answer for {q_id}")
        
        # If we don't have enough questions, use the first N questions
        if len(questions_asked) < len(answers):
            print(f"DEBUG: Only matched {len(questions_asked)} questions, using first {len(answers)} questions")
            questions_asked = all_questions[:min(len(answers), len(all_questions))]
        
        # Grade the quiz
        results = []
        total_score = 0
        total_questions = len(questions_asked)
        correct_answers = 0
        incorrect_answers = 0
        
        print(f"=== GRADING START ===")
        print(f"Total questions to grade: {total_questions}")
        
        for i, question in enumerate(questions_asked):
            q_id = str(question.get('id', i+1))
            user_answer = answers.get(q_id, '')
            
            # If q_id not found, try with index
            if user_answer == '':
                # Try with numeric index
                user_answer = answers.get(str(i+1), '')
            
            print(f"\nQ{i+1} (ID: {q_id}):")
            print(f"  Question: {question.get('question', '')[:50]}...")
            print(f"  User answer: '{user_answer}' (type: {type(user_answer)})")
            print(f"  Correct answer (stored): {question.get('correct_answer')} (type: {type(question.get('correct_answer'))})")
            
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
                
                # Handle case where correct_answer is None
                if correct_answer is None:
                    print(f"  WARNING: No correct answer specified for question {q_id}")
                    result['correct_answer'] = 'Not specified'
                    result['is_correct'] = False
                    result['points'] = 0
                    incorrect_answers += 1
                    print(f"  RESULT: ✗ INCORRECT (No correct answer in database)")
                
                else:
                    # Handle empty answer - mark as incorrect
                    if user_answer is None or str(user_answer).strip() == '':
                        result['is_correct'] = False
                        result['points'] = 0
                        incorrect_answers += 1
                        print(f"  EMPTY ANSWER - Marked as incorrect")
                        
                    else:
                        # Convert both to strings and normalize
                        user_ans_str = str(user_answer).strip()
                        correct_ans_str = str(correct_answer).strip()
                        
                        # Debug print
                        print(f"  Comparing: user='{user_ans_str}', correct='{correct_ans_str}'")
                        
                        is_correct = False
                        
                        # Get options safely
                        if not isinstance(options, list):
                            options = []
                        
                        # CRITICAL FIX: Check if this is REALLY a true/false question
                        # True/false questions have NO options array or empty options
                        is_true_false = False
                        
                        # Method 1: Check question type from data
                        if question.get('type') == 'true_false':
                            is_true_false = True
                            print(f"  Question marked as 'true_false' type")
                        
                        # Method 2: No options = true/false question  
                        elif len(options) == 0:
                            is_true_false = True
                            print(f"  No options - treating as True/False question")
                        
                        # Method 3: Check for boolean correct answer
                        elif isinstance(correct_answer, bool):
                            is_true_false = True
                            print(f"  Boolean correct answer - treating as True/False question")
                        
                        # Method 4: Check question text for true/false indicators
                        elif 'true or false' in question.get('question', '').lower() or \
                             'true/false' in question.get('question', '').lower():
                            is_true_false = True
                            print(f"  Question contains 'true/false' - treating as True/False question")
                        
                        else:
                            # Has options = regular multiple choice
                            is_true_false = False
                            print(f"  Has {len(options)} options - treating as regular multiple choice")
                        
                        if is_true_false:
                            # ==============================================
                            # TRUE/FALSE QUESTION LOGIC
                            # ==============================================
                            
                            # Normalize user answer
                            user_normalized = user_ans_str.upper()
                            if user_normalized in ['TRUE', 'T', '1', 'YES', 'Y']:
                                user_normalized = 'TRUE'
                            elif user_normalized in ['FALSE', 'F', '0', 'NO', 'N']:
                                user_normalized = 'FALSE'
                            
                            # Normalize correct answer
                            if isinstance(correct_answer, bool):
                                correct_normalized = 'TRUE' if correct_answer else 'FALSE'
                            elif correct_ans_str.upper() in ['TRUE', 'T', '1']:
                                correct_normalized = 'TRUE'
                            elif correct_ans_str.upper() in ['FALSE', 'F', '0']:
                                correct_normalized = 'FALSE'
                            else:
                                correct_normalized = correct_ans_str.upper()
                            
                            is_correct = (user_normalized == correct_normalized)
                            print(f"  True/False comparison: '{user_normalized}' == '{correct_normalized}': {is_correct}")
                        
                        else:
                            # ==============================================
                            # REGULAR MULTIPLE CHOICE QUESTION LOGIC
                            # ==============================================
                            
                            print(f"  Regular multiple choice with {len(options)} options")
                            
                            # Method 1: Direct numeric comparison (0, 1, 2, 3)
                            if user_ans_str in ['0', '1', '2', '3'] and correct_ans_str in ['0', '1', '2', '3']:
                                is_correct = (user_ans_str == correct_ans_str)
                                print(f"  Numeric comparison: '{user_ans_str}' == '{correct_ans_str}': {is_correct}")
                            
                            # Method 2: Letter to index comparison (A, B, C, D -> 0, 1, 2, 3)
                            elif user_ans_str.upper() in ['A', 'B', 'C', 'D']:
                                letter_to_index = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
                                user_index = letter_to_index.get(user_ans_str.upper())
                                
                                if correct_ans_str in ['0', '1', '2', '3']:
                                    is_correct = (user_index == int(correct_ans_str))
                                    print(f"  Letter '{user_ans_str}' (index {user_index}) == '{correct_ans_str}': {is_correct}")
                                else:
                                    # Try to match letter directly
                                    is_correct = (user_ans_str.upper() == correct_ans_str.upper())
                                    print(f"  Direct letter comparison: '{user_ans_str}' == '{correct_ans_str}': {is_correct}")
                            
                            # Method 3: Direct string comparison (for any other format)
                            else:
                                is_correct = (user_ans_str.upper() == correct_ans_str.upper())
                                print(f"  Direct string comparison: '{user_ans_str}' == '{correct_ans_str}': {is_correct}")
                        
                        # Update counters based on result
                        if is_correct:
                            result['is_correct'] = True
                            result['points'] = 1
                            total_score += 1
                            correct_answers += 1
                            print(f"  RESULT: ✓ CORRECT! Total correct: {correct_answers}")
                        else:
                            result['is_correct'] = False
                            result['points'] = 0
                            incorrect_answers += 1
                            print(f"  RESULT: ✗ INCORRECT")
                    
                    # Store correct answer text for display
                    try:
                        # For true/false questions
                        if isinstance(correct_answer, bool):
                            result['correct_answer'] = 'True' if correct_answer else 'False'
                        elif str(correct_answer).upper() in ['TRUE', 'T', '1']:
                            result['correct_answer'] = 'True'
                        elif str(correct_answer).upper() in ['FALSE', 'F', '0']:
                            result['correct_answer'] = 'False'
                        # For multiple choice with options
                        elif len(options) > 0:
                            if isinstance(correct_answer, int) and 0 <= correct_answer < len(options):
                                result['correct_answer'] = options[correct_answer]
                            elif isinstance(correct_answer, str) and correct_answer.isdigit():
                                idx = int(correct_answer)
                                if 0 <= idx < len(options):
                                    result['correct_answer'] = options[idx]
                                else:
                                    result['correct_answer'] = str(correct_answer)
                            else:
                                result['correct_answer'] = str(correct_answer)
                        else:
                            result['correct_answer'] = str(correct_answer)
                    except Exception as e:
                        print(f"  Error formatting correct answer: {e}")
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
                    print(f"  Written answer: ✓ CORRECT! Similarity: {verification['similarity']:.2f}")
                else:
                    result['is_correct'] = False
                    result['points'] = 0
                    incorrect_answers += 1
                    print(f"  Written answer: ✗ INCORRECT! Similarity: {verification['similarity']:.2f}")
                
                result['similarity'] = verification['similarity']
                result['found_keywords'] = verification['found_keywords']
                result['correct_answer'] = question.get('correct_answer', '')
                result['expected_keywords'] = question.get('keywords', [])
            
            results.append(result)
        
        # Final validation
        print(f"\n=== GRADING COMPLETE ===")
        print(f"Total Questions: {total_questions}")
        print(f"Total Score: {total_score}")
        print(f"Correct Answers: {correct_answers}")
        print(f"Incorrect Answers: {incorrect_answers}")
        
        # Validate that totals match
        if (correct_answers + incorrect_answers) != total_questions:
            print(f"WARNING: Numbers don't match! {correct_answers} + {incorrect_answers} != {total_questions}")
            print(f"Fixing discrepancy...")
            incorrect_answers = total_questions - correct_answers
            print(f"Adjusted: Correct={correct_answers}, Incorrect={incorrect_answers}")
        
        # Calculate percentage and grade
        percentage = (total_score / total_questions) * 100 if total_questions > 0 else 0
        grade_letter, grade_message = calculate_grade(percentage)
        
        # Get time taken from request if available
        time_taken = data.get('time_taken', 0)
        passing_score = quiz_data.get('passing_score', 60)
        
        print(f"\n=== FINAL RESULTS ===")
        print(f"Percentage: {percentage:.1f}%")
        print(f"Grade: {grade_letter}")
        print(f"Passing Score: {passing_score}%")
        print(f"Passed: {percentage >= passing_score}")
        
        # Create metadata for JSON storage
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
        
        # Combine all data for JSON storage
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
        
        # Save to database
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
            print(f"SUCCESS: Quiz attempt saved to database with ID {attempt_id}")
            print(f"  Correct answers: {correct_answers}")
            print(f"  Incorrect answers: {incorrect_answers}")
            print(f"  Total questions: {total_questions}")
            
        except Exception as db_error:
            print(f"DATABASE ERROR: {db_error}")
            traceback.print_exc()
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
            'course_name': quiz_info['name'],
            'correct_answers': correct_answers,
            'incorrect_answers': incorrect_answers,
            'time_taken': time_taken,
            'adaptive_metrics': adaptive_metrics,
            'attempt_id': attempt_id,
            'debug_info': {
                'score_match': total_score == correct_answers,
                'correct_plus_incorrect': f"{correct_answers} + {incorrect_answers} = {correct_answers + incorrect_answers}",
                'total_questions_graded': total_questions,
                'answers_received': len(answers)
            }
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
    """API endpoint to get questions for a specific quiz"""
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
        print(f"Error in get_quiz_questions_api: {str(e)}")
        return jsonify({
            'success': False,
            'message': f'Error retrieving questions: {str(e)}'
        }), 500

# ==============================================
# RESULTS API ENDPOINTS
# ==============================================

@quizzes_bp.route('/api/results')
@login_required
def get_all_results():
    """Get all quiz results for the current user"""
    try:
        print(f"DEBUG: Getting results for user_id={current_user.id}")
        
        # Get all attempts for the user
        attempts = QuizAttempt.query.filter_by(
            user_id=current_user.id
        ).order_by(QuizAttempt.attempt_date.desc()).all()
        
        print(f"DEBUG: Found {len(attempts)} attempts in database")
        
        results = []
        for attempt in attempts:
            # Get course information from QUIZ_COURSES mapping
            course_info = QUIZ_COURSES.get(attempt.quiz_type, {})
            
            # Initialize with defaults
            correct_answers = attempt.score  # Use score as correct answers
            incorrect_answers = attempt.total_questions - correct_answers if attempt.total_questions else 0
            time_taken = 0
            passing_score = 60
            adaptive_metrics = {}
            course_name = attempt.quiz_name
            course_code = course_info.get('course_code', '')
            passed = attempt.percentage >= passing_score
            
            # Try to extract from JSON answers
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
            except Exception as e:
                print(f"Error parsing JSON for attempt {attempt.id}: {e}")
            
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
        
        print(f"DEBUG: Returning {len(results)} results")
        
        return jsonify({
            'success': True,
            'results': results
        })
        
    except Exception as e:
        print(f"ERROR in get_all_results: {e}")
        traceback.print_exc()
        return jsonify({
            'success': False,
            'message': f'Error retrieving results: {str(e)}'
        }), 500

@quizzes_bp.route('/api/results/<int:attempt_id>')
@login_required
def get_quiz_attempt_details(attempt_id):
    """Get detailed results for a specific quiz attempt"""
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
        
        # Get course information
        course_info = QUIZ_COURSES.get(attempt.quiz_type, {})
        
        # Extract data
        correct_answers = attempt.score
        incorrect_answers = attempt.total_questions - correct_answers if attempt.total_questions else 0
        time_taken = 0
        passing_score = 60
        adaptive_metrics = {}
        course_name = attempt.quiz_name
        course_code = course_info.get('course_code', '')
        passed = attempt.percentage >= passing_score
        
        # Try to extract from JSON
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
        
        # Get questions data
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
        print(f"Error getting attempt details: {e}")
        return jsonify({
            'success': False,
            'message': f'Error retrieving attempt details: {str(e)}'
        }), 500

# ==============================================
# DEBUG ROUTES
# ==============================================

@quizzes_bp.route('/api/debug-latest-attempt')
@login_required
def debug_latest_attempt():
    """Debug the latest quiz attempt"""
    try:
        # Get latest attempt
        attempt = QuizAttempt.query.filter_by(
            user_id=current_user.id
        ).order_by(QuizAttempt.attempt_date.desc()).first()
        
        if not attempt:
            return jsonify({'success': False, 'message': 'No attempts found'})
        
        # Show RAW data
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
        
        # Parse and show JSON structure
        parsed_data = {}
        if attempt.answers:
            try:
                parsed = json.loads(attempt.answers)
                parsed_data['parsed_answers_keys'] = list(parsed.keys()) if isinstance(parsed, dict) else type(parsed)
                
                # Show what's in quiz_data
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
            'error': str(e),
            'traceback': traceback.format_exc()
        })

@quizzes_bp.route('/api/debug-answer-matching')
@login_required
def debug_answer_matching():
    """Test answer matching logic"""
    try:
        # Test cases for answer matching
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
            
            # Test the matching logic
            if user_ans_str in ['A', 'B', 'C', 'D']:
                letter_to_index = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
                user_index = letter_to_index.get(user_ans_str)
                is_correct = user_index == int(correct_ans_str)
            elif user_ans_str == correct_ans_str:
                is_correct = True
            elif user_ans_str in ['0', '1', '2', '3'] and user_ans_str == correct_ans_str:
                is_correct = True
            else:
                # Normalize true/false answers
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
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@quizzes_bp.route('/api/debug-db-state')
@login_required
def debug_db_state():
    """Debug endpoint to check database state"""
    try:
        # Count all quiz attempts for this user
        total_attempts = QuizAttempt.query.filter_by(user_id=current_user.id).count()
        
        # Get all attempts
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
    print(f"404 error handler called: {error}")
    if request.path.startswith('/api/'):
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return f"<h1>Page Not Found</h1><p>The page you requested could not be found.</p>", 404

@quizzes_bp.errorhandler(500)
def internal_error(error):
    print(f"500 error handler called: {error}")
    traceback.print_exc()
    if request.path.startswith('/api/'):
        return jsonify({'success': False, 'error': 'Internal server error', 'details': str(error)}), 500
    return f"<h1>Internal Server Error</h1><p>An error occurred. Please try again later.</p><pre>{error}</pre>", 500