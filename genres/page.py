import streamlit as st
import pandas as pd
import time

from st_aggrid import AgGrid
from genres.service import GenreService


def show_genres_page():
    st.markdown('## Lista de Gêneros')

    genre_service = GenreService()
    genres = genre_service.get_genres()

    if genres:
        genres_df = pd.json_normalize(genres)
        AgGrid(
            data=genres_df,
            reload_data=True,
            key='genres_grid',
        )
    else:
        st.warning('Nenhum gênero encontrado.')

    st.markdown('## Cadastrar novo Gênero')
    name = st.text_input('Nome do gênero')
    if st.button('Cadastrar'):
        try:
            new_genre = genre_service.create_genre({'name': name})
            if new_genre:
                st.success(f'Gênero {name} cadastrado com sucesso!')
                time.sleep(2)
                st.rerun()
            else:
                st.error(f'Erro ao cadastrar gênero {name}, verifique os dados e tente novamente.')
        except Exception as e:
            st.error(f'Erro ao cadastrar gênero: {e}')
