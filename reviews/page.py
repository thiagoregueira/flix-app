import streamlit as st
import pandas as pd
import time

from st_aggrid import AgGrid
from reviews.service import ReviewService
from movies.service import MovieService


def show_reviews_page():
    review_service = ReviewService()
    reviews = review_service.get_reviews()

    movie_service = MovieService()
    movies = movie_service.get_movies()
    movie_titles_dict = {movie['id']: movie['title'] for movie in movies}

    if reviews:
        st.markdown('## Lista de Avaliações')

        reviews_df = pd.json_normalize(reviews)
        reviews_df['movie'] = reviews_df['movie'].map(movie_titles_dict)

        AgGrid(
            data=reviews_df,
            reload_data=True,
            key='reviews_grid',
        )
    else:
        st.warning('Nenhuma avaliação cadastrada.')

    st.markdown('## Cadastrar nova Avaliação')

    movie_titles = {movie['title']: movie['id'] for movie in movies}
    selected_movie_title = st.selectbox('Filme', list(movie_titles.keys()))

    stars = st.number_input(
        label='Estrelas',
        min_value=0,
        max_value=5,
        step=1,
        value=0,
    )
    comment = st.text_area(
        label='Comentário',
        placeholder='Digite seu comentário',
        value='',
    )

    if st.button('Cadastrar'):
        new_review = review_service.create_review(
            movie=movie_titles[selected_movie_title],
            stars=stars,
            comment=comment,
        )

        if new_review:
            st.success(f'Avaliação do filme {selected_movie_title} cadastrada com sucesso!')
            time.sleep(2)
            st.rerun()
        else:
            st.error(f'Erro ao cadastrar avaliação do filme {selected_movie_title}.')
