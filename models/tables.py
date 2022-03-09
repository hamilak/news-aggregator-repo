import os
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

connection_string = os.getenv('database_url')

app = Flask(__name__)


app.config['SECRET_KEY'] = 'potato'
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = connection_string
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Articles(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    news_title = db.Column(db.String(500))
    url = db.Column(db.String(1000))
    news_content = db.Column(db.String(5000))
    published_at = db.Column(db.DateTime, default=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    # category = db.relationship('Categories', backref='article', lazy=True)

    def __init__(self, news_title, url, news_content, published_at, category_id):
        self.news_title = news_title
        self.url = url
        self.news_content = news_content
        self.published_at = published_at
        self.category_id = category_id


class Categories(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(20))
    article = db.relationship('Articles', backref='categories', lazy=True)

    def __init__(self, category_name):
        self.category_name = category_name
