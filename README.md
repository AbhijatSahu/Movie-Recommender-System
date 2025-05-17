# 🎬 Movie Recommender System

An intelligent and interactive Movie Recommender System built using **Streamlit**, **pandas**, **scikit-learn**, and **RapidFuzz**. It allows users to get movie recommendations based on selected titles, complete with posters, taglines, ratings, and descriptions.

---

## 🚀 Features

- 🎥 Select any movie from a list of thousands.
- 🧠 Get 5 intelligent recommendations based on content similarity.
- 🖼️ View movie posters and taglines.
- ⭐ Ratings out of 5 for each movie.
- 💬 Hover over posters to view descriptions.
- 🗂️ Browse all movies in a separate "Movies" page.
- 🔍 Clicking on any movie gives recommendations for it.

---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/AbhijatSahu/Movie-Recommender-System.git
cd Movie-Recommender-System```

```
### 2. Set up a virtual environment (optional but recommended)
bash
Copy
Edit
python -m venv venv
# For Linux/macOS
source venv/bin/activate
# For Windows
venv\Scripts\activate
```
### 3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
### 4. Run the Streamlit app
bash
Copy
Edit
streamlit run app.py
### 📦 File Structure
bash
Copy
Edit
Movie-Recommender-System/
│
├── app.py                  # Main Streamlit app
├── movie.pkl               # Movie dataset with names, posters, ratings, taglines, descriptions
├── similar_movies.pkl      # Precomputed similarity matrix for recommendations
├── similarity.ipynb        # Jupyter notebook to compute similarity matrix
├── requirements.txt        # Required Python libraries
├── README.md               # Project documentation
└── screenshots/            # Folder for UI demo images (optional)
### ⚙️ Dependencies
Below are the main libraries used in this project (also included in requirements.txt):

plaintext
Copy
Edit
streamlit
pandas
scikit-learn
rapidfuzz
numpy
📖 Usage
Open the app in your browser using the Streamlit command above.

Select a movie from the dropdown list on the home page.

View the movie details (poster, tagline, rating, description).

See the top 5 recommended movies displayed horizontally.

Navigate to the "Movies" page to browse all movies and get recommendations by clicking on any movie.

🧑‍💻 Development Notes
similarity.ipynb contains the code for building the similarity matrix based on movie features.

The pickled files (movie.pkl and similar_movies.pkl) store your preprocessed datasets and similarity scores.

Ensure your pickle files are in the same directory as app.py.
