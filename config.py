import os

from instance.config import SECRET_KEY 

class Config:
  """
  Defining the configuration parent class
  """
  SECRET_KEY = os.urandom(32)
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:access@localhost/putotrial'

   # email configurations
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
  MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class prodConfig(Config):
  pass

class DevConfig(Config):
  DEBUG = True

config_options = {
  'developement' : DevConfig,
  'production' : prodConfig
}