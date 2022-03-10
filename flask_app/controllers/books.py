from flask_app import app
from flask import redirect, render_template,request
from ..models.author import Author
from ..models.book import Book

@app.route('/')
def index():
    return redirect('/authors')

# view all books

@app.route('/books')
def books():
    context = {
        'books' : Book.get_all()
    }
    return render_template("books.html", **context)

# add a new book

@app.route('/books/create',methods=['POST'])
def create_book():
    Book.save(request.form)
    return redirect('/books')

# view one book and all authors that liked that book.

@app.route('/books/<int:id>')
def show_book(id):
    data ={
        "id":id
    }
    context = {
        'book' : Book.get_by_id(data),
        'unfavorited_authors' : Author.unfavorited_authors(data)
    }
    return render_template("show_book.html", **context)

# add author to a list of authors that like a book

@app.route('/join/author',methods=['POST'])
def join_author():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    Author.add_favorite(data)
    return redirect(f"/books/{request.form['book_id']}")