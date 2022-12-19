from flask import Flask, redirect, render_template, request, url_for

from books import Books, db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
db.init_app(app)

all_books = []


@app.route("/")
def home():
    global all_books
    # Get all books in database
    with app.app_context():
        all_books = db.session.query(Books).all()
    all_books = [
        {
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "rating": book.rating,
        }
        for book in all_books
    ]
    return render_template("index.html", all_books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        book_name = request.form.get("book_name")
        author = request.form.get("author")
        rating = request.form.get("rating")

        book = {
            "title": book_name,
            "author": author,
            "rating": rating,
        }
        all_books.append(book)

        # Update that book into csv
        new_book = Books(title=book_name, author=author, rating=rating)
        with app.app_context():
            db.session.add(new_book)
            db.session.commit()

        return redirect(url_for("home"))
    return render_template("add.html")


@app.route("/edit/rating/<book_id>", methods=["GET", "POST"])
def edit_rating(book_id):

    book_to_update = Books.query.get(book_id)
    if request.method == "POST":
        with app.app_context():
            db.session.query(Books).get(book_id).rating = request.form.get("rating")
            db.session.commit()
        return redirect(url_for("home"))

    return render_template("edit_rating.html", book=book_to_update)


@app.route("/<book_id>")
def delete(book_id):
    with app.app_context():
        delete_book = db.session.query(Books).get(book_id)
        db.session.delete(delete_book)
        db.session.commit()

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
