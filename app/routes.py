from flask import render_template, flash, redirect
from app import app
from app.forms import *
import pprint



@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def loginPage():
	form = SignInForm()
	return render_template("login.html", title='Log In', form=form)

@app.route('/sign-up', methods=['GET', 'POST'])
def signUpPage():
    form = SignUpForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, pronouns={}, you def can\'t read my password. Wait. Shi- {}'.format(form.username.data, form.pronouns.data, form.password.data))
        return redirect('/index')

    return render_template("sign-up.html", title="Sign Up", form=form)
