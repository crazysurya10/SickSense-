
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/creator")
def creator():
    return render_template("creator.html")

@app.route("/origin")
def origin():
    return render_template("origin.html")

@app.route("/finder")
def finder():
    return render_template("finder.html")


@app.route("/symptoms")
def symptoms():
    return render_template("symptoms.html")


if __name__ == '__main__':
    app.run(port=5001, debug=True)