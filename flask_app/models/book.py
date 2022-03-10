from ..config.mysqlconnection import connectToMySQL
from flask_app.models import author

db = "books_schema"

class Book:

    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.authors_who_favorited = []

    @classmethod
    def save(cls, data ):
        query = """
        INSERT INTO books (title, num_of_pages, created_at, updated_at)
        VALUES (%(title)s, %(num_of_pages)s, NOW(), NOW());"""
        return connectToMySQL(db).query_db( query, data )

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL(db).query_db(query)
        books = []
        for book in results:
            books.append( cls(book) )
        return books

    @classmethod
    def get_one(cls,data):
        query  = """
        SELECT * FROM books
        WHERE id = %(id)s;"""
        result = connectToMySQL(db).query_db(query, data)
        return cls(result[0])

    @classmethod
    def get_by_id(cls,data):
        query = """
        SELECT * FROM books
        LEFT JOIN favorites ON books.id = favorites.book_id
        LEFT JOIN authors ON authors.id = favorites.author_id
        WHERE books.id = %(id)s;"""
        results = connectToMySQL(db).query_db(query,data)
        book = cls(results[0])
        for row in results:
            if row['authors.id'] == None:
                break
            data = {
                "id": row['authors.id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            }
            book.authors_who_favorited.append(author.Author(data))
        return book

# is there another way to do this? maybe add it into the get_by_id method in an if statement?
    @classmethod
    def unfavorited_books(cls,data):
        query = """
        SELECT * FROM books
        WHERE books.id
        NOT IN ( SELECT book_id FROM favorites
        WHERE author_id = %(id)s );"""
        results = connectToMySQL(db).query_db(query,data)
        books = []
        for row in results:
            books.append(cls(row))
        # print(books)
        return books