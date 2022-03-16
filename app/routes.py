from app import app
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def aboutPage():
    return render_template('about.html')

@app.route('/api/v2/pokemon/')
def pokedex():
    
    return {'hi' : "there"}