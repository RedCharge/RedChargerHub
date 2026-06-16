from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import json

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    name = db.Column(db.String(100), nullable=False)
    firebase_uid = db.Column(db.String(128), unique=True)
    
    courses = db.relationship('Course', backref='user', lazy=True)
    quiz_attempts = db.relationship('QuizAttempt', backref='user', lazy=True)
    question_progress = db.relationship('UserQuestionProgress', backref='user', lazy=True)
    
    def set_password(self, password):
        """Set password hash for the user"""
        if password:
            self.password_hash = generate_password_hash(password)
        else:
            raise ValueError("Password cannot be empty")
    
    def check_password(self, password):
        """Check if password matches the hash"""
        if not self.password_hash:
            print(f"❌ No password hash set for user: {self.email}")
            return False
        return check_password_hash(self.password_hash, password)

    def get_quiz_stats(self):
        """Get quiz statistics for this user"""
        attempts = QuizAttempt.query.filter_by(user_id=self.id).all()
        
        if not attempts:
            return {
                'total_attempts': 0,
                'average_score': 0,
                'best_score': 0,
                'passed_quizzes': 0,
                'total_quizzes': 0
            }
        
        total_attempts = len(attempts)
        total_score = sum(attempt.score for attempt in attempts)
        total_possible = sum(attempt.total_questions for attempt in attempts)
        average_score = (total_score / total_possible * 100) if total_possible > 0 else 0
        best_score = max(attempt.percentage for attempt in attempts)
        passed_quizzes = sum(1 for attempt in attempts if attempt.percentage >= 60)
        unique_quizzes = len(set(attempt.quiz_type for attempt in attempts))
        
        return {
            'total_attempts': total_attempts,
            'average_score': round(average_score, 2),
            'best_score': round(best_score, 2),
            'passed_quizzes': passed_quizzes,
            'unique_quizzes': unique_quizzes
        }
    
    def get_question_progress_summary(self, quiz_type):
        """Get progress summary for a specific quiz"""
        progress = UserQuestionProgress.query.filter_by(
            user_id=self.id,
            quiz_type=quiz_type
        ).all()
        
        total = len(progress)
        completed = sum(1 for p in progress if p.is_completed)
        incorrect = sum(1 for p in progress if not p.is_completed and p.attempts > 0)
        unattempted = sum(1 for p in progress if p.attempts == 0)
        
        return {
            'total_questions': total,
            'completed': completed,
            'incorrect': incorrect,
            'unattempted': unattempted,
            'progress_percentage': (completed / total * 100) if total > 0 else 0,
            'cycle_complete': completed == total if total > 0 else False
        }

    def __repr__(self):
        return f'<User {self.email}>'

class Course(db.Model):
    __tablename__ = 'courses'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    days = db.Column(db.String(100))
    start_time = db.Column(db.String(50))
    end_time = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # REMOVED: description = db.Column(db.Text)  # This column doesn't exist in your database
    
    resources = db.relationship('Resource', backref='course', lazy=True)
    quizzes = db.relationship('Quiz', backref='course', lazy=True)
    quiz_attempts = db.relationship('QuizAttempt', backref='course', lazy=True)

    def __repr__(self):
        return f'<Course {self.name}>'

class Resource(db.Model):
    __tablename__ = 'resources'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    filename = db.Column(db.String(300))
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Resource {self.title}>'

class Quiz(db.Model):
    __tablename__ = 'quizzes'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    questions = db.Column(db.Text)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    passing_score = db.Column(db.Integer, default=60)
    time_limit = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    @property
    def questions_data(self):
        """Get questions as Python object"""
        if self.questions:
            try:
                return json.loads(self.questions)
            except json.JSONDecodeError:
                return []
        return []
    
    @questions_data.setter
    def questions_data(self, value):
        """Set questions from Python object"""
        self.questions = json.dumps(value) if value else None

    def __repr__(self):
        return f'<Quiz {self.title}>'

