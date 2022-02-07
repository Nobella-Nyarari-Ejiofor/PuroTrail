from crypt import methods
from . import main
from flask import render_template 
from .forms import LoginForm , SignUpForm


@main.route('/', methods = ['GET','POST'])
def home():
  return render_template('home.html')
 

@main.route('/login' , methods = ['GET','POST'])
def login():
  form = LoginForm()

  return  render_template ('login.html', form = form)


  

