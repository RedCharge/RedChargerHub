from flask import Blueprint, render_template, request, flash, jsonify, session, redirect, url_for
from flask_login import login_required, current_user
from app.models import QuizAttempt, UserQuestionProgress, db
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
    'emerging-frontiers': {
        'course_code': 'BCP 203',
        'name': 'Emergigng Frontiers in Technology',
        'image': 'https://images.ctfassets.net/mrbo2ykgx5lt/5wwL0gvQpNnFvqDe5wF2Sg/205cccfa608e8da290c6993bf84739f0/Horizontal-Arabic_Female_Future_Engineer_Looks_At_Work_of_Skilful_Developer._Asian_Man_Explains_Core_Principles_and_Examins_.png?&w=912&fm=webp&q=80',
        'questions': 50,
        'duration': '60 minutes'
    },
    'database-system': {
        'course_code': 'ATU 203',
        'name': 'Database System Design',
        'image': 'https://everconnectds.com/wp-content/uploads/2022/02/what-connections-do-databases-have-to-business-intelligence-700x350.jpg',
        'questions': 50,
        'duration': '60 minutes'
    },
    'creative-thinking': {
        'course_code': 'BCP 105',
        'name': 'Creative Thinking and Problem Solving',
        'image': 'https://previews.123rf.com/images/rawpixel/rawpixel1609/rawpixel160954833/62638073-problem-solving-creative-thinking-brainstorm-people-concept.jpg',
        'questions': 50,
        'duration': '60 minutes'
    },
    'entrepreneurship-new-venture': {
        'course_code': 'ATU 201',
        'name': 'Enterpreneurship and New venture Creation',
        'image': 'https://unctad.org/sites/default/files/2024-04/2024-04-02_South-Africa-entrepreneurship_1200x675.jpg',
        'questions': 50,
        'duration': '60 minutes'
    },
    'grid-computing': {
        'course_code': 'BCB 209',
        'name': 'Grid Computing',
        'image': 'https://assets.enterprisenetworkingplanet.com/uploads/2021/05/Grid-Computing-vs-Cloud-Computing.jpeg?f=jpeg',
        'questions': 50,
        'duration': '60 minutes'
    },
    'web-development': {
        'course_code': 'BCP 207',
        'name': 'Web Development Technologies II',
        'image': 'https://images.unsplash.com/photo-1627398242454-45a1465c2479?ixlib=rb-4.0.3&auto=format&fit=crop&w=2074&q=80',
        'questions': 50,
        'duration': '60 minutes'
    },
    'java-programming': {
        'course_code': 'BCP 201',
        'name': 'Programming with Java',
        'image': 'https://miro.medium.com/1*fOdb_ET1sOd4uZStK4E8HA.jpeg',
        'questions': 50,
        'duration': '60 minutes'
    },
    'data-structure-algorithm': {
        'course_code': 'BCP 201',
        'name': 'Data Structure and Algorithm',
        'image': 'https://d3sujgifhk94se.cloudfront.net/wp-content/uploads/2023/10/23125043/coding_algorithm.jpg',
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

def initialize_question_progress(user_id, quiz_type, questions):
    """Initialize progress records for all questions in a quiz"""
    try:
        print(f"Initializing question progress for user {user_id}, quiz {quiz_type}")
        created_count = 0
        
        for question in questions:
            question_id = str(question.get('id'))
            
            # Check if progress record already exists
            existing = UserQuestionProgress.query.filter_by(
                user_id=user_id,
                quiz_type=quiz_type,
                question_id=question_id
            ).first()
            
            if not existing:
                progress = UserQuestionProgress(
                    user_id=user_id,
                    quiz_type=quiz_type,
                    question_id=question_id
                )
                db.session.add(progress)
                created_count += 1
        
        if created_count > 0:
            db.session.commit()
            print(f"Created {created_count} progress records")
        
        return True
    except Exception as e:
        print(f"Error initializing question progress: {e}")
        db.session.rollback()
        return False

def get_adaptive_questions(quiz_slug, user_id, batch_size=20):
    """
    Get adaptive questions based on user's progress.
    Implements the cycling algorithm:
    1. Questions answered incorrectly get highest priority
    2. Unattempted questions get medium priority
    3. Completed questions get lowest priority
    4. Cycle resets when all questions are completed
    """
    try:
        # Load all questions for the course
        quiz_data = load_quiz_data_from_module(quiz_slug)
        if not quiz_data:
            print(f"Could not load quiz data for {quiz_slug}")
            return None
        
        all_questions = quiz_data.get('questions', [])
        print(f"Loaded {len(all_questions)} total questions for {quiz_slug}")
        
        # Initialize progress records if they don't exist
        initialize_question_progress(user_id, quiz_slug, all_questions)
        
        # Get user's progress for this quiz
        progress_records = UserQuestionProgress.query.filter_by(
            user_id=user_id,
            quiz_type=quiz_slug
        ).all()
        
        if not progress_records:
            print(f"No progress records found for user {user_id}, quiz {quiz_slug}")
            # Fallback to random selection
            return get_random_questions(all_questions, batch_size)
        
        # Create a mapping of question_id to progress record
        progress_map = {p.question_id: p for p in progress_records}
        
        # Categorize questions
        incorrect_questions = []
        unattempted_questions = []
        completed_questions = []
        
        for question in all_questions:
            q_id = str(question.get('id'))
            progress = progress_map.get(q_id)
            
            if not progress:
                # No progress record - treat as unattempted
                unattempted_questions.append(question)
            elif progress.needs_review:
                # Answered incorrectly, needs review
                incorrect_questions.append({
                    'question': question,
                    'priority_score': progress.priority_score,
                    'incorrect_attempts': progress.incorrect_attempts
                })
            elif progress.is_unattempted:
                # Never attempted
                unattempted_questions.append(question)
            else:
                # Completed correctly
                completed_questions.append(question)
        
        print(f"Question breakdown: {len(incorrect_questions)} incorrect, {len(unattempted_questions)} unattempted, {len(completed_questions)} completed")
        
        # Check if all questions are completed (cycle complete)
        if len(completed_questions) == len(all_questions):
            print("🎯 CYCLE COMPLETE! All questions answered correctly!")
            # Reset all progress for new cycle
            for progress in progress_records:
                progress.reset_for_new_cycle()
            print("All progress reset for new cycle")
            
            # After reset, all questions become unattempted again
            unattempted_questions = all_questions.copy()
            incorrect_questions = []
            completed_questions = []
        
        # Select questions based on priority
        selected_questions = []
        
        # 1. First, include incorrect questions (highest priority)
        # Sort by priority score (highest first)
        incorrect_questions.sort(key=lambda x: x['priority_score'], reverse=True)
        
        for item in incorrect_questions[:batch_size]:
            selected_questions.append(item['question'])
        
        print(f"Added {len(selected_questions)} incorrect questions")
        
        # 2. Then fill remaining slots with unattempted questions
        remaining_slots = batch_size - len(selected_questions)
        if remaining_slots > 0 and unattempted_questions:
            # Shuffle unattempted questions for variety
            random.shuffle(unattempted_questions)
            selected_questions.extend(unattempted_questions[:remaining_slots])
            print(f"Added {min(remaining_slots, len(unattempted_questions))} unattempted questions")
        
        # 3. If still need more questions, add completed ones (for review)
        if len(selected_questions) < batch_size:
            remaining = batch_size - len(selected_questions)
            if completed_questions:
                # Randomly select from completed questions
                random.shuffle(completed_questions)
                selected_questions.extend(completed_questions[:remaining])
                print(f"Added {min(remaining, len(completed_questions))} completed questions for review")
        
        # 4. If still no questions, something went wrong - use random
        if not selected_questions:
            print("No questions selected - falling back to random")
            return get_random_questions(all_questions, batch_size)
        
        # Randomize answer positions for multiple choice questions
        for question in selected_questions:
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
        
        # Calculate progress statistics
        total = len(all_questions)
        completed_count = len(completed_questions)
        progress_percentage = (completed_count / total * 100) if total > 0 else 0
        
        return {
            'success': True,
            'questions': selected_questions,
            'total_questions': total,
            'quiz_count': len(selected_questions),
            'course_code': quiz_data.get('course_code', QUIZ_COURSES.get(quiz_slug, {}).get('course_code', '')),
            'course_name': quiz_data.get('course_name', QUIZ_COURSES.get(quiz_slug, {}).get('name', '')),
            'passing_score': quiz_data.get('passing_score', 60),
            'progress': {
                'completed': completed_count,
                'incorrect': len(incorrect_questions),
                'unattempted': len(unattempted_questions),
                'total': total,
                'percentage': progress_percentage,
                'cycle_complete': completed_count == total
            }
        }
        
    except Exception as e:
        print(f"Error getting adaptive questions for {quiz_slug}: {str(e)}")
        traceback.print_exc()
        return {
            'success': False,
            'message': f'Error retrieving questions: {str(e)}'
        }

def get_random_questions(all_questions, batch_size=20):
    """Fallback: Get random questions"""
    try:
        if len(all_questions) < batch_size:
            batch_size = len(all_questions)
        
        quiz_questions = random.sample(all_questions, batch_size) if len(all_questions) > batch_size else all_questions.copy()
        
        # Randomize answer positions
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
            'progress': {
                'completed': 0,
                'incorrect': 0,
                'unattempted': len(all_questions),
                'total': len(all_questions),
                'percentage': 0,
                'cycle_complete': False
            }
        }
    except Exception as e:
        print(f"Error in get_random_questions: {e}")
        return None

