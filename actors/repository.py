import requests
import streamlit as st

from login.service import logout


class ActorRepository:
    def __init__(self):
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}',
            'Content-Type': 'application/json',
        }
        self.__base_url = 'https://flixapi.dominio.qzz.io/'
        self.__api_version = 'api/v1/'
        self.__actor_url = self.__base_url + self.__api_version + 'actors/'

    def get_actors(self):
        response = requests.get(self.__actor_url, headers=self.__headers)
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None

        raise Exception(f'Erro ao buscar atores. Status code: {response.status_code}')

    def create_actor(self, actor):
        response = requests.post(
            self.__actor_url,
            headers=self.__headers,
            json=actor,
        )
        if response.status_code == 201:
            return response.json()
        if response.status_code == 401:
            logout()
            return None

        raise Exception(f'Erro ao criar ator. Status code: {response.status_code}')
