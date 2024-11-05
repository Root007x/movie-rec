import streamlit as st
import pickle
import pandas as pd


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies_list = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))


def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    ls = []
    for i in movies:
        ls.append(movies_list.iloc[i[0]].title)
    return ls


st.title("Movie Recommender System")

movie_name = st.selectbox(
    "Select or Search your movie",
    (movies_list['title'])
)

if st.button("Rcommended"):
    movie_ls = recommend(movie_name)
    for i in movie_ls:
        st.write(i)