class QuizAttempt(db.Model):
    __tablename__ = 'quiz_attempts'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    quiz_type = db.Column(db.String(50), nullable=False)
    quiz_name = db.Column(db.String(200), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    total_questions = db.Column(db.Integer, nullable=False)
    percentage = db.Column(db.Float, nullable=False)
    grade = db.Column(db.String(5), nullable=False)
    answers = db.Column(db.Text)
    results = db.Column(db.Text)
    attempt_date = db.Column(db.DateTime, default=datetime.utcnow)
    
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=True)
    db_quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.id'), nullable=True)
    
    # New fields for tracking adaptive quiz cycles
    cycle_number = db.Column(db.Integer, default=1)
    questions_asked = db.Column(db.Text)  # JSON array of question IDs asked in this attempt
    incorrect_questions = db.Column(db.Text)  # JSON array of question IDs answered incorrectly
    
    @property
    def answers_data(self):
        """Get answers as Python object"""
        if self.answers:
            try:
                return json.loads(self.answers)
            except json.JSONDecodeError:
                return {}
        return {}
    
    @answers_data.setter
    def answers_data(self, value):
        """Set answers from Python object"""
        self.answers = json.dumps(value) if value else None
    
    @property
    def results_data(self):
        """Get results as Python object"""
        if self.results:
            try:
                return json.loads(self.results)
            except json.JSONDecodeError:
                return []
        return []
    
    @results_data.setter
    def results_data(self, value):
        """Set results from Python object"""
        self.results = json.dumps(value) if value else None
    
    @property
    def questions_asked_list(self):
        """Get questions asked as Python list"""
        if self.questions_asked:
            try:
                return json.loads(self.questions_asked)
            except json.JSONDecodeError:
                return []
        return []
    
    @questions_asked_list.setter
    def questions_asked_list(self, value):
        """Set questions asked from Python list"""
        self.questions_asked = json.dumps(value) if value else None
    
    @property
    def incorrect_questions_list(self):
        """Get incorrect questions as Python list"""
        if self.incorrect_questions:
            try:
                return json.loads(self.incorrect_questions)
            except json.JSONDecodeError:
                return []
        return []
    
    @incorrect_questions_list.setter
    def incorrect_questions_list(self, value):
        """Set incorrect questions from Python list"""
        self.incorrect_questions = json.dumps(value) if value else None
    
    @property
    def is_passed(self):
        """Check if quiz was passed (≥60%)"""
        return self.percentage >= 60
    
    def to_dict(self):
        """Convert quiz attempt to dictionary for API responses"""
        return {
            'id': self.id,
            'quiz_type': self.quiz_type,
            'quiz_name': self.quiz_name,
            'score': self.score,
            'total_questions': self.total_questions,
            'percentage': round(self.percentage, 2),
            'grade': self.grade,
            'is_passed': self.is_passed,
            'attempt_date': self.attempt_date.strftime('%Y-%m-%d %H:%M'),
            'course_id': self.course_id,
            'db_quiz_id': self.db_quiz_id,
            'cycle_number': self.cycle_number,
            'questions_asked': len(self.questions_asked_list) if self.questions_asked else 0,
            'incorrect_count': len(self.incorrect_questions_list) if self.incorrect_questions else 0
        }
    
    def get_detailed_results(self):
        """Get detailed results including question-by-question data"""
        results = self.to_dict()
        results['answers'] = self.answers_data
        results['detailed_results'] = self.results_data
        results['questions_asked_list'] = self.questions_asked_list
        results['incorrect_questions_list'] = self.incorrect_questions_list
        return results

    def __repr__(self):
        return f'<QuizAttempt {self.quiz_name} - {self.grade} ({self.percentage}%)>'


