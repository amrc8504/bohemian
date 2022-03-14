from flask import Blueprint, render_template
from .forms import UserCreationForm
from app.models import User

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/signUp')
def signUp():
    return render_template('signUp.html')

@auth.route('/logIn')
def logIn():
    form = UserCreationForm()
    return render_template('logIn.html', form=form)