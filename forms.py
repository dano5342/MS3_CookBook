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
    recipe_name = StringField('Recipe Name:')
    recipe_type = StringField('Recipe Type:')
    recipe_desc = StringField('Description:')
    serving = IntegerField('Serving Size:')
    prep_time = IntegerField('Preparation Time:')
    cook_time = IntegerField('Cooking Time:')
    ingredients = TextAreaField('Ingredients:') 
    method = TextAreaField('Method:')
    img_url = StringField('Got a photo link?:')
    submit = SubmitField('Add Recipe')
    


