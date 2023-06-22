import requests
import time
import pandas as pd

# API key and URLs
api_key = "79bc37f757b05c716c2d839e6678172d"
base_url = "https://api.themoviedb.org/3/discover/movie"
genre_url = "https://api.themoviedb.org/3/genre/movie/list"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3OWJjMzdmNzU3YjA1YzcxNmMyZDgzOWU2Njc4MTcyZCIsInN1YiI6IjY0OTQ5NDI4OWEzNThkMDEzOWUwMWQwOSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.2gZFfjL-BE9iF_dUm9iFgjfr9RpK6r20rg5B_hrY5wE"
}

genre_response = requests.get(genre_url, headers=headers)
genre_data = genre_response.json()
genre_lookup = {genre['id']: genre['name'] for genre in genre_data['genres']}

movies = []
movies_df = pd.DataFrame(
    columns=['title', 'genre_ids', 'overview', 'vote_average'])
for page in range(1, 201):
    params = {
        "page": page,
        "api_key": api_key
    }
    response = requests.get(base_url, headers=headers, params=params)
    data = response.json()

    if response.status_code == 200:
        movies.extend(data['results'])
    else:
        print("Error on page", page, ":", response.status_code)
        break

    time.sleep(0.5)  # Add a delay of 1 second between requests

for movie in movies:
    genre_ids = movie['genre_ids']
    movie['genre_ids'] = [genre_lookup[genre_id] for genre_id in genre_ids]

for movie in movies:
    movie_title = movie['title']
    movie_genre = movie['genre_ids']
    movie_overview = movie['overview']
    movie_avg = movie['vote_average']

    movies_df = movies_df.append({'title': movie_title, 'genre_ids': movie_genre,
                                 'overview': movie_overview, 'vote_average': movie_avg}, ignore_index=True)

movies_df = movies_df.rename(columns={'genre_ids': 'genre'})
print(movies_df.head())
movies_df.to_csv('movies.csv', index=False)
