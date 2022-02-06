from flask import Flask
from config import config_options


def create_app(config_name):
  # Creating the app instance
  app = Flask(__name__)

  # Creating the configurations for the app
  app.config.from_object(config_options[config_name])

  # Registering the 'main' blueprint
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)
  
 
  return app
