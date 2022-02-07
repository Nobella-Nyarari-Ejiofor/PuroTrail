from . import main
from app import db, login_manager
from flask import render_template , redirect , url_for , flash
from .forms import LoginForm , SignUpForm
from werkzeug.security import check_password_hash, generate_password_hash
from ..models import User
from flask_login import login_user


# defining the login manager function that takes in a user id
@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id)).first()

@main.before_app_first_request
def create_all():
  db.create_all()

@main.route('/', methods = ['GET','POST'])
def home():
  return render_template('home.html')
 

@main.route('/login' , methods = ['GET','POST'])
def login():
  form = LoginForm()
  # Check validation of the form
  if form.validate_on_submit():
    user = User.query.filter_by(username = form.username.data).first()
    # if user exists
    if user:
      # Compare the passwords.
      if check_password_hash(user.password,form.password.data):
        # /loging the user in
        login_user(user)
        # redirecting to the pitch page
        return redirect(url_for('pitches'))
      
      return ("Invalid username or password")
    return("The username doesn't exist")


  return  render_template ('login.html', form = form)

@main.route('/signup' , methods =['GET', 'POST'])
def signup():
  form = SignUpForm()
  if form.validate_on_submit():
    first_name = form.first_name.data
    last_name = form.last_name.data
    username = form.username.data
    email = form.email.data
    password = form.password.data
    
    # Creating a hashed password
    hashed_password = generate_password_hash(password, method= 'sha256')
   
    #  Creating a new_user with the properties above matched to each property of the class
    new_user = User(first_name = first_name ,last_name = last_name ,password = hashed_password , email =email , username =username)

    # Adding to the database
    db.session.add(new_user)
    # Sending new_user to the database
    db.session.commit()
    flash("Your account has been  created successfuly")
    return redirect(url_for('main.login'))
  return render_template('signup.html', form = form)


@main.route('/pitches' , methods =['GET', 'POST'])
def pitches():

  return render_template('pitches.html')

