from flask import render_template
from app import app
from app.forms import *


@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def loginPage():
	form = SignInForm()
	return render_template("login.html", title='Log In', form=form)

@app.route('/sign-up')
def signUpPage():
    form = SignUpForm()
    return render_template("sign-up.html", title="Sign Up", form=form)
