from flask import Flask, request, redirect, render_template
import sqlite3
import bcrypt

app = Flask(__name__)

def connect_db():
    return sqlite3.connect('users.db')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password'].encode('utf-8')
        con = connect_db()
        cur = con.cursor()
        query = "SELECT password FROM users WHERE username=?"
        cur.execute(query, (username,))
        user = cur.fetchone()
        con.close()
        if user and bcrypt.checkpw(password, user[0].encode('utf-8')):
            return redirect('/welcome')
        else:
            return render_template('index.html', error='Invalid login')
    return redirect('/')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password'].encode('utf-8')
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        con = connect_db()
        cur = con.cursor()
        query = "INSERT INTO users (username, password) VALUES (?, ?)"
        cur.execute(query, (username, hashed.decode('utf-8')))
        con.commit()
        con.close()
        return redirect('/')
    return render_template('signup.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

if __name__ == '__main__':
    app.run()
