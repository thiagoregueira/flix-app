import streamlit as st
from movies.repository import MovieRepository


class MovieService:
    def __init__(self):
        self.__movie_repository = MovieRepository()

    def get_movies(self):
        if 'movies' in st.session_state:
            return st.session_state.movies
        movies = self.__movie_repository.get_movies()
        st.session_state.movies = movies
        return movies

    def create_movie(self, title, release_date, genre, resume, actors):
        movie = dict(
            title=title,
            release_date=str(release_date),
            genre=genre,
            resume=resume,
            actors=actors,
        )
        new_movie = self.__movie_repository.create_movie(movie)
        st.session_state.movies.append(new_movie)
        return new_movie

    def get_movie_stats(self):
        if 'movie_stats' in st.session_state:
            return st.session_state.movie_stats
        movie_stats = self.__movie_repository.get_movie_stats()
        st.session_state.movie_stats = movie_stats
        return movie_stats
