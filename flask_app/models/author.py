from ..config.mysqlconnection import connectToMySQL
from flask_app.models import book

class Author:

    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorite_books = []

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO authors (first_name, last_name, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, NOW(), NOW());"
        return connectToMySQL('books_schema').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL('books_schema').query_db(query)
        authors = []
        for author in results:
            authors.append( cls(author) )
        return authors

    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM authors WHERE id = %(id)s;"
        result = connectToMySQL('books_schema').query_db(query,data)
        return cls(result[0])

    @classmethod
    def unfavorited_authors(cls,data):
        query = "SELECT * FROM authors WHERE authors.id NOT IN ( SELECT author_id FROM favorites WHERE book_id = %(id)s );"
        authors = []
        results = connectToMySQL('books_schema').query_db(query,data)
        for row in results:
            authors.append(cls(row))
        return authors

    @classmethod
    def add_favorite(cls,data):
        query = "INSERT INTO favorites (author_id, book_id) VALUES (%(author_id)s, %(book_id)s);"
        return connectToMySQL('books_schema').query_db(query,data);


    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM authors LEFT JOIN favorites ON authors.id = favorites.author_id LEFT JOIN books ON books.id = favorites.book_id WHERE authors.id = %(id)s;"
        results = connectToMySQL('books_schema').query_db(query,data)

        # Creates instance of author object from row one
        author = cls(results[0])
        # append all book objects to the instances favorites list.
        for row in results:
            # if there are no favorites
            if row['books.id'] == None:
                break
            # common column names come back with specific tables attached
            data = {
                "id": row['books.id'],
                "title": row['title'],
                "num_of_pages": row['num_of_pages'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            }
            author.favorite_books.append(book.Book(data))
        return author
    # @classmethod
    # def update(cls,data):
    #     query = "UPDATE users SET first_name=%(fname)s,last_name=%(lname)s,email=%(email)s,updated_at=NOW() WHERE id = %(id)s;"
    #     return connectToMySQL('books_schema').query_db(query,data)

    # @classmethod
    # def delete(cls,data):
    #     query  = "DELETE FROM users WHERE id = %(id)s;"
    #     return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)