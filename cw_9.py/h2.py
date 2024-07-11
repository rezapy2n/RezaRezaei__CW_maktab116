import pickle

class FavoriteMovies:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
       
        self.movies.append(movie)

    def remove_movie(self, movie):
        
        if movie in self.movies:
            self.movies.remove(movie)
        else:
            print(f"{movie} is not in the list.")

    def list_movies(self):
        
        for movie in self.movies:
            print(movie)

    def save_to_file(self, filename):
        
        with open(filename, 'wb') as file:
            pickle.dump(self.movies, file)
        print(f"Movie list saved to {filename}.")

    def load_from_file(self, filename):
        
        try:
            with open(filename, 'rb') as file:
                self.movies = pickle.load(file)
            print(f"Movie list loaded from {filename}.")
        except FileNotFoundError:
            print(f"{filename} not found. Starting with an empty list.")


if __name__ == "__main__":
    my_movies = FavoriteMovies()
    my_movies.add_movie("antman")
    my_movies.add_movie("LOL")
    my_movies.list_movies()

   
    my_movies.save_to_file("favorite_movies.pkl")

 
    loaded_movies = FavoriteMovies()
    loaded_movies.load_from_file("favorite_movies.pkl")
    loaded_movies.list_movies()
