from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.author import Author

class Book:

    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO books ( title , num_of_pages, created_at, updated_at ) VALUES ( %(title)s, %(num_of_pages)s, NOW() , NOW() );"
        return connectToMySQL('books_schema').query_db( query, data )

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL('books_schema').query_db(query)
        books = []
        for book in results:
            books.append( cls(book) )
        return books

    # @classmethod
    # def dojo_with_members(cls, data ):
    #     query = "SELECT * FROM books LEFT JOIN authors on books.id = authors.book_id WHERE books.id = %(id)s;"
    #     results = connectToMySQL('books_schema').query_db(query,data)
    #     book = cls(results[0])
    #     for row in results:
    #         n = {
    #             'id': row['books.id'],
    #             'title': row['title'],
    #             'num_of_pages': row['num_of_pages'],
    #             'created_at': row['books.created_at'],
    #             'updated_at': row['books.updated_at']
    #         }
    #         book.authors.append(Author(n))
    #     return book

    # @classmethod
    # def get_one(cls,data):
    #     query  = "SELECT * FROM users WHERE id = %(id)s";
    #     result = connectToMySQL('books_schema').query_db(query,data)
    #     return cls(result[0])

    # @classmethod
    # def update(cls,data):
    #     query = "UPDATE users SET first_name=%(fname)s,last_name=%(lname)s,email=%(email)s,updated_at=NOW() WHERE id = %(id)s;"
    #     return connectToMySQL('books_schema').query_db(query,data)

    # @classmethod
    # def delete(cls,data):
    #     query  = "DELETE FROM users WHERE id = %(id)s;"
    #     return connectToMySQL('books_schema').query_db(query,data)