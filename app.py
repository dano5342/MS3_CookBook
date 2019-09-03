import pymongo
import math
import re
import os
import bcrypt
from flask import (Flask, render_template, redirect,
                   request, url_for, flash, session)
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from forms import LoginForm, RegisterForm, RecipeForm
from flask_login import (current_user, login_user, logout_user,
                         login_required, LoginManager, login_manager)
from flask_wtf.csrf import CSRFProtect


csrf = CSRFProtect()


app = Flask(__name__)

# Env Vars
app.config["MONGO_DBNAME"] = "CookBook"
app.config["MONGO_URI"] = os.getenv("MONGO_URI", "mongodb://localhost")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
mongo = PyMongo(app)

login_manager = LoginManager(app)


csrf.init_app(app)

@app.route('/')
# Display recipes on the homepage
def index():
    # Pagination function
    page_limit = 6
    current_page = int(request.args.get('current_page', 1))
    total = mongo.db.Recipes.count()
    pages = range(1, int(math.ceil(total / page_limit)) + 1)
    recipes = mongo.db.Recipes.find().sort('_id', pymongo.DESCENDING).skip(
                            (current_page - 1)*page_limit).limit(page_limit)

    return render_template("index.html", recipe=recipes, pages=pages,
                           current_page=current_page)


# Recipe Functions, View, Edit, Create, Delete.
@app.route('/recipes/<recipe_id>')
# Take the ObjectID and display the information for the recipe
def recipe(recipe_id):
    the_recipe = mongo.db.Recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('recipe.html', recipe=the_recipe,
                           title=the_recipe['recipe_name'])


@app.route('/delete/<recipe_id>', methods=['POST', 'GET'])
def delete(recipe_id):  # non users cannot delete recipes.
    # redirects back to recipe
    if 'username' not in session:
        flash('This is not possible for non-members.')
        return redirect('recipe/<recipe_id>')
    mongo.db.Recipes.remove({'_id': ObjectId(recipe_id)})
    flash('Recipe Deleted.')
    return redirect(url_for('index'))


@app.route('/editrecipe/<recipe_id>', methods=['GET', 'POST'])
def editrecipe(recipe_id):
    if 'username' not in session:  # Same for editing, logged in users ONLY
        flash('Not possible for non-members! Please create an account.')
        return redirect(url_for('register'))

    form = RecipeForm()
    getrep = mongo.db.Recipes.find_one({'_id': ObjectId(recipe_id)})
    # Find the recipe to edit
    if request.method == 'GET':  # GET the recipe
        form = RecipeForm(data=getrep)
        return render_template('edit_recipe.html', recipe=getrep,
                               form=form, title="Edit Recipe")
    if form.validate_on_submit:
        rec = mongo.db.Recipes
        rec.update_one({'_id': ObjectId(recipe_id), }, {
            '$set': {'recipe_name': request.form['recipe_name'],
                     # Populates the fields with the data to be edited.
                     'recipe_type': request.form['recipe_type'],
                     'recipe_desc': request.form['recipe_desc'],
                     'serving': request.form['serving'],
                     'prep_time': request.form['prep_time'],
                     'cook_time': request.form['cook_time'],
                     'ingredients': request.form.getlist('ingredients'),
                     'method': request.form.getlist('methods'),
                     # Lists for Ingredients and Method to store in an array.
                     'img_url': request.form['img_url']}})
        flash('Recipe Succesfully Updated.')
        return redirect(url_for('recipe', recipe_id=recipe_id))
    return render_template(url_for('recipe', recipe_id=recipe_id))


@app.route('/addrecipe', methods=['GET', 'POST'])
def addrecipe():
    if 'username' not in session:
        flash('Not possible for non-members! Please create an account.')
        return redirect(url_for('register'))

    form = RecipeForm()
    if request.method == 'POST' and form.validate_on_submit():
        recipe = mongo.db.Recipes
        recipe.insert({'recipe_name': request.form['recipe_name'],
                       'recipe_type': request.form['recipe_type'],
                       'recipe_desc': request.form['recipe_desc'],
                       'serving': request.form['serving'],
                       'prep_time': request.form['prep_time'],
                       'cook_time': request.form['cook_time'],
                       'ingredients': request.form.getlist('ingredients'),
                       'method': request.form.getlist('methods'),
                       # Lists for Ingredients and Method to store in an array.
                       'img_url': request.form['img_url']})
        flash('Recipe successfully added.')
        return redirect(url_for('index'))
    return render_template('addrecipe.html', form=form)

# Functions and Routing for Login, Registration and Logging out.


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if 'logged in' in session:  # check user not logged in
        return redirect(url_for('index'))
    if request.method == "POST" and form.validate_on_submit:
        existing_user = mongo.db.users.find_one({'name':
                                                 request.form['username']})
        if bcrypt.checkpw(request.form['password'].encode('utf-8'),
                          existing_user['password']):
                        # check password against hash
            session['username'] = request.form['username']
            session['logged in'] = True
            return redirect(url_for('index'))
        flash('Incorrect Username/Password combination.')
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():

    if 'username' in session:
        return redirect(url_for('index'))

    form = RegisterForm()
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name': request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'),
                                     bcrypt.gensalt())
# generate password hash
            users.insert({'name': request.form['username'],
                          'password': hashpass})
            session['username'] = request.form['username']
            # User is now successfully logged in
            session['username'] = request.form['username']
            flash('User creation successful!')
            return redirect(url_for('index'))

        flash('That username already exists!')

    return render_template('register.html', form=form)


@app.route('/search', methods=["GET", "POST"])
def search():
    # Pagination within a search function.
    page_limit = 6  # Logic for pagination
    current_page = int(request.args.get('current_page', 1))
    #  get the searchdb form and use this to check against the index in the DB
    search_db = request.args['search_db']
    #  Assistance for indexes and logic for this was given by Shane Muirhead
    total = mongo.db.Recipes.find({'$text': {'$search': search_db}})
    t_total = len([r for r in total])
    pages = range(1, int(math.ceil(t_total / page_limit)) + 1)
    results = mongo.db.Recipes.find({'$text': {'$search': search_db}}).sort(
        '_id', pymongo.ASCENDING).skip((current_page - 1)*page_limit).limit(
            page_limit)

    if 'logged_in' in session:
        current_user = mongo.db.users.find_one()
        return render_template('search.html',
                               results=results, pages=pages,
                               current_page=current_page,
                               search_db=search_db, current_user=current_user,
                               title="Your Results", t_total=t_total)
    else:
        return render_template('search.html',
                               results=results, pages=pages,
                               current_page=current_page, search_db=search_db,
                               title="Your Results", t_total=t_total)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)
