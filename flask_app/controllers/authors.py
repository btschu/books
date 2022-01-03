from flask_app import app
from flask import redirect, render_template,request
from ..models.author import Author
from ..models.book import Book


@app.route('/authors')
def authors():
    return render_template("authors.html", authors = Author.get_all())

@app.route('/authors/create',methods=['POST'])
def create_author():
    Author.save(request.form)
    return redirect('/')

@app.route('/authors/<int:id>')
def show_author(id):
    data ={
        "id":id
    }
    return render_template("show_author.html", author=Author.get_by_id(data),unfavorited_books=Book.unfavorited_books(data))

@app.route('/join/book',methods=['POST'])
def join_book():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    Author.add_favorite(data)
    return redirect(f"/authors/{request.form['author_id']}")
# @app.route('/')
# def index():
#     return redirect('/users')

# @app.route('/users/new')
# def new():
#     return render_template("create.html")


# @app.route('/authors/<int:id>')
# def edit(id):
#     data ={
#         "id":id
#     }
#     return render_template("authors.html", authors = author.Author.get_one(data))


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