class UserQuestionProgress(db.Model):
    """
    Tracks individual question progress for each user in the adaptive quiz system.
    This enables the cycling algorithm where questions are repeated until answered correctly.
    """
    __tablename__ = 'user_question_progress'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    quiz_type = db.Column(db.String(100), nullable=False)  # e.g., 'emerging-frontiers'
    question_id = db.Column(db.String(50), nullable=False)  # The question's ID from the course module
    
    # Attempt tracking
    attempts = db.Column(db.Integer, default=0)  # Total attempts for this question
    correct_attempts = db.Column(db.Integer, default=0)  # Number of correct attempts
    incorrect_attempts = db.Column(db.Integer, default=0)  # Number of incorrect attempts
    last_attempt_correct = db.Column(db.Boolean, default=False)  # Was the last attempt correct?
    last_attempt_date = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Cycle tracking
    current_cycle = db.Column(db.Integer, default=1)  # Which cycle is the user on?
    cycles_completed = db.Column(db.Integer, default=0)  # How many times has this question been correctly answered?
    first_correct_date = db.Column(db.DateTime)  # When was it first answered correctly?
    last_incorrect_date = db.Column(db.DateTime)  # When was it last answered incorrectly?
    
    # Metadata
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Unique constraint to prevent duplicate progress records
    __table_args__ = (
        db.UniqueConstraint('user_id', 'quiz_type', 'question_id', 
                           name='unique_user_quiz_question'),
        db.Index('idx_user_quiz_question', 'user_id', 'quiz_type', 'question_id'),
        db.Index('idx_user_quiz_progress', 'user_id', 'quiz_type', 'last_attempt_correct'),
    )
    
    @property
    def is_completed(self):
        """Check if this question has been completed correctly in the current cycle"""
        return self.last_attempt_correct and self.attempts > 0
    
    @property
    def needs_review(self):
        """Check if this question needs review (incorrect in current cycle)"""
        return not self.last_attempt_correct and self.attempts > 0
    
    @property
    def is_unattempted(self):
        """Check if this question has never been attempted"""
        return self.attempts == 0
    
    @property
    def success_rate(self):
        """Calculate success rate for this question"""
        if self.attempts == 0:
            return 0.0
        return (self.correct_attempts / self.attempts) * 100
    
    @property
    def priority_score(self):
        """
        Calculate priority score for adaptive selection.
        Higher score = should be shown sooner.
        """
        score = 0
        
        # Incorrect questions get highest priority
        if self.needs_review:
            score += 100
            
            # More attempts = higher priority (stuck on this question)
            score += self.incorrect_attempts * 10
            
            # Recent incorrect attempts = higher priority
            if self.last_incorrect_date:
                days_since = (datetime.utcnow() - self.last_incorrect_date).days
                if days_since < 1:
                    score += 20  # Very recent
                elif days_since < 3:
                    score += 10  # Recent
        
        # Unattempted questions get medium priority
        elif self.is_unattempted:
            score += 50
        
        # Completed questions get lowest priority (but still show occasionally for review)
        else:
            score += 10
            # Random element for review
            import random
            score += random.randint(0, 10)
        
        return score
    
    def record_attempt(self, was_correct):
        """Record a new attempt for this question"""
        self.attempts += 1
        self.last_attempt_date = datetime.utcnow()
        self.last_attempt_correct = was_correct
        
        if was_correct:
            self.correct_attempts += 1
            if self.first_correct_date is None:
                self.first_correct_date = datetime.utcnow()
        else:
            self.incorrect_attempts += 1
            self.last_incorrect_date = datetime.utcnow()
        
        self.updated_at = datetime.utcnow()
        db.session.commit()
    
    def reset_for_new_cycle(self):
        """Reset progress for a new cycle (all questions need to be answered again)"""
        self.last_attempt_correct = False
        self.cycles_completed += 1
        self.current_cycle += 1
        self.attempts = 0
        self.correct_attempts = 0
        self.incorrect_attempts = 0
        self.first_correct_date = None
        self.last_incorrect_date = None
        self.updated_at = datetime.utcnow()
        db.session.commit()
    
    def to_dict(self):
        """Convert to dictionary for API responses"""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'quiz_type': self.quiz_type,
            'question_id': self.question_id,
            'attempts': self.attempts,
            'correct_attempts': self.correct_attempts,
            'incorrect_attempts': self.incorrect_attempts,
            'last_attempt_correct': self.last_attempt_correct,
            'last_attempt_date': self.last_attempt_date.isoformat() if self.last_attempt_date else None,
            'current_cycle': self.current_cycle,
            'cycles_completed': self.cycles_completed,
            'is_completed': self.is_completed,
            'needs_review': self.needs_review,
            'is_unattempted': self.is_unattempted,
            'success_rate': self.success_rate,
            'priority_score': self.priority_score,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

    def __repr__(self):
        return f'<UserQuestionProgress user={self.user_id} quiz={self.quiz_type} q={self.question_id} attempts={self.attempts}>'


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))