def update_question_progress(user_id, quiz_type, question_id, was_correct):
    """Update or create progress record for a question"""
    try:
        progress = UserQuestionProgress.query.filter_by(
            user_id=user_id,
            quiz_type=quiz_type,
            question_id=question_id
        ).first()
        
        if not progress:
            # Create new progress record if it doesn't exist
            progress = UserQuestionProgress(
                user_id=user_id,
                quiz_type=quiz_type,
                question_id=question_id
            )
            db.session.add(progress)
        
        # Record the attempt
        progress.record_attempt(was_correct)
        
        print(f"Updated progress for user {user_id}, question {question_id}: {'Correct' if was_correct else 'Incorrect'}")
        return True
    except Exception as e:
        print(f"Error updating question progress: {e}")
        db.session.rollback()
        return False

def get_question_progress_summary(user_id, quiz_type):
    """Get progress summary for a specific quiz"""
    try:
        progress_records = UserQuestionProgress.query.filter_by(
            user_id=user_id,
            quiz_type=quiz_type
        ).all()
        
        if not progress_records:
            return {
                'total_questions': 0,
                'completed': 0,
                'incorrect': 0,
                'unattempted': 0,
                'percentage': 0,
                'cycle_complete': False,
                'current_cycle': 1
            }
        
        total = len(progress_records)
        completed = sum(1 for p in progress_records if p.is_completed)
        incorrect = sum(1 for p in progress_records if p.needs_review)
        unattempted = sum(1 for p in progress_records if p.is_unattempted)
        current_cycle = max([p.current_cycle for p in progress_records]) if progress_records else 1
        
        return {
            'total_questions': total,
            'completed': completed,
            'incorrect': incorrect,
            'unattempted': unattempted,
            'percentage': (completed / total * 100) if total > 0 else 0,
            'cycle_complete': completed == total if total > 0 else False,
            'current_cycle': current_cycle
        }
    except Exception as e:
        print(f"Error getting progress summary: {e}")
        return None

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
        
        # Get progress data for this quiz
        progress = get_question_progress_summary(current_user.id, slug)
        if progress:
            course_info['progress'] = progress
        
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
    """Take an interactive quiz with adaptive questions"""
    print(f"take_quiz called with slug: {quiz_slug}")
    
    if quiz_slug not in QUIZ_COURSES:
        flash('Quiz not found', 'error')
        return redirect(url_for('quizzes.quizzes'))
    
    quiz_info = QUIZ_COURSES[quiz_slug]
    print(f"Quiz info loaded: {quiz_info['name']}")
    
    # Get adaptive questions
    result = get_adaptive_questions(quiz_slug, current_user.id, 20)
    
    if not result or not result.get('success'):
        flash('Could not load quiz questions from course module. Please contact administrator.', 'error')
        return redirect(url_for('quizzes.quizzes'))
    
    quiz_data = {
        'questions': result['questions'],
        'passing_score': result.get('passing_score', 60),
        'course_code': result.get('course_code', quiz_info['course_code']),
        'course_name': result.get('course_name', quiz_info['name'])
    }
    
    print(f"Loaded {len(quiz_data['questions'])} adaptive questions")
    
    # Calculate question counts for template
    questions = quiz_data.get('questions', [])
    total_questions = len(questions)
    mc_questions = len([q for q in questions if q.get('type') == 'multiple_choice'])
    written_questions = len([q for q in questions if q.get('type') == 'written'])
    
    # Get progress summary
    progress = get_question_progress_summary(current_user.id, quiz_slug)
    
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
                         last_attempt=last_attempt,
                         progress=progress)

