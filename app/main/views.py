from . import main
from app import db, login_manager,csrf
from flask import render_template , redirect , url_for , flash , abort
from .forms import LoginForm , SignUpForm , PitchesForm , CommentsForm
from werkzeug.security import check_password_hash, generate_password_hash
from ..models import User , Pitch , Category , Comment
from flask_login import login_user , login_required , current_user ,logout_user
from ..email import mail_message



@main.before_app_first_request
def create_all():
  db.create_all()

# defining the login manager function that takes in a user id
@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))


@main.route('/', methods = ['GET','POST'])
def home():
  """
  A function that returns the home page for the application.

  Args : Takes in the pitches from the database.

  Kwargs: Returns the pitches for display in the database.
  """
  homepitches = Pitch.query.all()
  return render_template('home.html', homepitches = homepitches)
 

@main.route('/login' , methods = ['GET','POST'])
def login():
  """
  A function that logs in a user to the web application.
  """
  form = LoginForm()
  # Check validation of the form
  if form.validate_on_submit():
    # Creates a user based on whether the name submitted in the form matches a name in the database
    user = User.query.filter_by(username = form.username.data).first()
  
    # if user exists
    if user:
    
      # Compare the passwords.
      if check_password_hash(user.password,form.password.data):
        # /loging the user in
        login_user(user)
        
        # redirecting to the pitch page
        return redirect(url_for('main.home'))
      
      return ("Invalid username or password")
    return("The username doesn't exist")


  return  render_template ('login.html', form = form)

@main.route('/signup' , methods =['GET', 'POST'])
def signup():
  """
  A function that signs up a user into the application and saves their data into the database
  """
  form = SignUpForm()
  if form.validate_on_submit():
    first_name = form.first_name.data
    last_name = form.last_name.data
    username = form.username.data
    email = form.email.data
    password = form.password.data
    
    # Creating a hashed password
    hashed_password = generate_password_hash(password, method= 'sha256')
   
    #  Creating a new_user with the properties above matched to each property of the class in the database
    new_user = User(first_name = first_name ,last_name = last_name ,password = hashed_password , email =email , username =username)

    # Adding to the database
    db.session.add(new_user)
    # Sending new_user to the database
    db.session.commit()
    print(new_user)

    mail_message("Welcome to PuroTrail","email/welcome_user",new_user.email,new_user=new_user)

    return redirect(url_for('main.login'))
  return render_template('signup.html', form = form)




@main.route('/pitches' , methods =['GET', 'POST'])
@login_required
def pitches():
  """
  A function that takes value from the pitches form and saves it to the database
  """
  form = PitchesForm()
  

  if form.validate_on_submit():
   posted_pitch = form.pitch_words.data
   category_select = form.category_field.data
   summary_posted_pitches = Pitch( pitchwords = posted_pitch , user_id = current_user.id , category_id = category_select)

  # Adding pitch to the database
   db.session.add(summary_posted_pitches)
  # commiting to the database
   db.session.commit()
 
  return render_template('pitches.html' , form =form )

@main.route('/comments/<id>', methods = ['GET','POST'])
@login_required
def comment(id):
  """
  A function that returns the comments form and displays the comments submitted
  """
  pitch = Pitch.query.filter_by(id=id).first()
  comments = Comment.query.filter_by(pitches_id = id).all()
  form = CommentsForm()
  if form.validate_on_submit():
    commentsdata = form.comment_words.data
    commented = Comment(commentwords = commentsdata ,pitch = pitch )

    db.session.add(commented)
    db.session.commit()
  return render_template('comments.html', pitch = pitch ,form =form ,comments = comments )

@main.route('/category/<id>')
@login_required
def pickup(id):
  """
  A function that returns pitches of a specific user by catgory
  """
  
  category_specific = Category.query.filter_by(id = id).first() 
  pitches = Pitch.query.filter_by(category = category_specific).all()
 
  return render_template('categories.html', pitches = pitches)



@main.route('/pitches/user/<uname>', methods = ['GET', 'POST'])
@login_required
def profileview(uname):
  """
  A function to display users profile information
  """
  user = User.query.filter_by(username = uname).first()
  # pitches = Pitch.query.filter_by(user_id= user.id).all() - displays all the pitches by a user but will interfere with my UI
  
  if user is None:
    abort(404)
  return render_template('otherpitches.html', user = user)

@main.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('main.home'))
