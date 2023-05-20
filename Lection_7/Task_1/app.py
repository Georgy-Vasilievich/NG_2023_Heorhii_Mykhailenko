from flask import Flask
import secrets
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SESSION_TYPE'] = 'memcached'
app.secret_key = secrets.token_hex(32)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
