import pymongo
import math
import re
import os 
import bcrypt
from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from forms import LoginForm, RegisterForm
from flask_login import current_user, login_user, logout_user, login_required, LoginManager, login_manager

app = Flask(__name__)
#Env Vars
app.config["MONGO_DBNAME"] = "CookBook"
app.config["MONGO_URI"] = os.getenv("MONGO_URI", "mongodb://localhost")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
mongo = PyMongo(app)

login_manager = LoginManager(app)

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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if 'logged in' in session:
        return redirect(url_for('index.html'))
    if request.method == "POST" and form.validate:
        existing_user = mongo.db.users.find_one({'name': request.form['username']})
        if bcrypt.hashpw(request.form['password'].encode('utf-8'), existing_user['password']):
            session['username'] = request.form['username']
            session['logged in'] = True
            return redirect(url_for('index'))
        flash('Incorrect Password.')
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            flash('User creation successful!')
            return redirect(url_for('index'))
        
        return 'That username already exists!'

    return render_template('register.html', form=form)


@app.route('/new_recipe')
def new_recipe():
    return render_template('new_recipe.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
