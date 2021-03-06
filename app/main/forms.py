from flask_wtf import FlaskForm, csrf
from wtforms import StringField, TextAreaField,SubmitField, SelectField
from wtforms.validators import InputRequired , Length , Email



class LoginForm(FlaskForm):
  username = StringField('username' , validators = [InputRequired(), Length(min = 3 ,max =15)])
  password = StringField('password' , validators = [InputRequired(), Length(min = 3 ,max =15)])
  submit = SubmitField('Sign In')

class SignUpForm(FlaskForm):
  first_name = StringField('first_name' , validators = [InputRequired(), Length(min = 5 , max =15)])
  last_name = StringField('last_name' , validators= [InputRequired(), Length (min =5 ,max =15)])
  username = StringField('username' , validators = [InputRequired() , Length(min= 4 , max =15)])
  password = StringField('password' , validators = [InputRequired() , Length(min= 4 , max =15)])
  email = StringField('email' , validators= [InputRequired(), Email(message = "Invalid Email") , Length(min =5 , max=100)])
  register = SubmitField('Register')


class PitchesForm(FlaskForm):
   pitch_words = StringField('Write your Pitch' , validators = [InputRequired(), Length(min = 50, max =200)])
   category_field = SelectField("Category", choices =[(1,'Pickup Line'),(2,'Product Pitch'),(3,'Promotional Pitch'),(4,'Interview')],validators=[InputRequired()])
   post = SubmitField('post pitch')

class CommentsForm(FlaskForm):
  comment_words = StringField('comment',validators = [InputRequired(), Length(min = 5 , max =15)])
  submit = SubmitField('submit')
  
