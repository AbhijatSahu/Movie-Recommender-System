import streamlit as st
import pandas as pd
import pickle
from rapidfuzz import process, fuzz

# Load similarity matrix
with open('similar_movies.pkl', 'rb') as f:
    similarity_matrix = pickle.load(f)

# Load movies data
with open('movie.pkl', 'rb') as f:
    movie = pickle.load(f)

def recommend(title, similarity_matrix=similarity_matrix, movie=movie):
    movie_names = movie['name'].tolist()
    matches = process.extract(title, movie_names, scorer=fuzz.ratio, limit=5)
    best_match = matches[0][0]
    movie_id = movie.loc[movie['name'] == best_match, 'id'].values[0]

    similar = similarity_matrix[similarity_matrix['movieId'] == movie_id]
    if similar.empty:
        return best_match, movie.loc[movie['name'] == best_match].iloc[0], []

    similar_movies = similar['similar_movies'].values[0]
    recommendations = []
    for sim_id, _ in similar_movies:
        if sim_id == movie_id:
            continue
        row = movie.loc[movie['id'] == sim_id]
        if not row.empty:
            recommendations.append(row.iloc[0])
            if len(recommendations) == 5:
                break

    return best_match, movie.loc[movie['name'] == best_match].iloc[0], recommendations

# Streamlit UI
st.set_page_config(layout="wide")
st.title("🎬 Movie Recommender System")

all_titles = ["Select a movie"] + movie['name'].tolist()
selected_movie = st.selectbox("Select a movie", all_titles)

if selected_movie != "Select a movie":
    match_name, match_data, recommendations = recommend(selected_movie)

    # CSS for tooltip
    st.markdown("""
    <style>
    .tooltip-container {
        position: relative;
        display: inline-block;
    }
    .tooltip-text {
        visibility: hidden;
        width: 200px;
        background-color: rgba(0, 0, 0, 0.85);
        color: #fff;
        text-align: left;
        border-radius: 6px;
        padding: 10px;
        position: absolute;
        bottom: 0;
        right: 0;
        z-index: 1;
        font-size: 12px;
    }
    .tooltip-container:hover .tooltip-text {
        visibility: visible;
    }
    img {
        border-radius: 12px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Main movie being recommended for
    st.markdown("<h3 style='text-align: center;'>Recommendations for</h3>", unsafe_allow_html=True)
    st.markdown(f"""
        <div style='display: flex; justify-content: center;'>
            <div class='tooltip-container'>
                <img src="{match_data['poster']}" width="200" />
                <div class='tooltip-text'>{match_data['description']}</div>
            </div>
        </div>
        <h4 style='text-align: center;'>{match_data['name']}</h4>
        <p style='text-align: center; color: gray; font-style: italic;'>{match_data['tagline']}</p>
        <p style='text-align: center;'><b>Rating:</b> {match_data['rating']}/5</p>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("<h4 style='text-align: center;'>Top 5 Recommendations:</h4>", unsafe_allow_html=True)

    # Show 5 recommendations in a row
    cols = st.columns(5)
    for col, rec in zip(cols, recommendations):
        with col:
            st.markdown(f"""
                <div class='tooltip-container'>
                    <img src="{rec['poster']}" width="180" />
                    <div class='tooltip-text'>{rec['description']}</div>
                </div>
                <div style='font-weight: bold; margin-top: 8px;'>{rec['name']}</div>
                <div style='font-size: smaller; color: gray; font-style: italic;'>{rec['tagline']}</div>
                <div><b>Rating:</b> {rec['rating']}/5</div>
            """, unsafe_allow_html=True)