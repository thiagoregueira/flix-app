import requests
import streamlit as st

from login.service import logout


class MovieRepository:
    def __init__(self):
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}',
            'Content-Type': 'application/json',
        }
        self.__base_url = 'https://flixapi.dominio.qzz.io/'
        self.__api_version = 'api/v1/'
        self.__movie_url = self.__base_url + self.__api_version + 'movies/'

    def get_movies(self):
        response = requests.get(self.__movie_url, headers=self.__headers)
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None

        raise Exception(f'Erro ao buscar filmes. Status code: {response.status_code}')

    def create_movie(self, movie):
        response = requests.post(
            self.__movie_url,
            headers=self.__headers,
            json=movie,
        )
        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None

        raise Exception(f'Erro ao criar filme. Status code: {response.status_code}')

    def get_movie_stats(self):
        response = requests.get(self.__movie_url + 'stats/', headers=self.__headers)
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None

        raise Exception(f'Erro ao buscar estatísticas de filmes. Status code: {response.status_code}')
