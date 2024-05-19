from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField, RadioField, TextAreaField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, InputRequired, Length, NumberRange
import sqlalchemy as sa
from app import db
from app.models import User

#User log in/sign in form
class SignInForm(FlaskForm):
	username = StringField("Username",validators=[DataRequired()])
	password = StringField("Password",validators=[DataRequired()])
	remember_me = BooleanField('Remember Me')
	logIn = SubmitField("Log In")

#Sign up form
class SignUpForm(FlaskForm):
	username = StringField("Username",validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField("Password",validators=[DataRequired()])
	password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password', "Passwords must match.")])
	signUp = SubmitField("Sign Up")
	pronouns = RadioField("Pronouns:", validators=[InputRequired(message=None)], choices=[("She/Her", "She/Her"), ("He/Him", "He/Him"), ("They/Them","They/Them")])

	def validate_username(self, username):	#Check to see if username is already in use
		user = db.session.scalar(sa.select(User).where(
			User.username == username.data))
		if user is not None:
			raise ValidationError('Username already in use.')

	def validate_email(self, email):	#Check that email submitted is a valid email
		user = db.session.scalar(sa.select(User).where(
			User.email == email.data))
		if user is not None:
			raise ValidationError('Email already in use.')

#Create new post form
class newPost(FlaskForm):
    title = TextAreaField('Write Title', validators=[DataRequired(), Length(min=1, max=140)])
    post = TextAreaField('Write Post', validators=[DataRequired(), Length(min=1, max=1400)])
    submit = SubmitField('Post!')

#Create new comment form
class newComment(FlaskForm):
	commentBody = TextAreaField('Write comment', validators=[DataRequired(), Length(min=1, max=1400)])
	submit = SubmitField('Reply!')

#Search form
class SearchForm(FlaskForm):
	textToSearch = StringField('Search Field Placeholder', validators=[DataRequired(), Length(min=1, max=1400)])
	submitSearch = SubmitField('🔍︎')

#Edit number of thinkpads form
class editThinkPads(FlaskForm):
    number = IntegerField('Number of ThinkPads', validators=[NumberRange(min=0, max=9000000)])
    submit = SubmitField('Submit')

