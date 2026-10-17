# Movie Recommendation System

## Project Overview

This project is a Python-based movie recommendation system that suggests movies similar to a selected title based on their genres.

It uses a content-based filtering approach with TF-IDF weighting and cosine similarity to compare movie genres and recommend the five most similar movies. A Streamlit interface allows users to select a movie and view recommendations interactively.

## Features

- Select a movie from a dropdown menu.
- Recommend five similar movies based on genre similarity.
- Use TF-IDF weighting to represent movie genres numerically.
- Calculate similarity using cosine similarity.
- Display recommendations through an interactive web interface.
- Process movie data from a CSV file.

## Technologies Used

- **Python** — Core programming language.
- **Streamlit** — Interactive web interface.
- **CSV** — Movie dataset storage.
- **Regular Expressions** — Text tokenization.
- **TF-IDF** — Genre-based text representation.
- **Cosine Similarity** — Similarity calculation between movies.

## How It Works

1. **Load the dataset:** Read movie titles and genres from `movies.csv`.
2. **Process genres:** Convert genre descriptions into lowercase tokens.
3. **Calculate TF-IDF weights:** Assign weights to genre terms based on their occurrence across the dataset.
4. **Calculate similarity:** Compare movie vectors using cosine similarity.
5. **Generate recommendations:** Rank other movies by similarity and select the top five.
6. **Display results:** Show recommendations in the Streamlit interface.

## Project Structure

```text
movie-recommendation-system/
├── app.py
├── movies.csv
├── requirements.txt
└── README.md
```

## Installation and Setup

### Prerequisites

- Python 3
- pip package manager

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/movie-recommendation-system.git
cd movie-recommendation-system
```

Replace `YOUR-USERNAME` with your GitHub username.

Alternatively, download the repository as a ZIP file and extract it.

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv .venv
```

Activate it on Windows:

```cmd
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

Ensure `requirements.txt` includes:

```text
streamlit
```

### 4. Run the Application

```bash
python -m streamlit run app.py
```

Streamlit will provide a local URL, usually `http://localhost:8501`, where you can access the application.

## Dataset

The project uses `movies.csv`, which contains movie titles and genre information.

The CSV file must include these columns:

- `title` — Movie title.
- `genres` — Genre information used to calculate similarity.

## Limitations

- Recommendations are based on genres only.
- The system does not use user preferences, viewing history, or movie ratings.
- Recommendation quality depends on the dataset's content and variety.
- The project does not use a trained predictive model.

## Future Improvements

- Include movie ratings and descriptions.
- Add movie posters and release-year information.
- Improve recommendations using additional movie features.
- Allow users to filter recommendations by genre.
- Deploy the application online for public access.

## Learning Outcomes

This project demonstrates practical concepts in Python, text processing, content-based recommendation systems, similarity calculations, and interactive application development.

