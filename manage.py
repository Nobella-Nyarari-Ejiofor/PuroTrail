from app import create_app,db
from flask_script import Manager,Server
from app.models import User

# Creating app instance
app = create_app('developement')

manager = Manager(app)
manager.add_command('server' , Server)

# Making a shell context
@manager.shell
def make_shell_context():
  """
  A function that allows to pass in our properties to our shell
  """
  return dict(app=app , db=db , User=User)

# Running the app
if __name__ == "__main__":
    manager.run()
