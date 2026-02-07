import streamlit as st

from genres.page import show_genres_page
from actors.page import show_actors_page
from movies.page import show_movies_page
from reviews.page import show_reviews_page
from login.page import show_login_page
from home.page import show_home_page


def main():
    if 'token' not in st.session_state:
        show_login_page()
    else:
        st.title('Flix App')

        menu_option = st.sidebar.selectbox(
            'Selecione uma opção', ['Início', 'Gêneros', 'Atores', 'Filmes', 'Avaliações']
        )

        if menu_option == 'Início':
            show_home_page()
        elif menu_option == 'Gêneros':
            show_genres_page()
        elif menu_option == 'Atores':
            show_actors_page()
        elif menu_option == 'Filmes':
            show_movies_page()
        elif menu_option == 'Avaliações':
            show_reviews_page()


if __name__ == '__main__':
    main()
