from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, BooleanField, SubmitField,
                     TextAreaField, IntegerField, FieldList, FormField)
from wtforms.validators import (DataRequired, Length, Optional,
                                InputRequired, EqualTo)


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),
                           Length(min=5, max=16)])
    password = PasswordField('Password', validators=[DataRequired(),
                             Length(min=5, max=100)])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),
                           Length(min=5, max=16)])
    password = PasswordField('Password', validators=[DataRequired(),
                             Length(min=5, max=100),
                             EqualTo('confirm',
                             message="Passwords must match")])
    confirm = PasswordField('Confirm Password')
    submit = SubmitField('Register')


# Custom forms for single input fields. ARRAYS had to be done manually.

class RecipeForm(FlaskForm):
    recipe_name = StringField('Recipe Name:', [InputRequired()])
    recipe_type = StringField('Recipe Type:', [InputRequired()])
    recipe_desc = StringField('Description:', [InputRequired()])
    serving = IntegerField('Serving Size:', [InputRequired()])
    prep_time = IntegerField('Preparation Time:', [InputRequired()])
    cook_time = IntegerField('Cooking Time:', [InputRequired()])
    img_url = StringField('Got a photo link?:', [Optional()])
    submit = SubmitField('Add Recipe')
