from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

class Routing:    
    @app.route("/")
    def menu_page():
        title = request.args.get('added')
        msg = f"book <span>{title}</span> added" if title else ""
        return render_template("index.html", msg=msg)


    @app.route("/add_book")
    def add_book():
        return render_template("add_book.html")


    @app.route("/get_data", methods=['POST'])
    def get_data():
        title = request.form['title']
        return redirect(f"/?added={title}")



app.run()