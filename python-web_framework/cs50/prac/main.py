#!/usr/bin/python3
"""
    Basic flask server
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/products")
def products():
    return "Nothing Phone(3). Coming soon!"


@app.route("/customers")
def customers():
    return "<h3>Ochego, Fonsi, Ogweezy</h3>"


if __name__ == "__main__":
    app.run(debug=True, host="127.14.50.60", port=1450)
