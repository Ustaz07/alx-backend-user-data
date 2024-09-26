#!/usr/bin/env python3
"""Authentication service."""
from models import User
from db import db

class Auth:
    """Auth class that handles user authentication logic."""

    @staticmethod
    def register_user(username: str, password: str) -> User:
        """Register a new user."""
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def authenticate_user(username: str, password: str) -> bool:
        """Authenticate user with username and password."""
        user = User.query.filter_by(username=username).first()
        if user and user.verify_password(password):
            return True
        return False
