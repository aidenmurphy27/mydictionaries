#create dictionary
movie_ratings =  {'Spider-Man':'10',
                  'Knives-Out':'10', 
                  'Back to the Future': '9',
                  'Kung Fu Panda':'8',
                  'Avengers':'7',
                  'Wall-E':'5'}

#get user input
movie_title = input('Please enter a movie title: ')
#recommended movies function
recommended_movies = []

for title, rating in movie_ratings.items():
    if int(rating) >= 8:
        recommended_movies.append(title)

if movie_title in movie_ratings:
    rating = movie_ratings[movie_title]

    if int(rating) >= 8:
        print(f"Your selected movie: {movie_title} is recommended!")
    else:
        print(f"Your selected movie: {movie_title} is not recommended\n We recommend the following movies: {recommended_movies}")
else: 
    print(f"Selected movie not found, we recommend the following movies: {recommended_movies}")

