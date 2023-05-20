from app import app
from database import *
from flask import Flask, render_template, redirect, request, session, url_for
from markupsafe import escape

with app.app_context():
    createUsers()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'account' in session:
            author = session['account']
            header = escape(request.form.get('header'))
            content = escape(request.form.get('content'))
            insertArticle(author, header, content)
        else:
            return redirect(url_for('login'))

    return render_template('index.html', authenticated=True if 'account' in session else False, articles=getArticles())

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'account' in session:
        return redirect(url_for('index'))
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        account = auth(username, password)

        if account:
            session['account'] = account
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Invalid credentials.')
    return render_template('login.html')

@app.route('/logout', methods=['GET'])
def logout():
    if 'account' in session:
        session.pop('account')
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
