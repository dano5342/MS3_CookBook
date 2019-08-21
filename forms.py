from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, IntegerField, FieldList
from wtforms.validators import DataRequired, Length, Optional

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
    recipe_name = StringField('Recipe Name:')
    recipe_type = StringField('Recipe Type:')
    recipe_desc = StringField('Description:')
    serving = StringField('Serving Size:')
    prep_time = StringField('Preparation Time:')
    cook_time = StringField('Cooking Time:')
    ingredients = FieldList(StringField('Ingredients:', min_entries=1, max_entries=15))
    method = FieldList(StringField('Method:', min_entries=1, max_entries=10))
    img_url = StringField('Got a photo link? Paste it here!:')