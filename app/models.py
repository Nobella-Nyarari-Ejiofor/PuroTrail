from . import db
from flask_login import UserMixin

class User(UserMixin,db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key =True)
  first_name = db.Column(db.String(255))
  last_name = db.Column(db.String(255))
  username = db.Column(db.String(255))
  role_id = db.Column(db.Integer , db.ForeignKey('roles.id'))
  password = db.Column(db.String(255))
  email = db.Column(db.String(255))
  
  def is_active(self):
    return True

  def __repr__(self):
        return f'User {self.username}'


# Class for the role of the user
class Role(UserMixin,db.Model) :
  __tablename__ = 'roles'
  id = db.Column(db.Integer , primary_key =True)
  username = db.Column(db.String(255), unique = True)
  users = db.relationship('User' , backref = 'role' , lazy = "dynamic")
  

  def __repr__(self):
    return f'User {self.name}'

