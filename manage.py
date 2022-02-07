from app import create_app,db
from flask_script import Manager,Server
from app.models import User , Role
from flask_migrate import Migrate, MigrateCommand

# Creating app instance
app = create_app('developement')

manager = Manager(app)
manager.add_command('server' , Server)

# Initializing Migrate then pass in the app instance and the db instance 
migrate = Migrate(app,db)
manager.add_command('db', MigrateCommand)

# Making a shell context
@manager.shell
def make_shell_context():
  """
  A function that allows to pass in our properties to our shell
  """
  return dict(app=app , db=db , User=User , Role = Role)

# Running the app
if __name__ == "__main__":
    manager.run()
