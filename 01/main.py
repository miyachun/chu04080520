from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html", title="HOME PAGE")

@app.route("/docs")
def docs():
    return render_template("index.html", title="docs page")

@app.route("/about")
def about():
    return render_template("index.html", title="about page")