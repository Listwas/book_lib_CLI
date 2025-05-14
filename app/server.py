from flask import Flask, render_template, request, redirect
import os
from main import Library

app = Flask(__name__)
lib = Library('books_data.json')

class Routing:    
    @app.route("/")
    def menu_page():
        title = request.args.get('added')
        author = request.args.get('author')
        
        msg = (f"book <span style='color: green'>{title.capitalize()}</span> "
               f"added by <span style='color: green'>{author.capitalize()}</span>") if title and author else ""
        return render_template("index.html", msg=msg)


    @app.route("/add_book")
    def add_book():
        return render_template("add_book.html")
    
    
    @app.route("/get_data", methods=['POST'])
    def get_data():
        title = request.form['title']
        author = request.form['author']
        pages = request.form['pages']
        status = request.form['status']
        
        book = {
            "title": title,
            "author": author,
            "pages": int(pages),
            "status": status
            }
        
        lib.add_book(book)
        return redirect(f"/?added={title}&author={author}")
    
    @app.route("/list_books")
    def list_books():
        all_books = lib.list_books()
        return render_template("/list_books.html", all_books=all_books)
    
def main():
    app.run()

main()