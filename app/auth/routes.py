from flask import Blueprint, redirect, render_template, url_for, flash
from .forms import RegistrationForm, LogInForm

auth = Blueprint('auth', __name__, template_folder='auth_templates')


@auth.route('/signUp', methods=['POST', 'GET'])
def signUp():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account successfully created for {form.username.data}!', category='success')
        return redirect(url_for('auth.login'))
    return render_template('signUp.html', title='Register', form=form)


@auth.route('/logIn', methods=['POST', 'GET'])
def login():
    form = LogInForm()
    if form.validate_on_submit():
        if form.email.data == 'jonathan89@gmail.com' and form.password.data == '123456':
            flash(f'Welcome, {form.email.data}!', category='success')
            return redirect(url_for('home'))
        else:
            flash(f'Login unsuccessful for {form.email.data}.', category='danger')
            return redirect(url_for('auth.login'))
    return render_template('logIn.html', title='Login', form=form)
