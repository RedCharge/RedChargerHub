from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from app import db
from app.models import Course

courses_bp = Blueprint('courses', __name__)

@courses_bp.route('/')
@courses_bp.route('/course')
@login_required
def courses():
    user_courses = Course.query.filter_by(user_id=current_user.id).all()
    return render_template('courses/courses.html', courses=user_courses)

@courses_bp.route('/timetable')
@login_required
def timetable():
    user_courses = Course.query.filter_by(user_id=current_user.id).all()
    return render_template('timetable.html', courses=user_courses)



@courses_bp.route('/add_course', methods=['GET', 'POST'])
@login_required
def add_course():
    if request.method == 'POST':
        name = request.form.get('name')
        days = ','.join(request.form.getlist('days'))
        start_time = request.form.get('start_time')
        end_time = request.form.get('end_time')
        
        course = Course(
            name=name,
            days=days,
            start_time=start_time,
            end_time=end_time,
            user_id=current_user.id
        )
        
        db.session.add(course)
        db.session.commit()
        flash('Course added successfully!')
        return redirect(url_for('courses.courses'))
    
    return render_template('courses/add_course.html')

@courses_bp.route('/delete_course/<int:course_id>')
@login_required
def delete_course(course_id):
    course = Course.query.filter_by(id=course_id, user_id=current_user.id).first()
    if course:
        db.session.delete(course)
        db.session.commit()
        flash('Course deleted successfully!')
    return redirect(url_for('courses.courses'))
