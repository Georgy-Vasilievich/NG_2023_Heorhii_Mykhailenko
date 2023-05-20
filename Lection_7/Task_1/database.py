from app import app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import bcrypt

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    username = db.Column(db.Text, unique = True, nullable = False)
    password = db.Column(db.Text, nullable = False)

class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    author = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    timestamp = db.Column(db.DateTime(timezone=True), nullable = False, server_default=db.func.current_timestamp())
    header = db.Column(db.Text, nullable = False)
    content = db.Column(db.Text, nullable = False)

def createUsers():
    try:
        password = bcrypt.hashpw('admin'.encode(), bcrypt.gensalt())
        db.session.add(User(username = 'admin',
                            password = password))
        db.session.commit()
    except:
        pass

def insertArticle(author, header, content):
    db.session.add(Article(author = author,
                           header = header,
                           content = content))
    db.session.commit()

def getArticles():
    result = ''
    articles = Article.query.all()
    for article in articles:
        username = User.query.get(article.author).username
        result += '''
    <hr>
    <h2>{}</h2>
    <p>
    Posted by {} at {}<br>
    '''.format(article.header, username, article.timestamp)
        content = article.content.splitlines()
        for index, line in enumerate(content):
            result += '{}'.format(line)
            if index != len(content) - 1:
                result += '<br>\n    '
        result += '</p>\n'
    return result

def auth(username, password):
    user = User.query.filter_by(username=username).first()
    if user:
        if bcrypt.checkpw(password.encode(), user.password):
            return user.id
    print(user)
    return 0
