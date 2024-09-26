#!/usr/bin/env python3
"""Flask app for user authentication."""
from flask import Flask, request, redirect, render_template, jsonify, make_response
from auth import Auth
from db import app, db

app.secret_key = 'secret_key'  # Used for cookies and session management

@app.route('/')
def home():
    """Home page."""
    return 'Welcome to the User Authentication Service.'

@app.route('/register', methods=['POST'])
def register():
    """Handle user registration."""
    data = request.form
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    try:
        Auth.register_user(username, password)
        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        return jsonify({"error": "User registration failed"}), 500

@app.route('/login', methods=['POST'])
def login():
    """Handle user login."""
    data = request.form
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    if Auth.authenticate_user(username, password):
        response = make_response(redirect('/dashboard'))
        response.set_cookie('username', username)  # Setting a cookie
        return response
    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/dashboard')
def dashboard():
    """Protected route that requires login."""
    username = request.cookies.get('username')
    if not username:
        return jsonify({"error": "Unauthorized access"}), 403
    return f'Welcome to the dashboard, {username}.'

@app.route('/logout')
def logout():
    """Handle user logout."""
    response = make_response(redirect('/'))
    response.set_cookie('username', '', expires=0)  # Remove cookie
    return response

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)
