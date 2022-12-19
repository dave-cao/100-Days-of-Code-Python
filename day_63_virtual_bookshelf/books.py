from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()


# INTEGER PRIMARY KEY: this is our unique identifier for the book
# varchar(250) NOT NULL UNIQUE: max 250 characters, it must have a value, and it must not be the same
# varchar(250) NOT NULL: author must have characters with max 250
# FLOAT NOT NULL: a not null float number
# cursor.execute(
#     "CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)"
# )

# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
db = SQLAlchemy(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # this will allow each object to be identified by its title when printed
    def __repr__(self):
        return "<Book %r>" % self.title


with app.app_context():
    db.create_all()
    # The primary key will be auto generated!!
    # new_book = Books(title='Super Powered 3', author='Drew Hayes', rating=9.5)
    # db.session.add(new_book)
    # db.session.commit()

    # all_books = db.session.query(Books).all()
    # book = Books.query.filter_by(title="Super Powered 2").first()
    # print(book)
