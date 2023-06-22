from random import choice, sample
import pandas as pd

movies_df = pd.read_csv('movies.csv')
# print(movies_df.head())
critical_input = input("Consider movies under 7? (y/n): ")
if critical_input.lower() == 'n':
    movies_df = movies_df[movies_df['vote_average'] >= 7]

genre_input = input("Enter a genre to avoid (or press Enter to skip): ")
if genre_input:
    movies_df = movies_df[~movies_df['genre'].str.contains(
        genre_input, case=False)]
movies_df.reset_index(drop=True, inplace=True)

random_movies = sample(range(len(movies_df)), 5)
for index in random_movies:
    movie = movies_df.loc[index]
    movie_title = movie['title']
    movie_genre = movie['genre']
    movie_overview = movie['overview']

    print("Title:", movie_title)
    print("Genre:", movie_genre)
    print("Overview:", movie_overview)
    print("---------------")
