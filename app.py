import csv
import math
import re
import streamlit as st


# Load movies from CSV
movies = []

with open("movies.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for row in reader:
        movies.append({
            "title": row["title"],"genres": row["genres"]
        })


# Create TF-IDF vectors using only Python
documents = [movie["genres"].lower() for movie in movies]

tokenized = [
    re.findall(r"\b\w+\b", document)
    for document in documents
]

vocabulary = sorted(set(
    word
    for document in tokenized
    for word in document
))

N = len(documents)

idf = {}

for word in vocabulary:
    document_count = sum(word in document for document in tokenized)
    idf[word] = math.log((N + 1) / (document_count + 1)) + 1


def tfidf_vector(words):
    counts = {}

    for word in words:
        counts[word] = counts.get(word, 0) + 1

    total = len(words)

    return {
        word: (count / total) * idf[word]
        for word, count in counts.items()
    }


vectors = [
    tfidf_vector(words)
    for words in tokenized
]


def cosine_similarity(vector_a, vector_b):
    all_words = set(vector_a) | set(vector_b)

    dot_product = sum(
        vector_a.get(word, 0) * vector_b.get(word, 0)
        for word in all_words
    )

    magnitude_a = math.sqrt(
        sum(value ** 2 for value in vector_a.values())
    )

    magnitude_b = math.sqrt(
        sum(value ** 2 for value in vector_b.values())
    )

    if magnitude_a == 0 or magnitude_b == 0:
        return 0

    return dot_product / (magnitude_a * magnitude_b)


def recommend(movie_title):
    movie_index = next(
        i for i, movie in enumerate(movies)
        if movie["title"] == movie_title
    )

    similarities = []

    for i, vector in enumerate(vectors):
        if i != movie_index:
            similarity = cosine_similarity(
                vectors[movie_index],
                vector
            )
            similarities.append((similarity, movies[i]["title"]))

    similarities.sort(reverse=True)

    return [
        title
        for similarity, title in similarities[:5]
    ]


# Streamlit interface
st.title("🎬 Movie Recommendation System")

movie_name = st.selectbox(
    "Choose a Movie",
    [movie["title"] for movie in movies]
)

if st.button("Recommend"):
    recommendations = recommend(movie_name)

    st.subheader("Recommended Movies:")

    for movie in recommendations:
        st.write("✅", movie)