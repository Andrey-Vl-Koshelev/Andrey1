import pickle
import os.path


class Movie:
    def __init__(self, title, genre, name, year, duration, studio, actors):
        self.title = title
        self.genre = genre
        self.name = name
        self.year = year
        self.duration = duration
        self.studio = studio
        self.actors = actors

    def __str__(self):
        return f"{self.title} ({self.genre})"


class MovieModel:
    def __init__(self):
        self.movie_name = 'movie.txt'
        self.movies = self.load_data()

    def add_movie(self, dict_movie):
        movie = Movie(*dict_movie.values())
        self.movies[movie.title] = movie

    def get_all_movies(self):
        return self.movies.values()

    def get_singe_movie(self, user_title):
        movie = self.movies[user_title]
        dict_movie = {
            "название ": movie.title,
            "жанр": movie.genre,
            "режиссер": movie.name,
            "год выпуска": movie.year,
            "длительность": movie.duration,
            "студия": movie.studio,
            "актеры": movie.actors
        }
        return dict_movie

    def remove_movie(self, user_title):
        return self.movies.pop(user_title)

    def load_data(self):
        if os.path.exists(self.movie_name):
            with open(self.movie_name, 'rb') as f:
                return pickle.load(f)
        else:
            return dict()

    def save_data(self):
        with open(self.movie_name, 'wb') as f:
            pickle.dump(self.movies, f)
