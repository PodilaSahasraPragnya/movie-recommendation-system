# 🎬 Movie Recommendation System

## 📌 Overview
The Movie Recommendation System is a simple machine learning project that recommends similar movies based on their genres. It uses a content-based filtering approach with TF-IDF vectorization and cosine similarity.

## 🚀 Features
- Recommend movies based on selected movie.
- Content-based recommendation using genres.
- Simple and user-friendly Streamlit interface.
- Fast and lightweight.

## 🛠 Technologies Used
- Python
- Pandas
- Scikit-learn
- Streamlit

## 📂 Project Structure
```
movie_recommender/
│── app.py
│── movies.csv
│── requirements.txt
│── README.md
```

## 📊 Dataset
The project uses a movie dataset (`movies.csv`) containing:
- Movie Title
- Genres

## ⚙️ Installation

Install the required packages:

```bash
pip install streamlit pandas scikit-learn
```

## ▶️ Run the Project

```bash
python -m streamlit run app.py
```

## 📸 Output
- Select a movie from the dropdown.
- Click **Recommend**.
- The system displays the top 5 similar movies.

## 📈 Future Improvements
- Use the full MovieLens dataset.
- Add movie posters.
- Add ratings and user reviews.
- Deploy using Streamlit Cloud.

