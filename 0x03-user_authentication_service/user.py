#!/usr/bin/env python3
"""
User model definition for a database table named 'users'
"""
from sqlalchemy import Column, Integer, String
from db import db


class User(db.Model):
    """User class to map the 'users' table."""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(250), nullable=False, unique=True)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
