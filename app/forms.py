from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField, RadioField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, InputRequired
import sqlalchemy as sa
from app import db
from app.models import User

class SignInForm(FlaskForm):
	username = StringField("Username",validators=[DataRequired()])
	password = StringField("Password",validators=[DataRequired()])
	remember_me = BooleanField('Remember Me')
	logIn = SubmitField("Log In")

class SignUpForm(FlaskForm):
	username = StringField("Username",validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField("Password",validators=[DataRequired()])
	password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
	signUp = SubmitField("Sign Up")
	pronouns = RadioField("Pronouns:", validators=[InputRequired(message=None)], choices=[("She/Her", "She/Her"), ("He/Him", "He/Him"), ("They/Them","They/Them")])
	
	def validate_username(self, username):
		user = db.session.scalar(sa.select(User).where(
			User.username == username.data))
		if user is not None:
			raise ValidationError('Please use a different username.')

	def validate_email(self, email):
		user = db.session.scalar(sa.select(User).where(
			User.email == email.data))
		
		if user is not None:
			raise ValidationError('Please use a different email address.')

class editThinkPadCount(FlaskForm):
	ThinkPadCount = IntegerField("Number of ThinkPads", validators=[DataRequired()])
	editCount = SubmitField("Submit")
