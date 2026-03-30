from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'capsule123'

import os

DATABASE_URL = os.environ.get("DATABASE_URL")

import psycopg2

def get_db():
    return psycopg2.connect(DATABASE_URL)

def get_db():
    return mysql.connector.connect(**DB)

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('home'))
    return redirect(url_for('login'))

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        conn = get_db(); cur = conn.cursor()
        try:
            cur.execute("INSERT INTO users(username,email,password) VALUES(%s,%s,%s)",
                (request.form['username'], request.form['email'], request.form['password']))
            conn.commit()
            flash('Registered! Please login.', 'success')
            return redirect(url_for('login'))
        except:
            flash('User already exists.', 'danger')
        finally:
            cur.close(); conn.close()
    return render_template('register.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        conn = get_db(); cur = conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM users WHERE email=%s AND password=%s",
            (request.form['email'], request.form['password']))
        user = cur.fetchone(); cur.close(); conn.close()
        if user:
            session['user_id'] = user['id']
            session['username'] = user['username']
            return redirect(url_for('home'))
        flash('Wrong email or password.', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/home')
def home():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    conn = get_db(); cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM capsules WHERE user_id=%s ORDER BY created_at DESC", (session['user_id'],))
    capsules = cur.fetchall(); cur.close(); conn.close()
    return render_template('home.html', capsules=capsules, now=datetime.now())

@app.route('/submit', methods=['POST'])
def submit():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    conn = get_db(); cur = conn.cursor()
    cur.execute("INSERT INTO capsules(user_id,title,message,unlock_date) VALUES(%s,%s,%s,%s)",
        (session['user_id'], request.form['title'], request.form['message'], request.form['unlock_date']))
    conn.commit(); cur.close(); conn.close()
    flash('Capsule locked successfully!', 'success')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
