from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, IntegerField, FieldList, FormField
from wtforms.validators import DataRequired, Length, Optional, InputRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=16)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=100)])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    
class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=16)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=100)])
    submit = SubmitField('Register')


class RecipeForm(FlaskForm):
    recipe_name = StringField('Recipe Name:', validators=[DataRequired(), Length(min=7, max=50)])
    recipe_type = StringField('Recipe Type:', validators=[DataRequired(), Length(min=7, max=50)])
    recipe_desc = StringField('Description:', validators=[DataRequired(), Length(min=10, max=100)])
    serving = IntegerField('Serving Size:', validators=[DataRequired()])
    prep_time = IntegerField('Preparation Time:', validators=[DataRequired()])
    cook_time = IntegerField('Cooking Time:', validators=[DataRequired()])
    img_url = StringField('Got a photo link?:')
    submit = SubmitField('Add Recipe')

