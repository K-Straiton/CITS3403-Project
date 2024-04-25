from flask import render_template, flash, redirect, session, url_for, request
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
    if form.validate_on_submit():
        flash('Login requested for user {}, you def can\'t read my password. Wait. Shi- {}'.format(form.username.data, form.password.data))
        return redirect('/index')
    return render_template("login.html", title='Log In', form=form)

@app.route('/sign-up', methods=['GET', 'POST'])
def signUpPage():
    form = SignUpForm()
    if form.validate_on_submit():
        # Username = form.username.data
        # Pronouns = form.pronouns.data
        # session['Username'] = form.username.data
        # session['Pronouns'] = form.pronouns.data
        # return redirect(url_for('.profileFunc', Username=Username, Pronouns=Pronouns))
        return redirect(url_for('profilePage', name=form.username.data, pronouns=form.pronouns.data))

    return render_template("sign-up.html", title="Sign Up", form=form)


@app.route('/profile')
def profilePage():
    name = request.args.get('name', None)
    pronouns = request.args.get('pronouns')

    return render_template("profile.html", name=name, pronouns=pronouns)
