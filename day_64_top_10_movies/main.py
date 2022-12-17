from flask import Flask, redirect, render_template, request, url_for
from flask_bootstrap import Bootstrap

from add_movie import get_movie_data, get_movie_details
from forms import AddMovie, EditMovie
from movies import Movies, db

all_movies = []



app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
Bootstrap(app)
db.init_app(app)


@app.route("/")
def home():
    global all_movies

    # Get all movies in database 
    with app.app_context():
        all_movies = db.session.query(Movies).order_by(Movies.rating).all()
    all_movies = [{"id": movie.id, "title": movie.title, "year": movie.year, "description": movie.description, "rating": movie.rating, "ranking": movie.ranking, "review": movie.review, "img_url": movie.img_url } for movie in all_movies]

    # put ranking in based on rating score
    rank = len(all_movies)
    for i in range(len(all_movies)):
        all_movies[i]["ranking"] = rank
        rank -= 1

    return render_template("index.html", all_movies=all_movies)

# Update the review and rating of the movie!
@app.route("/update", methods=["GET", "POST"])
def update():
    form = EditMovie()
    movie_id = request.args.get("movie_id")
    if form.validate_on_submit():
        with app.app_context():
            movie = db.session.query(Movies).get(movie_id)
            movie.rating = form.rating.data
            movie.review = form.review.data
            db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get("movie_id")
    with app.app_context():
        movie = db.session.query(Movies).get(movie_id)
        db.session.delete(movie)
        db.session.commit()

    return redirect(url_for('home'))

    
@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovie()
    if form.validate_on_submit():
        title = form.title.data 
        return redirect(url_for('select', title=title))

    return render_template('add.html', form=form)

@app.route("/select")
def select():
    movie_data = get_movie_data(request.args.get("title"))
    return render_template('select.html', movie_data=movie_data)


@app.route("/get-movie-details")
def movie_details():
    # Gets the movie details and then appends to database
    movie = request.args.get("movie_id")
    movie_data = get_movie_details(int(movie))
    new_movie = Movies(title=movie_data.get("title"), year=movie_data.get("year"), description=movie_data.get("description"), img_url=movie_data.get("img_url"))
    with app.app_context():
        db.session.add(new_movie)
        db.session.commit()

    # We have to query the book that we are getting the movie details fom database
    # return redirect(url_for("edit", movie_id=int(movie.id)))
    movie_id = Movies.query.filter_by(title=movie_data.get("title")).first().id
    return redirect(url_for('update', movie_id=movie_id))

if __name__ == '__main__':
    app.run(debug=True)
