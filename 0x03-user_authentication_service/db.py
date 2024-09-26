#!/usr/bin/env python3
"""
Database setup using SQLAlchemy
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


def init_db():
    """Initialize the database and create tables."""
    db.create_all()


if __name__ == "__main__":
    with app.app_context():
        init_db()
