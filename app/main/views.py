from crypt import methods
from . import main
from flask import render_template 


@main.route('/', methods = ['GET','POST'])
def home():
  return render_template('base.html')
 
  

