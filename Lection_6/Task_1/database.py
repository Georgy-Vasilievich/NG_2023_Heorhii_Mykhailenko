from markupsafe import escape
import bcrypt
import sqlite3

connection = sqlite3.connect('database.db', check_same_thread=False)

def initTables():
    connection.execute('CREATE TABLE IF NOT EXISTS users (id integer PRIMARY KEY, username text UNIQUE NOT NULL, password text NOT NULL)')
    connection.execute('CREATE TABLE IF NOT EXISTS articles (id integer PRIMARY KEY, author integer NOT NULL, timestamp datetime NOT NULL DEFAULT CURRENT_TIMESTAMP, header text NOT NULL, content text NOT NULL, FOREIGN KEY(author) REFERENCES users(id))')

def createUsers():
    password = bcrypt.hashpw('admin'.encode(), bcrypt.gensalt())
    connection.execute('INSERT OR IGNORE INTO users(username, password) VALUES("admin", ?)', (password,))

def insertArticle(author, header, content):
    connection.execute('INSERT INTO articles(author, header, content) VALUES(?, ?, ?)', (author, header, content))

def getArticles():
    result = ''
    cursor = connection.cursor()
    cursor.execute('SELECT author, timestamp, header, content FROM articles')
    rows = cursor.fetchall()
    for article in rows:
        getUsernameCursor = connection.cursor()
        getUsernameCursor.execute('SELECT username FROM users WHERE id = ?', (article[0],))
        username = getUsernameCursor.fetchone()[0]
        result += '<hr>\n    <p><h2>{}</h2><br>\nPosted by {} at {}<br>\n'.format(article[2], username, article[1])
        content = article[3].splitlines()
        for index, line in enumerate(content):
            result += '{}'.format(line)
            if index != len(content) - 1:
                result += '<br>'
        result += '</p>\n'
    return result

def auth(username, password):
    cursor = connection.cursor()
    cursor.execute('SELECT id, password FROM users WHERE username = ?', (username,))
    row = cursor.fetchone()
    if row:
        if bcrypt.checkpw(password.encode(), row[1]):
            return row[0]
    return 0
