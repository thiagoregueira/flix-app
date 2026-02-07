import requests
import streamlit as st

from login.service import logout


class ReviewRepository:
    def __init__(self):
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}',
            'Content-Type': 'application/json',
        }
        self.__base_url = 'https://flixapi.dominio.qzz.io/'
        self.__api_version = 'api/v1/'
        self.__movie_url = self.__base_url + self.__api_version + 'reviews/'

    def get_reviews(self):
        response = requests.get(self.__movie_url, headers=self.__headers)

        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None

        raise Exception(f'Erro ao buscar reviews. Status code: {response.status_code}')

    def create_review(self, review):
        response = requests.post(
            self.__movie_url,
            headers=self.__headers,
            json=review,
        )

        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None

        raise Exception(f'Erro ao criar review. Status code: {response.status_code}')
