from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class SignInForm(FlaskForm):
	username = StringField("Username",validators=[DataRequired()])
	password = StringField("Password",validators=[DataRequired()])
	logIn = SubmitField("Log In")

class SignUpForm(FlaskForm):
	username = StringField("Username",validators=[DataRequired()])
	password = StringField("Password",validators=[DataRequired()])
	signUp = SubmitField("Sign Up")
#   STILL NEED TO ADD PRONOUNS TO THIS FORM