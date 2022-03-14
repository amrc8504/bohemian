from app import app
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def aboutPage():
    return render_template('about.html')

@app.route('/browse')
def browse():
    return render_template('browse.html')