from app import create_app
from flask_script import Manager,Server

# Creating app instance
app = create_app('developement')

manager = Manager(app)
manager.add_command('server' , Server)


# Running the app
if __name__ == "__main__":
    manager.run()
