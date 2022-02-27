import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)
DB_NAME = 'database.db'
app.config['SECRET_KEY'] = 'potato'
app.config['SQLAlCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'


class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    news_source = db.Column(db.String())
    URL = db.Column(db.String())
    news_content = db.Column(db.String())
    updated_at = db.Column(db.DateTime)

class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String())

class Articles_category(db.Model):
    pass
