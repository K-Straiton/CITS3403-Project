from flask import app, render_template, redirect, session, url_for, request, flash
# from app import flaskApp
from app.forms import *
#from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_user
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db
from app.models import User, Post, Comments
from sqlalchemy import func, select
from flask_login import logout_user
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from app.blueprints import main

from flask import request
from urllib.parse import urlsplit

#@app.route('/')
#@app.route('/index')
#def index():
#	return render_template("index.html")
# @app.route('/index', methods=['GET', 'POST'])
# @app.route('/', methods=['GET', 'POST'])
# def indexPage():
#     return render_template("index.html")

@main.route('/login', methods=['GET', 'POST'])
def loginPage():
    if current_user.is_authenticated:
        return redirect(url_for('main.profilePage'))
    form = SignInForm()
    if form.validate_on_submit():
        user = db.session.scalar(sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash("Incorrect username or password.", 'error')
            return redirect(url_for('main.loginPage'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('main.index'))
#    if form.validate_on_submit():
#        # hashedPassword = generate_password_hash('form.username.data')
#        # password = generate_password_hash('test')
#        # if(check_password_hash(password, form.password.data)):
#        return redirect('/index')
    return render_template("login.html", title='Log In', form=form)

@main.route('/', methods=['GET', 'POST'])
@main.route('/index', methods=['GET', 'POST'])
def index():
    form=newPost()
    if form.validate_on_submit():
        if current_user.is_authenticated:
            post = Post(title=form.title.data, body=form.post.data, author=current_user)
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('main.index'))
        else:
            flash("Please sign in to create a post.", 'error')
            return redirect(url_for('main.loginPage'))
    posts = db.session.scalars(sa.select(Post).order_by(Post.timestamp.desc())).all()
    length = len(posts)+1
    commentsList = [0]*length
    for post in posts:
        commentsList[post.id] = db.session.scalars(sa.select(func.count()).select_from(Comments).where(post.id==Comments.post_id)).all()[0]
    searchform = SearchForm()
    if searchform.validate_on_submit():
        #Get data from submitted form
        searched = searchform.textToSearch.data
        #Query the database
        posts2 = Post.query.filter(Post.body.contains(searched))
        return render_template("search.html", searchform=searchform, searched=searched, posts2=posts2, title='Home Page', posts=posts, comments=commentsList, form=form)
    return render_template('index.html', title='Home Page', posts=posts, comments=commentsList, form=form)

# Pass Stuff to Navbar
@app.context_processor
def base():
    searchform = SearchForm()
    return dict(searchform=searchform)

@main.route('/sign-up', methods=['GET', 'POST'])
def signUpPage():
    if current_user.is_authenticated:
        return redirect(url_for('main.profilePage'))
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, pronouns=form.pronouns.data, ThinkPads=0)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Sign up successful! Please log in.", 'success')
        return redirect(url_for('main.loginPage'))

    return render_template("sign-up.html", title="Sign Up", form=form)



@main.route('/profile', methods=['GET', 'POST'])
def profilePage():
    if current_user.is_authenticated:
        # name = request.args.get('name', None)
        name = current_user.username
        pronouns = current_user.pronouns
        thinkpads = current_user.ThinkPads
        postsNum = db.session.scalars(sa.select((func.count())).select_from(Post).where(Post.user_id==current_user.id)).first()
        commentsNum = db.session.scalars(sa.select((func.count())).select_from(Comments).where(Comments.user_id==current_user.id)).first()
        form = editThinkPads()
        
        if form.validate_on_submit():
            current_user.ThinkPads = form.number.data
            db.session.commit()
            return redirect(url_for('main.profilePage'))
    else:
        return redirect(url_for('main.loginPage'))
    posts = db.session.scalars(sa.select(Post).select_from(Post).where(Post.user_id==current_user.id).order_by(Post.timestamp.desc())).all()
    comments = db.session.scalars(sa.select(Comments).select_from(Comments).where(Comments.user_id==current_user.id).order_by(Comments.timestamp.desc())).all()
    return render_template("profile.html", name=name, postsNum=postsNum, commentsNum=commentsNum, pronouns=pronouns, thinkpads=thinkpads, form=form, posts=posts, comments=comments)

@main.route('/post/<post_id>', methods=['GET', 'POST'])
def postview(post_id):
    post = db.session.scalars(sa.select(Post).where(Post.id==post_id)).first()
    commentdb = db.session.scalars(sa.select(Comments).select_from(Comments).where(Comments.post_id==post_id).order_by(Comments.timestamp.desc())).all()
    commentNumber = db.session.scalars(sa.select(func.count()).select_from(Comments).where(post_id==Comments.post_id)).all()[0]
    # commentdb = db.session.scalars(sa.select(Comments).select_from(Comments).where(Comments.post_id==post_id).order_by(Comments.timestamp.desc())).all()
    form = newComment()
    if form.validate_on_submit():
        if not current_user.is_authenticated:
            flash("Please log in to post a comment.", 'error')
            return redirect(url_for('main.loginPage'))
        comment = Comments(body=form.commentBody.data, post_id=post_id, user_id=current_user.id)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('main.postview', post_id=post_id))
    return render_template('post-view.html', title='Post View', post=post, form=form, comments=commentdb, commentNumber=commentNumber)

@main.route('/user/<username>', methods=['GET'])
def userview(username):
    if current_user.is_authenticated:
        user = db.session.scalars(sa.select(User).where(User.username==username)).first()
        if(user.id == current_user.id):
            return redirect(url_for('main.profilePage'))
    user = db.session.scalars(sa.select(User).where(User.username==username)).first()
    name = user.username
    pronouns = user.pronouns
    thinkpads = user.ThinkPads
    postsNum = db.session.scalars(sa.select((func.count())).select_from(Post).where(Post.user_id==user.id)).first()
    commentsNum = db.session.scalars(sa.select((func.count())).select_from(Comments).where(Comments.user_id==user.id)).first()
    posts = db.session.scalars(sa.select(Post).select_from(Post).where(Post.user_id==user.id).order_by(Post.timestamp.desc())).all()
    comments = db.session.scalars(sa.select(Comments).select_from(Comments).where(Comments.user_id==user.id).order_by(Comments.timestamp.desc())).all()
    return render_template("userview.html", name=name, postsNum=postsNum, commentsNum=commentsNum, pronouns=pronouns, thinkpads=thinkpads, posts=posts, comments=comments)

@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.loginPage'))

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     # ...
#     if form.validate_on_submit():
#         user = db.session.scalar(
#             sa.select(User).where(User.username == form.username.data))
#         if user is None or not user.check_password(form.password.data):
#             return redirect(url_for('login'))
#         login_user(user, remember=form.remember_me.data)
#         next_page = request.args.get('next')
#         if not next_page or urlsplit(next_page).netloc != '':
#             next_page = url_for('index')
#         return redirect(next_page)
#     # ...
