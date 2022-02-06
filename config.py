import os

from instance.config import SECRET_KEY 

class Config:
  """
  Defining the configuration parent class
  """
  SECRET_KEY = os.environ.get('SECRET_KEY')

class prodConfig(Config):
  pass

class DevConfig(Config):
  DEBUG = True

config_options = {
  'developement' : DevConfig,
  'production' : prodConfig
}