# ==============================================
# API ROUTES
# ==============================================

@quizzes_bp.route('/api/submit', methods=['POST'])
@login_required
def submit_quiz():
    """API endpoint to submit and grade quiz - WITH ADAPTIVE TRACKING"""
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
        incorrect_question_ids = []  # Track which questions were wrong
        
        print(f"=== GRADING START ===")
        print(f"Total questions to grade: {total_questions}")
        
        for i, question in enumerate(questions_asked):
            q_id = str(question.get('id', i+1))
            user_answer = answers.get(q_id, '')
            
            # If q_id not found, try with index
            if user_answer == '':
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
            was_correct = False
            
            if question_type == 'multiple_choice':
                correct_answer = question.get('correct_answer')
                options = question.get('options', [])
                
                # Handle case where correct_answer is None
                if correct_answer is None:
                    print(f"  WARNING: No correct answer specified")
                    result['correct_answer'] = 'Not specified'
                    result['is_correct'] = False
                    result['points'] = 0
                    incorrect_answers += 1
                    incorrect_question_ids.append(q_id)
                    print(f"  RESULT: ✗ INCORRECT (No correct answer in database)")
                
                else:
                    # Handle empty answer
                    if user_answer is None or str(user_answer).strip() == '':
                        result['is_correct'] = False
                        result['points'] = 0
                        incorrect_answers += 1
                        incorrect_question_ids.append(q_id)
                        print(f"  EMPTY ANSWER - Marked as incorrect")
                        
                    else:
                        # SIMPLE COMPARISON - treat ALL questions the same way
                        user_ans_str = str(user_answer).strip()
                        correct_ans_str = str(correct_answer).strip()
                        
                        # Convert to uppercase for case-insensitive comparison
                        user_upper = user_ans_str.upper()
                        correct_upper = correct_ans_str.upper()
                        
                        # SPECIAL HANDLING FOR TRUE/FALSE VARIATIONS
                        # Map common true/false variations to '1' and '0'
                        
                        # Normalize user answer
                        if user_upper in ['TRUE', 'T', 'YES', 'Y']:
                            user_normalized = '1'
                        elif user_upper in ['FALSE', 'F', 'NO', 'N']:
                            user_normalized = '0'
                        else:
                            user_normalized = user_ans_str  # Keep original
                        
                        # Normalize correct answer
                        if correct_upper in ['TRUE', 'T', 'YES', 'Y']:
                            correct_normalized = '1'
                        elif correct_upper in ['FALSE', 'F', 'NO', 'N']:
                            correct_normalized = '0'
                        elif isinstance(correct_answer, bool):
                            correct_normalized = '1' if correct_answer else '0'
                        else:
                            correct_normalized = correct_ans_str  # Keep original
                        
                        # Now compare the normalized values
                        # First try direct string comparison
                        if user_normalized == correct_normalized:
                            was_correct = True
                            print(f"  Direct match: '{user_normalized}' == '{correct_normalized}': True")
                        
                        # Handle letter answers (A, B, C, D) for multiple choice
                        elif user_normalized in ['A', 'B', 'C', 'D'] and correct_normalized in ['0', '1', '2', '3']:
                            letter_to_index = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
                            user_index = letter_to_index.get(user_normalized)
                            was_correct = (user_index == int(correct_normalized))
                            print(f"  Letter to index: '{user_normalized}' (index {user_index}) == '{correct_normalized}': {was_correct}")
                        
                        # Handle numeric string comparison
                        elif user_normalized in ['0', '1', '2', '3'] and correct_normalized in ['0', '1', '2', '3']:
                            was_correct = (user_normalized == correct_normalized)
                            print(f"  Numeric comparison: '{user_normalized}' == '{correct_normalized}': {was_correct}")
                        
                        # Last resort: case-insensitive string comparison
                        else:
                            was_correct = (user_upper == correct_upper)
                            print(f"  Case-insensitive: '{user_upper}' == '{correct_upper}': {was_correct}")
                        
                        # Update counters
                        if was_correct:
                            result['is_correct'] = True
                            result['points'] = 1
                            total_score += 1
                            correct_answers += 1
                            print(f"  RESULT: ✓ CORRECT! Total correct: {correct_answers}")
                        else:
                            result['is_correct'] = False
                            result['points'] = 0
                            incorrect_answers += 1
                            incorrect_question_ids.append(q_id)
                            print(f"  RESULT: ✗ INCORRECT")
                    
                    # Store correct answer text for display
                    try:
                        if isinstance(correct_answer, bool):
                            result['correct_answer'] = 'True' if correct_answer else 'False'
                        elif str(correct_answer).upper() in ['TRUE', 'T', '1']:
                            result['correct_answer'] = 'True'
                        elif str(correct_answer).upper() in ['FALSE', 'F', '0']:
                            result['correct_answer'] = 'False'
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
                
                was_correct = verification['is_correct']
                
                if was_correct:
                    result['is_correct'] = True
                    result['points'] = 1
                    total_score += 1
                    correct_answers += 1
                    print(f"  Written answer: ✓ CORRECT! Similarity: {verification['similarity']:.2f}")
                else:
                    result['is_correct'] = False
                    result['points'] = 0
                    incorrect_answers += 1
                    incorrect_question_ids.append(q_id)
                    print(f"  Written answer: ✗ INCORRECT! Similarity: {verification['similarity']:.2f}")
                
                result['similarity'] = verification['similarity']
                result['found_keywords'] = verification['found_keywords']
                result['correct_answer'] = question.get('correct_answer', '')
                result['expected_keywords'] = question.get('keywords', [])
            
            # Update question progress
            if was_correct is not None:
                update_question_progress(
                    user_id=current_user.id,
                    quiz_type=quiz_type,
                    question_id=q_id,
                    was_correct=was_correct
                )
            
            results.append(result)
        
        # Final validation
        print(f"\n=== GRADING COMPLETE ===")
        print(f"Total Questions: {total_questions}")
        print(f"Total Score: {total_score}")
        print(f"Correct Answers: {correct_answers}")
        print(f"Incorrect Answers: {incorrect_answers}")
        print(f"Incorrect Question IDs: {incorrect_question_ids}")
        
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
        
        # Get current cycle number from progress
        progress_records = UserQuestionProgress.query.filter_by(
            user_id=current_user.id,
            quiz_type=quiz_type
        ).all()
        current_cycle = max([p.current_cycle for p in progress_records]) if progress_records else 1
        
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
            'total_questions': total_questions,
            'cycle_number': current_cycle,
            'incorrect_question_ids': incorrect_question_ids
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
        
        # Get progress summary before saving
        progress_summary = get_question_progress_summary(current_user.id, quiz_type)
        
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
                attempt_date=datetime.now(),
                cycle_number=current_cycle,
                questions_asked=json.dumps(answered_ids),
                incorrect_questions=json.dumps(incorrect_question_ids)
            )
            
            db.session.add(quiz_attempt)
            db.session.commit()
            attempt_id = quiz_attempt.id
            print(f"SUCCESS: Quiz attempt saved to database with ID {attempt_id}")
            print(f"  Correct answers: {correct_answers}")
            print(f"  Incorrect answers: {incorrect_answers}")
            print(f"  Total questions: {total_questions}")
            print(f"  Cycle number: {current_cycle}")
            
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
            'cycle_number': current_cycle,
            'progress': progress_summary,
            'incorrect_question_ids': incorrect_question_ids,
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
    """API endpoint to get adaptive questions for a specific quiz"""
    if quiz_slug not in QUIZ_COURSES:
        return jsonify({'success': False, 'error': 'Quiz not found'}), 404
    
    try:
        count = int(request.args.get('count', 20))
        result = get_adaptive_questions(quiz_slug, current_user.id, count)
        
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
# PROGRESS API ENDPOINTS
# ==============================================

