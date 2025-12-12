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
            'db_quiz_id': self.db_quiz_id
        }
    
    def get_detailed_results(self):
        """Get detailed results including question-by-question data"""
        results = self.to_dict()
        results['answers'] = self.answers_data
        results['detailed_results'] = self.results_data
        return results

    def __repr__(self):
        return f'<QuizAttempt {self.quiz_name} - {self.grade} ({self.percentage}%)>'

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))