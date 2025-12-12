from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models import User
import requests
import json

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
@auth_bp.route('/index')
def index():
    if current_user.is_authenticated:
        return render_template('index.html')
    return redirect(url_for('auth.login'))

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    print("🔐 Login route called")
    
    if current_user.is_authenticated:
        print("✅ User already authenticated, redirecting to index")
        return redirect(url_for('auth.index'))
    
    if request.method == 'POST':
        print("📨 POST request received")
        print("📨 Content-Type:", request.content_type)
        print("📨 Form data:", dict(request.form))
        
        # Handle traditional form submission (email/password)
        email = request.form.get('email')
        password = request.form.get('password')
        
        if email and password:
            print(f"🔐 Traditional login attempt: {email}")
            
            # Find user in database
            user = User.query.filter_by(email=email).first()
            print(f"🔍 User found: {user}")
            
            if user:
                print(f"🔐 Checking password for user: {email}")
                print(f"🔐 Password hash exists: {user.password_hash is not None}")
                
                # Check if user has a password set (not a Firebase-only user)
                if user.password_hash is None:
                    flash('This account was created with Google Sign-In. Please use Google Sign-In to login.', 'error')
                    print(f"❌ User has no password set (Firebase-only user): {email}")
                elif user.check_password(password):
                    login_user(user, remember=True)
                    print(f"✅ Traditional login successful: {email}")
                    next_page = request.args.get('next')
                    if next_page:
                        return redirect(next_page)
                    return redirect(url_for('auth.index'))
                else:
                    flash('Invalid email or password', 'error')
                    print(f"❌ Password check failed for: {email}")
            else:
                flash('Invalid email or password', 'error')
                print(f"❌ User not found: {email}")
        else:
            flash('Please enter both email and password', 'error')
    
    # If GET request or failed POST, render login page
    return render_template('auth/login.html')

@auth_bp.route('/firebase-login', methods=['POST'])
def firebase_login():
    """Handle Firebase authentication entirely in backend"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'success': False, 'error': 'No JSON data provided'}), 400
            
        id_token = data.get('id_token')
        email = data.get('email')
        name = data.get('name')
        
        print(f"🔥 Firebase login attempt: {email}")
        print(f"📦 Received data - id_token: {bool(id_token)}, email: {email}, name: {name}")
        
        if not id_token:
            return jsonify({'success': False, 'error': 'No ID token provided'}), 400
        
        # Verify Firebase ID token
        firebase_verify_url = "https://identitytoolkit.googleapis.com/v1/accounts:lookup?key=AIzaSyAw4CCOFDlfsVxkAcg2YdshgEB-x3fKNLY"
        
        verify_response = requests.post(firebase_verify_url, json={
            'idToken': id_token
        })
        
        print(f"🔍 Firebase verification response status: {verify_response.status_code}")
        
        if verify_response.status_code != 200:
            print(f"❌ Firebase token verification failed: {verify_response.text}")
            return jsonify({'success': False, 'error': 'Invalid Firebase token'}), 401
        
        verify_data = verify_response.json()
        print(f"🔍 Firebase verification data: {verify_data}")
        
        if not verify_data.get('users'):
            return jsonify({'success': False, 'error': 'Invalid user data'}), 401
        
        firebase_user = verify_data['users'][0]
        firebase_uid = firebase_user['localId']
        verified_email = firebase_user.get('email', email)
        
        print(f"✅ Firebase token verified for: {verified_email}")
        
        # Find or create user in database
        user = User.query.filter_by(email=verified_email).first()
        if not user:
            print(f"➕ Creating new user: {verified_email}")
            user = User(
                email=verified_email, 
                name=name or verified_email.split('@')[0],
                firebase_uid=firebase_uid
            )
            # Firebase users don't get a password hash initially
            db.session.add(user)
            db.session.commit()
            print(f"✅ New user created: {verified_email}")
        else:
            print(f"✅ User found: {verified_email}")
            # Update Firebase UID if not set
            if not user.firebase_uid:
                user.firebase_uid = firebase_uid
                db.session.commit()
        
        # Log the user in
        login_user(user, remember=True)
        print(f"✅ User logged in successfully: {verified_email}")
        
        return jsonify({
            'success': True,
            'message': 'Login successful!',
            'redirect': url_for('auth.index')
        })
        
    except Exception as e:
        print(f"❌ Firebase login error: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': f'Login failed: {str(e)}'
        }), 500

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('auth.index'))
        
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        print(f"📝 Registration attempt: {email}")
        
        # Basic validation
        if not email or not name or not password:
            flash('Please fill in all fields', 'error')
            return render_template('auth/register.html')
            
        if password != confirm_password:
            flash('Passwords do not match', 'error')
            return render_template('auth/register.html')
        
        # Check if user already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already exists. Please login instead.', 'error')
            print(f"❌ Email already exists: {email}")
            return render_template('auth/register.html')
        else:
            # Create new user
            try:
                user = User(email=email, name=name)
                user.set_password(password)  # This will set the password hash
                db.session.add(user)
                db.session.commit()
                
                flash('Registration successful! Please login.', 'success')
                print(f"✅ User registered: {email}")
                return redirect(url_for('auth.login'))
            except Exception as e:
                db.session.rollback()
                flash('Registration failed. Please try again.', 'error')
                print(f"❌ Registration error: {str(e)}")
                return render_template('auth/register.html')
    
    return render_template('auth/register.html')

@auth_bp.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if current_user.is_authenticated:
        return redirect(url_for('auth.index'))
        
    if request.method == 'POST':
        email = request.form.get('email')
        # In a real application, you would send a password reset email here
        flash('If an account exists with this email, a password reset link has been sent.', 'info')
        print(f"📧 Password reset requested for: {email}")
        return redirect(url_for('auth.login'))
    
    return render_template('auth/forgot_password.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out successfully.', 'info')
    return redirect(url_for('auth.login'))

# Test endpoint for debugging
@auth_bp.route('/test-users')
def test_users():
    """Debug endpoint to check users in database"""
    if not current_user.is_authenticated:
        return "Not authenticated"
    
    users = User.query.all()
    result = []
    for user in users:
        result.append({
            'id': user.id,
            'email': user.email,
            'name': user.name,
            'has_password': user.password_hash is not None,
            'firebase_uid': user.firebase_uid
        })
    
    return jsonify(result)