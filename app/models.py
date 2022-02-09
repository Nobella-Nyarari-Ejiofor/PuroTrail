from sqlalchemy import ForeignKey
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
  pitches = db.relationship('Pitch' , backref = 'user' , lazy = "dynamic")
  
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

#class for the pitch
class Pitch(db.Model):
  __tablename__ = 'pitches'
  id = db.Column(db.Integer , primary_key = True)
  pitchwords = db.Column(db.String(500))
  date = db.Column(db.DateTime )
  vote = db.Column(db.Boolean , default=False, server_default="false")
  comment = db.relationship('Comment' , backref = 'pitch' , lazy = "dynamic")
  user_id = db.Column(db.Integer , db.ForeignKey('users.id'))
  category_id = db.Column(db.Integer, db.ForeignKey('categorys.id'))

  def __repr__(self):
    return f'User {self.name}'

class Comment(db.Model):
  __tablename__ = 'comments'
  id= db.Column(db.Integer , primary_key = True)
  commentwords = db.Column(db.String(500))
  pitches_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
  

class Category(db.Model):
  __tablename__= 'categorys'
  id = db.Column(db.Integer , primary_key= True)
  categorywords = db.Column(db.String(255))
  pitches = db.relationship('Pitch', backref = 'category', lazy = "dynamic")
