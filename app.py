from flask import Flask, session, render_template, request, g
import sqlite3


app = Flask(__name__)

@app.route("/")
def index():
    data = get_db()
    return render_template("index.html", recipe = data)

@app.route("/pasta")
def pasta():
    data = get_db()
    return render_template("pasta.html", recipe = data)

@app.route("/chicken")
def chicken():
    data = get_db()
    return render_template("chicken.html", recipe = data)

@app.route("/cookies")
def cookies():
    data = get_db()
    return render_template("cookies.html", recipe = data)

@app.route("/beef")
def beef_stir_fry():
    data = get_db()
    return render_template("beef.html", recipe = data)

@app.route("/cury")
def cury():
    data = get_db()
    return render_template("cury.html", recipe = data)

@app.route("/salad")
def salad():
    data = get_db()
    return render_template("salad.html", recipe = data)

@app.route("/ratatouille")
def ratatouille():
    data = get_db()
    return render_template("ratatouille.html", recipe = data)

@app.route("/pancakes")
def pancakes():
    data = get_db()
    return render_template("pancakes.html", recipe = data)

@app.route("/tacos")
def tacos():
    data = get_db()
    return render_template("tacos.html", recipe = data)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect("food_recipes.db")
        cursor = db.cursor()
        cursor.execute("SELECT recipe_ID, recipe_name, recipe_ingredients, recipe_description, preparation_time_in_minute, cooking_time_in_minute FROM recipes")
        data = cursor.fetchall()
    return data