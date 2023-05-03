from flask import Flask, render_template, redirect, request, session, url_for
from markupsafe import escape
import secrets

app = Flask(__name__)

accounts = {}
messages = ''

@app.route('/', methods=['GET', 'POST'])
def chat():
    global messages
    if not 'account' in session or session['account'] not in accounts:
        return redirect(url_for('login'))
    if request.method == 'POST':
        account = escape(session['account'])
        message = escape(request.form.get('message')).splitlines()
        messages += '    <p><strong>{}</strong>: '.format(account)
        for index, line in enumerate(message):
            messages += '{}'.format(line)
            if index != len(message) - 1:
                messages += '<br>'
        messages += '</p>\n'
        
    return render_template('chat.html', messages=messages)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'account' in session and session['account'] in accounts:
        return redirect(url_for('chat'))
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if accounts.get(username) == password:
            session['account'] = username
            return redirect(url_for('chat'))
        else:
            return render_template('auth.html', error='Invalid credentials.')
    return render_template('auth.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'account' in session and session['account'] in accounts:
        return redirect(url_for('chat'))
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username in accounts:
            accounts[username] = password
            session['account'] = username
            return redirect(url_for('chat'))
        else:
            return render_template('auth.html', register=True, error='This username is already taken.')
    return render_template('auth.html', register=True)

@app.route('/logout', methods=['GET'])
def logout():
    if 'account' in session:
        session.pop('account')
    return redirect(url_for('chat'))

if __name__ == '__main__':
    app.secret_key = secrets.token_hex(32)
    app.config['SESSION_TYPE'] = 'memcached'
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True

    app.run()
