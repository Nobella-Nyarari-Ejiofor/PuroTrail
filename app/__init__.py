from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect

# creating the database and bootstrap instance
db = SQLAlchemy()
bootstrap = Bootstrap()
mail = Mail()
csrf = CSRFProtect()

# Initializing the login manager and assigning it to the view and protection.strong will monitor the changes in a user's request header and log the user out.
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'main.login'



def create_app(config_name):
  # Creating the app instance
  app = Flask(__name__)

  # The secret key
  # app.config['SECRET_KEY'] = SECRET_KEY
  # Creating the configurations for the app
  app.config.from_object(config_options[config_name])

  # Registering the 'main' blueprint
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)
  
  # Initializing flask extenssions
  db.init_app(app)
  bootstrap.init_app(app)
  login_manager.init_app(app)
  mail.init_app(app)
  csrf.init_app(app)
  
  return app
