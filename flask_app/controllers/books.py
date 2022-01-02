from flask import render_template,redirect,request
from flask_app import app
from flask_app.models.book import Book

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

# @app.route('/dojo/<int:id>')
# def show(id):
#     data ={
#         "id":id
#     }
#     return render_template("dojo_members.html", dojo = Dojo.dojo_with_members(data))

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