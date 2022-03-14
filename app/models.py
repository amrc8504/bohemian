from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(250), nullable=False)
    post = db.relationship('Post', backref="Seller", lazy=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

class Post():
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    image = db.Column(db.String(500), nullable=False)
    description = db.Column(db.String(500))
    date_Posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, title, image, caption):
        self.title = title
        self.image = image
        self.caption = caption