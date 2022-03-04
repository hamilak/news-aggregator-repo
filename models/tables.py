from app import db
from datetime import datetime


class Articles(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    news_source = db.Column(db.String(500))
    URL = db.Column(db.String(500))
    news_content = db.Column(db.String(500))
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    category = db.relationship('Category', backref='article', lazy=True)

    def __init__(self, news_source, URL, news_content, updated_at, category_id):
        self.news_source = news_source
        self.URL = URL
        self.news_content = news_content
        self.updated_at = updated_at
        self.category_id = category_id


class Categories(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(20))
    article = db.relationship('Articles', backref='category', lazy=True)

    def __init__(self, category_name):
        self.category_name = category_name


db.create_all()
db.session.commit()





