from flask import Blueprint, render_template, request, flash, redirect, url_for, send_file, current_app
from flask_login import login_required, current_user
import os
from app import db
from app.models import Course, Resource
from werkzeug.utils import secure_filename

resources_bp = Blueprint('resources', __name__)

# Course data for each individual course
COURSE_DATA = {
    'computer-organization-architecture': {
        'title': 'Computer Organization & Architecture',
        'code': 'BCP 203',
        'image_url': 'https://images.unsplash.com/photo-1517077304055-6e89abbf09b0?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2069&q=80',
        'videos': [
            {'id': 'Ol8D69VKX2k', 'title': 'Introduction to Computer Architecture', 'channel': 'Neso Academy'},
            {'id': 'GRInNLx3Tug', 'title': 'Basics of Computer Architecture', 'channel': 'Neso Academy'},
            {'id': '6_PHIL4LZEU', 'title': 'Classifications of Computer Architecture', 'channel': 'Neso Academy'},
            {'id': 'PujjqfUhtNo', 'title': 'Introduction to Memory', 'channel': 'Neso Academy'},
            {'id': 'lQcU4WwVALI', 'title': 'Memory Hierarchy & Interfacing', 'channel': 'Neso Academy'}
        ],
        'pdfs': [
            {'title': 'Computer Architecture Basics', 'size': '2.4 MB', 'url': '/static/pdf/COA.pdf'},
            {'title': 'CPU Design Principles', 'size': '3.1 MB', 'url': '/static/pdf/CO1.pdf'},
            {'title': 'Memory Systems Guide', 'size': '1.8 MB', 'url': '/static/pdf/COb.pdf'},
            {'title': 'I/O Systems Overview', 'size': '2.7 MB', 'url': '/static/pdf/COc.pdf'}
        ]
    },
    'logic-critical-thinking': {
        'title': 'Logic & Critical Thinking',
        'code': 'ATU 203',
        'image_url': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80',
        'videos': [
            {'id': 'RyqFD5OAJ40', 'title': 'Introduction to Logical Reasoning', 'channel': 'Philosophy Made Easy'},
            {'id': 'qVeyjW2J5Cc', 'title': 'Deductive vs Inductive Reasoning', 'channel': 'Critical Thinking'},
            {'id': '1N3TROKMOiQ', 'title': 'Logical Fallacies Explained', 'channel': 'Logic Matters'},
            {'id': 'ypw0L0-0_IM', 'title': 'Problem Solving Strategies', 'channel': 'Think Better'}
        ],
        'pdfs': [
            {'title': 'Logic Fundamentals', 'size': '1.9 MB', 'url': 'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf'},
            {'title': 'Critical Thinking Exercises', 'size': '2.2 MB', 'url': 'https://www.africau.edu/images/default/sample.pdf'},
            {'title': 'Logical Fallacies Guide', 'size': '1.5 MB', 'url': 'https://www.orimi.com/pdf-test.pdf'}
        ]
    },
    
    'data-communication-networks': {
        'title': 'Data Communication & Networks',
        'code': 'BCP 105',
        'image_url': 'https://images.unsplash.com/photo-1544197150-b99a580bb7a8?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80',
        'videos': [
            {'id': 'qiQR5rTSshw', 'title': 'Networking Fundamentals', 'channel': 'Network Engineer'},
            {'id': 'rL8R2RW6GZk', 'title': 'TCP/IP Protocol Suite', 'channel': 'Networking Explained'},
            {'id': 'EkN7b1nJpV4', 'title': 'Network Topologies', 'channel': 'IT Pro'},
            {'id': '4_zSIXb7tLQ', 'title': 'Wireless Networking', 'channel': 'Tech Tutorials'},
            {'id': 'YJGGZADh1Ck', 'title': 'Network Security Basics', 'channel': 'Cyber Security'}
        ],
        'pdfs': [
            {'title': 'Networking Basics', 'size': '2.8 MB', 'url': 'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf'},
            {'title': 'TCP/IP Protocol Guide', 'size': '3.2 MB', 'url': 'https://www.africau.edu/images/default/sample.pdf'},
            {'title': 'Network Security Handbook', 'size': '2.5 MB', 'url': 'https://www.orimi.com/pdf-test.pdf'},
            {'title': 'Wireless Technologies', 'size': '2.1 MB', 'url': 'https://www.clickdimensions.com/links/TestPDFfile.pdf'}
        ]
    },
    'principles-entrepreneurship': {
        'title': 'Principles of Entrepreneurship',
        'code': 'ATU 201',
        'image_url': 'https://images.unsplash.com/photo-1552664730-d307ca884978?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80',
        'videos': [
            {'id': 'pC5l5j2u9SQ', 'title': 'What is Entrepreneurship', 'channel': 'Business School'},
            {'id': 'XejcDaDE-UU', 'title': 'Business Plan Development', 'channel': 'Startup Guide'},
            {'id': 'Gj_zVW9qk4s', 'title': 'Market Research Strategies', 'channel': 'Entrepreneurship 101'},
            {'id': 'c6yf81C6H0w', 'title': 'Funding Your Startup', 'channel': 'Venture Capital'},
            {'id': '0yKDTU96A7w', 'title': 'Building Your Brand', 'channel': 'Marketing Masters'}
        ],
        'pdfs': [
            {'title': 'Business Plan Template', 'size': '1.7 MB', 'url': 'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf'},
            {'title': 'Market Analysis Guide', 'size': '2.3 MB', 'url': 'https://www.africau.edu/images/default/sample.pdf'},
            {'title': 'Funding Strategies', 'size': '1.9 MB', 'url': 'https://www.orimi.com/pdf-test.pdf'},
            {'title': 'Entrepreneurial Case Studies', 'size': '2.6 MB', 'url': 'https://www.clickdimensions.com/links/TestPDFfile.pdf'}
        ]
    },
    'principles-sustainability': {
        'title': 'Principles of Sustainability',
        'code': 'BCB 209',
        'image_url': 'https://images.unsplash.com/photo-1568992688065-536aad8a12f6?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2069&q=80',
        'videos': [
            {'id': 'zx04Kl8y4dE', 'title': 'Introduction to Sustainability', 'channel': 'Environmental Science'},
            {'id': 'B5NiTN0chj0', 'title': 'Sustainable Development Goals', 'channel': 'UN Sustainable Dev'},
            {'id': 'ixIo8W0c7cU', 'title': 'Circular Economy Principles', 'channel': 'Green Business'},
            {'id': 'Er7B6oVdUjE', 'title': 'Corporate Sustainability', 'channel': 'Business Ethics'},
            {'id': 'W8PcwyY0I70', 'title': 'Sustainable Energy Solutions', 'channel': 'Clean Energy'}
        ],
        'pdfs': [
            {'title': 'Sustainability Principles', 'size': '2.1 MB', 'url': 'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf'},
            {'title': 'SDG Implementation Guide', 'size': '2.9 MB', 'url': 'https://www.africau.edu/images/default/sample.pdf'},
            {'title': 'Circular Economy Handbook', 'size': '2.4 MB', 'url': 'https://www.orimi.com/pdf-test.pdf'},
            {'title': 'Environmental Impact Assessment', 'size': '3.1 MB', 'url': 'https://www.clickdimensions.com/links/TestPDFfile.pdf'}
        ]
    },
    'web-development-technologies': {
        'title': 'Web Development Technologies',
        'code': 'BCP 207',
        'image_url': 'https://images.unsplash.com/photo-1627398242454-45a1465c2479?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2074&q=80',
        'videos': [
            {'id': 'qz0aGYrrlhU', 'title': 'HTML5 Crash Course', 'channel': 'Web Dev Simplified'},
            {'id': '1Rs2ND1ryYc', 'title': 'CSS3 Fundamentals', 'channel': 'CSS Master'},
            {'id': 'W6NZfCO5SIk', 'title': 'JavaScript Basics', 'channel': 'JS Tutorials'},
            {'id': 'DIVfDZZeGxM', 'title': 'Responsive Web Design', 'channel': 'Frontend Masters'},
            {'id': 'Oe421EPjeBE', 'title': 'Introduction to React', 'channel': 'React Explained'},
            {'id': 'jBzwzrDvZ18', 'title': 'Backend Development with Node.js', 'channel': 'Full Stack'}
        ],
        'pdfs': [
            {'title': 'HTML5 Cheat Sheet', 'size': '1.2 MB', 'url': 'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf'},
            {'title': 'CSS3 Complete Guide', 'size': '3.5 MB', 'url': 'https://www.africau.edu/images/default/sample.pdf'},
            {'title': 'JavaScript Fundamentals', 'size': '2.8 MB', 'url': 'https://www.orimi.com/pdf-test.pdf'},
            {'title': 'Responsive Design Principles', 'size': '2.3 MB', 'url': 'https://www.clickdimensions.com/links/TestPDFfile.pdf'},
            {'title': 'React.js Handbook', 'size': '3.7 MB', 'url': 'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf'}
        ]
    },
    'programming-cpp': {
        'title': 'Programming with C++',
        'code': 'BCP 201',
        'image_url': 'https://images.unsplash.com/photo-1542831371-29b0f74f9713?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80',
        'videos': [
            {'id': 'vLnPwxZdW4Y', 'title': 'C++ Basics for Beginners', 'channel': 'C++ Tutorials'},
            {'id': 'Rub-JsjMhWY', 'title': 'Object-Oriented Programming in C++', 'channel': 'OOP Master'},
            {'id': 'iVLQeWbgbXs', 'title': 'C++ Memory Management', 'channel': 'Advanced C++'},
            {'id': 'w7xj1lMhS2Q', 'title': 'STL and Data Structures', 'channel': 'C++ Standard Library'},
            {'id': 'mUQZ1qmKlLY', 'title': 'C++ Best Practices', 'channel': 'Code Quality'},
            {'id': '8jLOx1BdDSE', 'title': 'Advanced C++ Features', 'channel': 'C++ Experts'}
        ],
        'pdfs': [
            {'title': 'C++ Syntax Reference', 'size': '1.8 MB', 'url': '/static/pdf/C++.pdf'},
            {'title': 'OOP in C++ Guide', 'size': '3.2 MB', 'url': 'https://www.africau.edu/images/default/sample.pdf'},
            {'title': 'STL Handbook', 'size': '2.7 MB', 'url': 'https://www.orimi.com/pdf-test.pdf'},
            {'title': 'C++ Programming Exercises', 'size': '2.1 MB', 'url': 'https://www.clickdimensions.com/links/TestPDFfile.pdf'},
            {'title': 'Advanced C++ Techniques', 'size': '3.4 MB', 'url': 'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf'}
        ]
    }

}

@resources_bp.route('/resources')
@login_required
def resources():
    # Convert course data to list for template
    courses = []
    for slug, data in COURSE_DATA.items():
        courses.append({
            'slug': slug,
            'name': data['title'],
            'code': data['code'],
            'image_url': data['image_url'],
            'video_count': len(data['videos']),
            'pdf_count': len(data['pdfs'])
        })
    return render_template('resources/resources.html', courses=courses)

@resources_bp.route('/resources/<course_slug>')
@login_required
def course_resources(course_slug):
    print(f"Looking for course: {course_slug}")  # Debug line
    
    if course_slug not in COURSE_DATA:
        print(f"Course '{course_slug}' not found in COURSE_DATA")  # Debug line
        flash('Course not found', 'error')
        return redirect(url_for('resources.resources'))
    
    course_data = COURSE_DATA[course_slug]
    template_name = f'resources/{course_slug}.html'
    print(f"Rendering template: {template_name}")  # Debug line
    
    return render_template(template_name, 
                         course=course_data,
                         course_slug=course_slug)