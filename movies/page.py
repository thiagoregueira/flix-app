from datetime import date
import streamlit as st
import pandas as pd
import time
from st_aggrid import AgGrid
from movies.service import MovieService
from genres.service import GenreService
from actors.service import ActorService


def show_movies_page():
    st.markdown('## Filmes')
    movie_service = MovieService()
    movies = movie_service.get_movies()
    genre_service = GenreService()
    genres = genre_service.get_genres()
    actor_service = ActorService()
    actors = actor_service.get_actors()

    if movies:
        movies_df = pd.json_normalize(movies)
        if 'rate' in movies_df.columns:
            movies_df['rate'] = movies_df['rate'].astype(str)

        movies_df = movies_df.drop(columns=['actors', 'genre.id'])
        AgGrid(
            data=movies_df,
            reload_data=True,
            key='movies_grid',
        )
    else:
        st.warning('Nenhum filme encontrado.')

    st.markdown('## Cadastrar novo Filme')
    title = st.text_input(label='Titulo do filme')
    genre_name = {genre['name']: genre['id'] for genre in genres}
    selected_genre_name = st.selectbox(label='Gênero', options=list(genre_name.keys()))
    release_date = st.date_input(
        label='Data de lançamento',
        value=date.today(),
        max_value=date.today(),
        format='DD/MM/YYYY',
        key='release_date',
        min_value=date(1900, 1, 1),
    )
    resume = st.text_area(label='Resumo')
    actors_name = {actor['name']: actor['id'] for actor in actors}
    selected_actors_name = st.multiselect(label='Atores', options=list(actors_name.keys()))
    selected_actors_id = [actors_name[name] for name in selected_actors_name]
    if st.button('Adicionar Filme'):
        try:
            movie_service.create_movie(
                title=title,
                release_date=release_date,
                genre=genre_name[selected_genre_name],
                resume=resume,
                actors=selected_actors_id,
            )

            st.success(f'Filme {title} cadastrado com sucesso!')
            time.sleep(2)
            st.rerun()
        except Exception:
            st.error(f'Erro ao cadastrar filme: {title}.')
