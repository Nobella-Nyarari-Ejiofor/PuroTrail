from . import db

class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key =True)
  first_name = db.Column(db.String(255))
  last_name = db.Column(db.String(255))
  username = db.Column(db.String(255))
  role_id = db.Column(db.Integer , db.ForeignKey('roles.id'))
  password = db.Column(db.String(255))
  email = db.Column(db.String(255))

  def __repr__(self):
        return f'User {self.username}'


# Class for the role of the user
class Role(db.Model) :
  __tablename__ = 'roles'
  id = db.Column(db.Integer , primary_key =True)
  username = db.Column(db.String(255), unique = True)
  users = db.relationship('User' , backref = 'role' , lazy = "dynamic")
  

  def __repr__(self):
    return f'User {self.name}'

