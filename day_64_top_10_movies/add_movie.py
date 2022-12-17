# Adding movies
import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()


headers = {"Authorization": f"Bearer {os.environ.get('API_KEY')}"}
def get_movie_data(title):
    """Grabs the title of a movie, using an API, it returns an object with
    the movie data.
    title (str): the title of the movie
    """
    print("Grabbing data from movie API!")

    movie_data = {
        "query": title
    }
    response = requests.get(url='https://api.themoviedb.org/3/search/movie?', params=movie_data, headers=headers)

    # We're gonna get pages from results 
    data = response.json()

    results = data["results"]


    return results

def get_movie_details(movie_id):
    # get movie data with movie id
    response = requests.get(url=f"https://api.themoviedb.org/3/movie/{movie_id}", headers=headers)

    top_movie = response.json()




    movie_year = int(top_movie.get("release_date")[:4])
    movie_formatted = {
     "title": top_movie.get("title"),
     "year": movie_year,
     "description": top_movie.get("overview"),
     "img_url": f"https://image.tmdb.org/t/p/original/{top_movie.get('poster_path')}",
    }
    return movie_formatted


get_movie_details(157336)

# new_movie = Movies(title=movie_data.get("title"), year=movie_data.get("year"), description=movie_data.get("description"), img_url=movie_data.get("img_url"))
