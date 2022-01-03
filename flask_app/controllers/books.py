from flask_app import app
from flask import redirect, render_template,request
from ..models.author import Author
from ..models.book import Book

@app.route('/')
def index():
    return redirect('/authors')

@app.route('/books')
def books():
    return render_template("books.html", books = Book.get_all())

@app.route('/books/create',methods=['POST'])
def create_book():
    Book.save(request.form)
    return redirect('/books')

@app.route('/books/<int:id>')
def show_book(id):
    data ={
        "id":id
    }
    return render_template("show_book.html", book=Book.get_by_id(data),unfavorited_authors=Author.unfavorited_authors(data))

@app.route('/join/author',methods=['POST'])
def join_author():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    Author.add_favorite(data)
    return redirect(f"/books/{request.form['book_id']}")

# @app.route('/users/new')
# def new():
#     return render_template("create.html")


# @app.route('/user/edit/<int:id>')
# def edit(id):
#     data ={
#         "id":id
#     }
#     return render_template("edit.html", user = User.get_one(data))


# @app.route('/user/update',methods=['POST'])
# def update():
#     User.update(request.form)
#     return redirect('/users')

# @app.route('/user/delete/<int:id>')
# def delete(id):
#     data = {
#         'id': id
#     }
#     User.delete(data)
#     return redirect('/users')