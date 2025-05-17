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
cd Movie-Recommender-System

### 2. Set up a virtual environment (optional but recommended)
python -m venv venv
# For Linux/macOS
source venv/bin/activate
# For Windows
venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt

### ▶️ Running the App
streamlit run app.py

### 📦 File Structure
Movie-Recommender-System/
│
├── app.py                  # Main Streamlit app
├── movie.pkl               # Movie dataset with names, posters, ratings
├── similar_movies.pkl      # Precomputed similarity matrix
├── similarity.ipynb        # Notebook to compute similarity matrix
├── requirements.txt        # Required Python libraries
├── README.md               # Project documentation
└── screenshots/            # Folder for UI demo images
