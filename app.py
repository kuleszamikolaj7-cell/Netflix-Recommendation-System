
import streamlit as st
from pathlib import Path
from recommender import NetflixRecomennderSystem

# Page configuration
st.set_page_config(
    page_title="Netflix Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# Netflix-style theme
st.markdown("""
<style>
    .stApp {
        background-color: #0e0f14;
        color: #ffffff;
    }

    h1, h2, h3 {
        color: #ffffff !important;
    }

    .stButton > button {
        background-color: #E50914;
        color: white;
        border: none;
        border-radius: 8px;
        height: 50px;
        font-weight: bold;
        width: 100%;
    }

    .stButton > button:hover {
        background-color: #b20710;
        color: white;
        border: none;
    }

    [data-testid="stMetricValue"] {
        color: #E50914;
    }

    hr {
        border-color: #333333;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.title("🎬 Netflix Recommendation System")
st.caption("Discover your next favorite movie")
st.divider()

# User settings
st.subheader("⚙️ Recommendation Settings")

genre = st.selectbox(
    "Movie Genre",
    ["Comedy", "Drama", "Action",
     "Horror", "Thriller", "Romance",
     "Adventure", "Sci-Fi", "Animation"]
)

votesThrs = st.slider(
    "Popularity threshold",
    min_value=0,
    max_value=95,
    value=80,
    step=5,
    format="%d%%"
)

topN = st.radio(
    "Number of recommendations",
    [5, 10, 20],
    horizontal=True
)

st.divider()

# Recommendation button
if st.button("🔍 Get Recommendations"):

    path = Path(__file__).resolve().parent / "imdb.csv"

    if not path.exists():
        st.error("File imdb.csv not found!")

    else:
        try:
            recommender = NetflixRecomennderSystem(
                str(path),
                genre,
                votesThrs / 100,
                topN
            )

            results = recommender.run()

            if results is None or results.empty:
                st.warning("No movies found.")

            else:
                st.success("Recommendations generated!")

                st.subheader(
                    f"🍿 Top {len(results)} {genre} Movies"
                )

                st.dataframe(
                    results,
                    use_container_width=True,
                    hide_index=True
                )

                st.metric(
                    "Movies recommended",
                    len(results)
                )

        except Exception as e:
            st.error(f"Something went wrong: {e}")

st.divider()

st.caption(
    "Netflix Recommendation System | "
    "Built with Python, Pandas & Streamlit"
)