@quizzes_bp.route('/api/progress/<quiz_slug>')
@login_required
def get_progress(quiz_slug):
    """Get user's progress for a specific quiz"""
    if quiz_slug not in QUIZ_COURSES:
        return jsonify({'success': False, 'error': 'Quiz not found'}), 404
    
    try:
        progress = get_question_progress_summary(current_user.id, quiz_slug)
        
        if progress:
            # Get detailed progress for each question
            progress_records = UserQuestionProgress.query.filter_by(
                user_id=current_user.id,
                quiz_type=quiz_slug
            ).all()
            
            detailed_progress = [p.to_dict() for p in progress_records]
            
            return jsonify({
                'success': True,
                'summary': progress,
                'detailed': detailed_progress
            })
        else:
            return jsonify({
                'success': False,
                'message': 'Could not retrieve progress'
            }), 500
            
    except Exception as e:
        print(f"Error in get_progress: {e}")
        return jsonify({
            'success': False,
            'message': f'Error retrieving progress: {str(e)}'
        }), 500

@quizzes_bp.route('/api/progress/reset/<quiz_slug>')
@login_required
def reset_progress(quiz_slug):
    """Reset progress for a specific quiz (start new cycle)"""
    if quiz_slug not in QUIZ_COURSES:
        return jsonify({'success': False, 'error': 'Quiz not found'}), 404
    
    try:
        progress_records = UserQuestionProgress.query.filter_by(
            user_id=current_user.id,
            quiz_type=quiz_slug
        ).all()
        
        if not progress_records:
            return jsonify({
                'success': False,
                'message': 'No progress records found to reset'
            }), 404
        
        for progress in progress_records:
            progress.reset_for_new_cycle()
        
        return jsonify({
            'success': True,
            'message': 'Progress reset successfully. New cycle started.'
        })
        
    except Exception as e:
        print(f"Error resetting progress: {e}")
        db.session.rollback()
        return jsonify({
            'success': False,
            'message': f'Error resetting progress: {str(e)}'
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
            cycle_number = attempt.cycle_number or 1
            questions_asked = attempt.questions_asked_list if attempt.questions_asked else []
            incorrect_questions = attempt.incorrect_questions_list if attempt.incorrect_questions else []
            
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
                        cycle_number = quiz_metadata.get('cycle_number', attempt.cycle_number or 1)
                        incorrect_questions = quiz_metadata.get('incorrect_question_ids', incorrect_questions)
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
                'adaptive_metrics': adaptive_metrics,
                'cycle_number': cycle_number,
                'questions_asked_count': len(questions_asked),
                'incorrect_questions_count': len(incorrect_questions)
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
        cycle_number = attempt.cycle_number or 1
        
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
                    cycle_number = quiz_metadata.get('cycle_number', attempt.cycle_number or 1)
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
        
        # Get questions asked and incorrect
        questions_asked = attempt.questions_asked_list if attempt.questions_asked else []
        incorrect_questions = attempt.incorrect_questions_list if attempt.incorrect_questions else []
        
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
            'adaptive_metrics': adaptive_metrics,
            'cycle_number': cycle_number,
            'questions_asked': questions_asked,
            'incorrect_questions': incorrect_questions
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
            'cycle_number': attempt.cycle_number,
            'questions_asked': attempt.questions_asked,
            'incorrect_questions': attempt.incorrect_questions,
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
                            'match_with_db_score': quiz_data.get('correct_answers', 0) == attempt.score,
                            'cycle_number': quiz_data.get('cycle_number', 'NOT FOUND'),
                            'incorrect_question_ids': quiz_data.get('incorrect_question_ids', 'NOT FOUND')
                        }
                    else:
                        parsed_data['warning'] = 'NO quiz_data key found!'
                        parsed_data['full_structure'] = parsed
                        
            except Exception as e:
                parsed_data['parse_error'] = str(e)
        
        # Get current progress
        progress = get_question_progress_summary(current_user.id, attempt.quiz_type)
        
        return jsonify({
            'success': True,
            'raw': raw_data,
            'parsed': parsed_data,
            'current_progress': progress
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
                'has_results': bool(attempt.results),
                'cycle_number': attempt.cycle_number,
                'questions_asked_count': len(attempt.questions_asked_list) if attempt.questions_asked else 0,
                'incorrect_questions_count': len(attempt.incorrect_questions_list) if attempt.incorrect_questions else 0
            })
        
        # Get progress records
        progress_records = UserQuestionProgress.query.filter_by(user_id=current_user.id).all()
        progress_summary = {}
        for record in progress_records:
            if record.quiz_type not in progress_summary:
                progress_summary[record.quiz_type] = {
                    'total': 0,
                    'completed': 0,
                    'incorrect': 0,
                    'unattempted': 0,
                    'cycle': 1
                }
            progress_summary[record.quiz_type]['total'] += 1
            if record.is_completed:
                progress_summary[record.quiz_type]['completed'] += 1
            elif record.needs_review:
                progress_summary[record.quiz_type]['incorrect'] += 1
            elif record.is_unattempted:
                progress_summary[record.quiz_type]['unattempted'] += 1
            progress_summary[record.quiz_type]['cycle'] = max(
                progress_summary[record.quiz_type]['cycle'],
                record.current_cycle
            )
        
        return jsonify({
            'success': True,
            'user_id': current_user.id,
            'total_attempts_in_db': total_attempts,
            'attempts': attempts_data,
            'progress_summary': progress_summary,
            'total_progress_records': len(progress_records)
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