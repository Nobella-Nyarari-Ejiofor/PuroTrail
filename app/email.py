from flask_mail import Message
from app import mail
from flask import render_template

# sending the email
def mail_message(subject,template,to,**kwargs):
    sender_email = 'nobella.ejiofor@student.moringaschool.com'

    email = Message(subject, sender=sender_email, recipients=[to])
    email.body= render_template(template + ".txt",**kwargs)
    email.html = render_template(template + ".html",**kwargs)
    mail.send(email)