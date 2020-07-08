from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,BooleanField
from wtforms.validators import DataRequired,length,EqualTo,ValidationError,Email
from app.auth.models import User

def email_exists(form,field):
    email=User.query.filter_by(user_email=field.data).first()
    if email:
        raise ValidationError('Email Already Exists')
    
class RegistrationForm(FlaskForm):
    name=StringField('What is your name',validators=[DataRequired(),length(3,15,message='Between 3 to 15 characters')])
    email=StringField('Enter your Email',validators=[DataRequired(),Email(),email_exists])
    password=PasswordField('Password',validators=[DataRequired(),length(5),EqualTo('confirm',message='Password must match')])
    confirm=PasswordField('Confirm Password',validators=[DataRequired()])
    submit=SubmitField('Register')
    

class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    stay_loggedin=BooleanField('stay logged-in')
    submit=SubmitField('LogIn')
    