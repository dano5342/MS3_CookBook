import pymongo
import math
import re
import os 
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId

app = Flask(__name__)

#Env Vars
app.config["MONGO_DBNAME"] = "CookBook"
app.config["MONGO_URI"] = os.getenv("MONGO_URI", "mongodb://localhost")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template("index.html", recipe=mongo.db.Recipes.find(),
                            cuisine=mongo.db.Cuisines.find())
                            
@app.route('/recipes/<recipe_id>')
def recipe(recipe_id):
    the_recipe = mongo.db.Recipes.find_one({"_id": ObjectId(recipe_id)})
    
    return render_template('recipe.html', recipe = the_recipe, title = the_recipe)
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
