from flask import render_template, flash, redirect, session, url_for, request
from app import app
from app.forms import *
#from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_user
import sqlalchemy as sa
from app import db
from app.models import User

from flask_login import logout_user

from flask import request
from urllib.parse import urlsplit

#@app.route('/')
#@app.route('/index')
#def index():
#	return render_template("index.html")
@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def loginPage():
    if current_user.is_authenticated:
        return redirect(url_for('profilePage', name=current_user.username, pronouns=current_user.pronouns, thinkpads=current_user.ThinkPads))
    form = SignInForm()
    if form.validate_on_submit():
        user = db.session.scalar(sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password {}'.format(form.remember_me.data))
            return redirect(url_for('loginPage'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('profilePage', name=user.username, pronouns=user.pronouns, thinkpads=user.ThinkPads))
#    if form.validate_on_submit():
#        # hashedPassword = generate_password_hash('form.username.data')
#        # password = generate_password_hash('test')
#        # if(check_password_hash(password, form.password.data)):
#        flash('Login requested for user {}, you def can\'t read my password. Wait. Shi- {}'.format(form.username.data, form.password.data))
#        return redirect('/index')
    return render_template("login.html", title='Log In', form=form)

@app.route('/sign-up', methods=['GET', 'POST'])
def signUpPage():
    if current_user.is_authenticated:
        return redirect(url_for('profilePage', name=current_user.username, pronouns=current_user.pronouns, thinkpads=current_user.ThinkPads))
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, pronouns=form.pronouns.data, ThinkPads=0)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('loginPage'))
    #     # Username = form.username.data
    #     # Pronouns = form.pronouns.data
    #     # session['Username'] = form.username.data
    #     # session['Pronouns'] = form.pronouns.data
    #     # return redirect(url_for('.profileFunc', Username=Username, Pronouns=Pronouns))
    #     return redirect(url_for('profilePage', name=form.username.data, pronouns=form.pronouns.data))

    return render_template("sign-up.html", title="Sign Up", form=form)


@app.route('/profile')
def profilePage():
    name = request.args.get('name', None)
    pronouns = request.args.get('pronouns')
    thinkpads = request.args.get('thinkpads')

    return render_template("profile.html", name=name, pronouns=pronouns, thinkpads=thinkpads)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('loginPage'))

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     # ...
#     if form.validate_on_submit():
#         user = db.session.scalar(
#             sa.select(User).where(User.username == form.username.data))
#         if user is None or not user.check_password(form.password.data):
#             flash('Invalid username or password')
#             return redirect(url_for('login'))
#         login_user(user, remember=form.remember_me.data)
#         next_page = request.args.get('next')
#         if not next_page or urlsplit(next_page).netloc != '':
#             next_page = url_for('index')
#         return redirect(next_page)
#     # ...