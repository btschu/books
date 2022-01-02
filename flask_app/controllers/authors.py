from flask import render_template,redirect,request
from flask_app import app
from flask_app.models import author, book


@app.route('/authors')
def authors():
    return render_template("authors.html", authors = author.Author.get_all())

@app.route('/authors/create',methods=['POST'])
def create_author():
    author.Author.save(request.form)
    return redirect('/')

@app.route('/authors/<int:id>')
def show(id):
    data ={
        "id":id
    }
    return render_template("show_author.html", author = author.Author.get_one(data))

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