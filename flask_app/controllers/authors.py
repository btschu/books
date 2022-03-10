from flask_app import app
from flask import redirect, render_template,request
from ..models.author import Author
from ..models.book import Book

# view all authors

@app.route('/authors')
def authors():
    context = {
        'authors' : Author.get_all()
    }
    return render_template("authors.html", **context)

# create a new author

@app.route('/authors/create',methods=['POST'])
def create_author():
    Author.save(request.form)
    return redirect('/')

# Show author's page and what books they have favorited

@app.route('/authors/<int:id>')
def show_author(id):
    data ={
        "id":id
    }
    context = {
        'author' : Author.get_by_id(data),
        'unfavorited_books' : Book.unfavorited_books(data)
    }
    return render_template("show_author.html", **context)

# add book to author's list of favorite books

@app.route('/join/book',methods=['POST'])
def join_book():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    Author.add_favorite(data)
    return redirect(f"/authors/{request.form['author_id']}")