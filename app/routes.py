from flask import render_template, redirect, session, url_for, request, flash
from app import app
from app.forms import *
from flask_login import current_user, login_user
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db
from app.models import User, Post, Comments
from sqlalchemy import func, select
from flask_login import logout_user
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from urllib.parse import urlsplit

#Route for login page
@app.route('/login', methods=['GET', 'POST'])   
def loginPage():
    if current_user.is_authenticated:	#Checks if current user is already authenticated
        return redirect(url_for('profilePage'))
    form = SignInForm()
    if form.validate_on_submit():	#Checks if login form is valid
        user = db.session.scalar(sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data): #Checks if user/username exists and if the password is correct if that user exists
            flash("Incorrect username or password.", 'error')
            return redirect(url_for('loginPage'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))	#Redirects to home page
    return render_template("login.html", title='Log In', form=form)

#Route for index (the home page)
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form=newPost()
    if form.validate_on_submit():	#Checks if the new post form is valid (has been filled out correctly)
        if current_user.is_authenticated:	#Makes sure that the person making the post is logged in
            post = Post(title=form.title.data, body=form.post.data, author=current_user)
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            flash("Please sign in to create a post.", 'error')	#If person was not signed in when making a post redirect the user to the login page, and flash a message asking them to log in
            return redirect(url_for('loginPage'))
    posts = db.session.scalars(sa.select(Post).order_by(Post.timestamp.desc())).all()	#Query the database for the posts
    length = len(posts)+1
    commentsList = [0]*length	#make a list for number of comments that is the same length as the posts query result
    for post in posts:
        commentsList[post.id] = db.session.scalars(sa.select(func.count()).select_from(Comments).where(post.id==Comments.post_id)).all()[0]	#Get number of comments for each post in the query
    searchform = SearchForm()
    if searchform.validate_on_submit():	#Get data from submitted form
        searched = searchform.textToSearch.data
        posts2 = Post.query.filter(Post.body.contains(searched))	#Query the database
        return render_template("search.html", searchform=searchform, searched=searched, posts2=posts2, title='Home Page', posts=posts, comments=commentsList, form=form)	#If a user searched, return the search results
    return render_template('index.html', title='Home Page', posts=posts, comments=commentsList, form=form)	#Else return the home page

#Pass Stuff to Navbar
@app.context_processor
def base():
    searchform = SearchForm()
    return dict(searchform=searchform)

#Route for the sign up page
@app.route('/sign-up', methods=['GET', 'POST'])
def signUpPage():
    if current_user.is_authenticated:	#if a user that is already logged in tries to resignup, redirect them to the profile page
        return redirect(url_for('profilePage'))
    form = SignUpForm()
    if form.validate_on_submit():	#Check that the data submitted is valid
        user = User(username=form.username.data, email=form.email.data, pronouns=form.pronouns.data, ThinkPads=0) #If valid submission, create a user (inital thinkpad count is set to zero)
        user.set_password(form.password.data)
        db.session.add(user)	#Add user to the database
        db.session.commit()
        flash("Sign up successful! Please log in.", 'success')	#Flash a success message and redirect user to the login page
        return redirect(url_for('loginPage'))
    return render_template("sign-up.html", title="Sign Up", form=form)


#Route for the profile page
@app.route('/profile', methods=['GET', 'POST'])
def profilePage():
    if current_user.is_authenticated:	#If user is logged in
        name = current_user.username
        pronouns = current_user.pronouns
        thinkpads = current_user.ThinkPads
        postsNum = db.session.scalars(sa.select((func.count())).select_from(Post).where(Post.user_id==current_user.id)).first()	#Collect number of posts made by the user
        commentsNum = db.session.scalars(sa.select((func.count())).select_from(Comments).where(Comments.user_id==current_user.id)).first()	#Collect number of comments/responses made by the user
        form = editThinkPads()
        if form.validate_on_submit():	#Checks if the new thinkpad number is valid
            current_user.ThinkPads = form.number.data
            db.session.commit()	#Updates number of thinkpad user has in the database
            return redirect(url_for('profilePage'))
    else:
        return redirect(url_for('loginPage'))
    posts = db.session.scalars(sa.select(Post).select_from(Post).where(Post.user_id==current_user.id).order_by(Post.timestamp.desc())).all()	#Selects the posts made by the user
    comments = db.session.scalars(sa.select(Comments).select_from(Comments).where(Comments.user_id==current_user.id).order_by(Comments.timestamp.desc())).all()	#Selects the comments made by the user
    return render_template("profile.html", name=name, postsNum=postsNum, commentsNum=commentsNum, pronouns=pronouns, thinkpads=thinkpads, form=form, posts=posts, comments=comments)

#Route for veiwing a post
@app.route('/post/<post_id>', methods=['GET', 'POST'])
def postview(post_id):
    post = db.session.scalars(sa.select(Post).where(Post.id==post_id)).first()	#Selects the post
    commentdb = db.session.scalars(sa.select(Comments).select_from(Comments).where(Comments.post_id==post_id).order_by(Comments.timestamp.desc())).all()	#Selects the comments from the post
    commentNumber = db.session.scalars(sa.select(func.count()).select_from(Comments).where(post_id==Comments.post_id)).all()[0]	#Collects the number of comments made on the post
    form = newComment()
    if form.validate_on_submit():	#Checks that the new comment form is valid
        if not current_user.is_authenticated:	#Checks that the user making the comment is valid
            flash("Please log in to post a comment.", 'error')	#If user is not logged in flash alert message and redirect to login page
            return redirect(url_for('loginPage'))
        comment = Comments(body=form.commentBody.data, post_id=post_id, user_id=current_user.id)	#If user is logged in, create the comment
        db.session.add(comment)	#Add the comment to the database
        db.session.commit()
        return redirect(url_for('postview', post_id=post_id))
    return render_template('post-view.html', title='Post View', post=post, form=form, comments=commentdb, commentNumber=commentNumber)

#Route for viewing another users profile
@app.route('/user/<username>', methods=['GET'])
def userview(username):
    if current_user.is_authenticated:	#Checks to see if user is currently logged in
        user = db.session.scalars(sa.select(User).where(User.username==username)).first()
        if(user.id == current_user.id):	#If user is logged in, and are trying to visit their own userview, redirect them to profile page
            return redirect(url_for('profilePage'))
    user = db.session.scalars(sa.select(User).where(User.username==username)).first()
    name = user.username
    pronouns = user.pronouns
    thinkpads = user.ThinkPads
    postsNum = db.session.scalars(sa.select((func.count())).select_from(Post).where(Post.user_id==user.id)).first()
    commentsNum = db.session.scalars(sa.select((func.count())).select_from(Comments).where(Comments.user_id==user.id)).first()
    posts = db.session.scalars(sa.select(Post).select_from(Post).where(Post.user_id==user.id).order_by(Post.timestamp.desc())).all()
    comments = db.session.scalars(sa.select(Comments).select_from(Comments).where(Comments.user_id==user.id).order_by(Comments.timestamp.desc())).all()
    return render_template("userview.html", name=name, postsNum=postsNum, commentsNum=commentsNum, pronouns=pronouns, thinkpads=thinkpads, posts=posts, comments=comments)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('loginPage'))

