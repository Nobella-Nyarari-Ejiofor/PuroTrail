
from . import main
from app import db, login_manager
from flask import render_template , redirect , url_for , flash 
from .forms import LoginForm , SignUpForm , PitchesForm , CommentsForm
from werkzeug.security import check_password_hash, generate_password_hash
from ..models import User , Pitch , Category , Comment
from flask_login import login_user
from ..email import mail_message



@main.before_app_first_request
def create_all():
  db.create_all()

# defining the login manager function that takes in a user id
@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

# @login_manager.pitches_loader
# def load_pitches(pitch_id):
#   return Pitch.query.get(int(pitch_id))


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
        return redirect(url_for('main.pitches'))
      
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

    mail_message("Welcome to PuroTrail","email/welcome_user",new_user.email,new_user=new_user)

    flash("Your account has been  created successfuly")
    return redirect(url_for('main.login'))
  return render_template('signup.html', form = form)


@main.route('/pitches' , methods =['GET', 'POST'])
def pitches():
  form = PitchesForm()
  commentsform = CommentsForm()
  posted_pitch = form.pitch_words.data
  comment = commentsform.comment_words.data
  summary_posted_pitches = Pitch( pitchwords = posted_pitch)
  summary_comments = Comment(commentwords = comment)
  
  # Adding pitch to the database
  db.session.add_all([summary_posted_pitches, summary_comments])
  # commiting to the database
  db.session.commit()
  # pitchedarray = []

  # if summary_posted_pitches:
  #   minipitch = summary_posted_pitches
  #   pitchedarray.append(minipitch)
  
  return render_template('pitches.html' , form =form , commentsform =commentsform)

@main.route('/otherpitches' , methods =['GET','POST'])
def otherpitches():

  return render_template('otherpitches.html')

@main.route('/fitness')
def fitness():
  form = CommentsForm()
  return render_template('categories/fitness.html', form = form)

@main.route('/pickup')
def pickup():
  return render_template('categories/pickup.html')

@main.route ('/product')
def product():
  return render_template('categories/product.html')

@main.route('/interview')
def interview():
  return render_template ('categories/interview.html')


