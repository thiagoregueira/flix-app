from datetime import date
import time
import streamlit as st
import pandas as pd
import unicodedata

from st_aggrid import AgGrid
from actors.service import ActorService


def show_actors_page():
    st.markdown('## Lista de Atores')
    actor_service = ActorService()
    actors = actor_service.get_actors()

    if actors:
        actors_df = pd.json_normalize(actors)
        AgGrid(
            data=actors_df,
            reload_data=True,
            key='actors_grid',
        )
    else:
        st.warning('Nenhum ator/atriz encontrado.')

    st.markdown('## Cadastrar novo Ator')
    name = st.text_input('Nome do(a) ator/atriz')
    birthday = st.date_input(
        label='Data de nascimento',
        value=date.today(),
        max_value=date.today(),
        format='DD/MM/YYYY',
        key='birthday',
        min_value=date(1900, 1, 1),
    )
    nationality_options = [
        'USA',
        'BRAZIL',
        'CANADA',
        'FRANCE',
        'GERMANY',
        'ITALY',
        'SPAIN',
        'AUSTRALIA',
        'CHINA',
        'INDIA',
        'JAPAN',
        'ARGENTINA',
        'MEXICO',
        'UK',
        'AUSTRIA',
        'BELGIUM',
        'CZECH_REPUBLIC',
        'DENMARK',
    ]

    nationality = st.selectbox(
        'Nacionalidade',
        options=sorted(
            nationality_options,
            key=lambda x: unicodedata.normalize('NFD', x).encode('ascii', 'ignore').decode('utf-8').lower(),
        ),
    )
    if st.button('Cadastrar'):
        try:
            actor_service.create_actor(name, birthday, nationality)
            st.success(f'Ator/atriz {name} cadastrado(a) com sucesso!')
            time.sleep(2)
            st.rerun()
        except Exception:
            st.error(f'Erro ao cadastrar ator/atriz: {name}')
