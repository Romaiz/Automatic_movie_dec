from flask import Flask, render_template, request
from random import choice, sample
import pandas as pd
app = Flask(__name__)

# Load the movie data
movies_df = pd.read_csv('movies.csv')
movies_df.reset_index(drop=True, inplace=True)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/recommendations')
def recommendations():
    # Get user inputs
    critical_input = request.args.get('critical_input')
    genre_input = request.args.get('genre_input')

    # Filter movies based on user inputs
    filtered_movies_df = movies_df.copy()
    if critical_input == 'n':
        filtered_movies_df = filtered_movies_df[filtered_movies_df['vote_average'] >= 7]
    if genre_input:
        filtered_movies_df = filtered_movies_df[~filtered_movies_df['genre'].str.contains(
            genre_input, case=False)]
        filtered_movies_df.reset_index(drop=True, inplace=True)
    # Get random movie recommendations
    num_movies = len(filtered_movies_df)
    random_movies = sample(range(num_movies), min(5, num_movies))
    movie_recommendations = []
    for index in random_movies:
        movie = filtered_movies_df.loc[index]
        movie_title = movie['title']
        movie_genre = movie['genre']
        movie_overview = movie['overview']
        movie_recommendations.append({
            'title': movie_title,
            'genre': movie_genre,
            'overview': movie_overview
        })

    return render_template('recommendation.html', recommendations=movie_recommendations)


if __name__ == '__main__':
    app.run()
