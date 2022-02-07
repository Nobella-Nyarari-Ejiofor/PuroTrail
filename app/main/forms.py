from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,SubmitField
from wtforms.validators import InputRequired , Length , Email


class LoginForm(FlaskForm):
  username = StringField('username' , validators = [InputRequired(), Length(min = 6 ,max =15)])
  password = StringField('password' , validators = [InputRequired(), Length(min = 6 ,max =15)])
  submit = SubmitField('Sign In')

class SignUpForm(FlaskForm):
  first_name = StringField('first_name' , validators = [InputRequired(), Length(min = 5 , max =15)])
  last_name = StringField('last_name' , validators= [InputRequired(), Length (min =5 ,max =15)])
  username = StringField('username' , validators = [InputRequired() , Length(min= 4 , max =15)])
  email = StringField('email' , validators= [InputRequired(), Email(message = "Invalid Email") , Length(min =5 , max=15)])
  submit = SubmitField('Sign In')


