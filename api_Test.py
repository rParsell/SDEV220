from flask import Flask
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_Key = True)
    book_name = db.Column(db.String(80))
    author = db.Column(db.String(80))
    publisher = db.Column(db.String(80))
    def __repr__(self):
        return f"{self.book_name} - {self.author} - {self.publisher}"

@app.route('/books')
def booken():
    books = Book.query.all()

    output = []
    for book in books:
        book_data = {'name': book.name, 'author': book.author, 'publisher': book.publisher}
        output.append(book_data)
    return {'book': output}
