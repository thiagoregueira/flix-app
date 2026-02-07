import requests


class Auth:
    def __init__(self):
        self.__base_url = 'https://flixapi.dominio.qzz.io/'
        self.__api_version = 'api/v1/'
        self.__auth_url = self.__base_url + self.__api_version + 'authentication/token/'

    def get_token(self, username, password):
        auth_payload = {
            'username': username,
            'password': password,
        }
        auth_response = requests.post(
            self.__auth_url,
            data=auth_payload,
        )
        if auth_response.status_code == 200:
            return auth_response.json()
        return {'error': f'Erro ao autenticar usuário. Status code: {auth_response.status_code}'}
