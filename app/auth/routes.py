from flask import Blueprint, render_template

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/signUp')
def signUp():
    return render_template('signUp.html')

@auth.route('/logIn')
def logIn():
    return render_template('logIn.html')