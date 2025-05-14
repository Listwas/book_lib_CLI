from flask import Flask, render_template, redirect
import os

app = Flask(__name__)

@app.route("/")
def menu_page():
    return render_template("index.html")

@app.route("/add_book")
def add_book():
    return render_template("add_book.html")
app.run()