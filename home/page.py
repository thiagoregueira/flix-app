import streamlit as st

import plotly.express as px
from movies.service import MovieService


def show_home_page():
    movie_service = MovieService()
    movie_stats = movie_service.get_movie_stats()

    st.title('Estatísticas de Filmes')

    if len(movie_stats['movies_by_genre']) > 0:
        st.subheader('Filmes por Gênero')
        fig = px.pie(
            movie_stats['movies_by_genre'],
            names='genre__name',
            values='count',
            title='Filmes por Gênero',
        )
        st.plotly_chart(fig)

    st.subheader('Total de Filmes Cadastrados:')
    st.write(movie_stats['total_movies'])

    st.subheader('Filmes por Gênero')
    for genre in movie_stats['movies_by_genre']:
        st.write(f'{genre["genre__name"]}: {genre["count"]}')

    st.subheader('Total de Avaliações Cadastradas:')
    st.write(movie_stats['total_reviews'])

    st.subheader('Média Geral de Estrelas nas Avaliações:')
    st.write(movie_stats['general_average_stars'])
