from app import db
from datetime import datetime


class Articles(db.Model):
    __tablename__ = 'Articles'
    id = db.Column(db.Integer, primary_key=True)
    news_source = db.Column(db.String(500))
    URL = db.Column(db.String(500))
    news_content = db.Column(db.String(500))
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    article_category = db.relationship('Aricles_category', backref='Articles', lazy=True)


class Category(db.Model):
    __tablename__ = 'Category'
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(20))
    article_category = db.relationship('Aricles_category', backref='Category', lazy=True)


class Articles_category(db.Model):
    __tablename__ = 'Articles category'
    id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.Integer, db.ForeignKey('articles.id'))
    category_name = db.relationship(db.String(20), db.ForeignKey('category.name'))



