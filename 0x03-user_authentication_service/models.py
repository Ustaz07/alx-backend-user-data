#!/usr/bin/env python3
"""User model definition."""
from db import db
import bcrypt

class User(db.Model):
    """User class that defines the database model for a user."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)

    def __init__(self, username: str, password: str):
        """Initialize user with hashed password."""
        self.username = username
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def verify_password(self, password: str) -> bool:
        """Verify the password."""
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash)
