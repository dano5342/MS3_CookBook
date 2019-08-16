import pymongo
import math
import re
import os 
import bcrypt
from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from forms import LoginForm, RegisterForm
from flask_login import current_user, login_user, logout_user, login_required

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
                            
@app.route('/add_recipe')
def add_recipe():
    return render_template('new_recipe')

@app.route('/recipes/<recipe_id>')
# Take the ObjectID and display the information for the recipe
def recipe(recipe_id):
    the_recipe = mongo.db.Recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('recipe.html', recipe = the_recipe, title = the_recipe['recipe_name'])

@app.route('/login.html', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['username']})
    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), 
        login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
            session['username'] = request.form['username']
            return redirect(url_for('index'))
    flash ('Invalid username/password combination')
    

@app.route('/register.html', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        users = mongo.db.users 
        existing_user = mongo.db.users.find_one({'username' : request.form['username']})
        if existing_user is None: #check user doesnt already exist
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert_one({'username': request.form['username'], 'password': hashpass})
            session['username'] = request.form['username']
            flash('Your now logged in as {{username}}')
        return index()
    flash('Apologies, however that Username taken!')
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
