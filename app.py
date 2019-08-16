import pymongo
import math
import re
import os 
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from forms import LoginForm, RegisterForm

app = Flask(__name__)

#Env Vars
app.config["MONGO_DBNAME"] = "CookBook"
app.config["MONGO_URI"] = os.getenv("MONGO_URI", "mongodb://localhost")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
mongo = PyMongo(app)

@app.route('/')
# Display recipes on the homepage
def index():
    return render_template("index.html", recipe=mongo.db.Recipes.find(),
                            cuisine=mongo.db.Cuisines.find())
                            
@app.route('/recipes/<recipe_id>')
# Take the ObjectID and display the information for the recipe
def recipe(recipe_id):
    the_recipe = mongo.db.Recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('recipe.html', recipe = the_recipe, title = the_recipe['recipe_name'])

@app.route('/login.html', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me{}'.format(
            form.username.data, form.remember_me.data))
    return render_template('login.html', title='Sign In', form=form)
    
@app.route('/register.html', methods=['GET', 'POST'])
def register():
    rform = RegisterForm
    if rform.validate_on_submit():
        flash('Registration requested for user {}, remember_me{}'.format(
            rform.username.data, rform.remember_me.data))
    return render_template('register.html', title='Register', form=rform)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
