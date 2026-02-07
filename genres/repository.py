import streamlit as st
import requests

from login.service import logout


class GenreRepository:
    def __init__(self):
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}',
            'Content-Type': 'application/json',
        }
        self.__base_url = 'https://flixapi.dominio.qzz.io/'
        self.__api_version = 'api/v1/'
        self.__genre_url = self.__base_url + self.__api_version + 'genres/'

    def get_genres(self):
        response = requests.get(self.__genre_url, headers=self.__headers)
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None

        raise Exception(f'Erro ao buscar gêneros. Status code: {response.status_code}')

    def create_genre(self, genre):
        response = requests.post(
            self.__genre_url,
            headers=self.__headers,
            json=genre,
        )
        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None

        raise Exception(f'Erro ao criar gênero. Status code: {response.status_code}')
