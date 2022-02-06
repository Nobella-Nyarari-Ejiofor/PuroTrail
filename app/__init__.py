from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy

# creating the database instance
db = SQLAlchemy()

def create_app(config_name):
  # Creating the app instance
  app = Flask(__name__)

  # Creating the configurations for the app
  app.config.from_object(config_options[config_name])

  # Registering the 'main' blueprint
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)
  
  # Initializing flask extenssions
  db.init_app(app)
 
  return app
