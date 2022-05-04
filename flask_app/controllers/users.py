from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.user import User

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/rosters')
def rosters():
    return render_template('rosters.html')

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')