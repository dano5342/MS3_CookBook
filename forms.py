from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=16)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=100)])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    
class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=16)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=100)])
    submit = SubmitField('Register')