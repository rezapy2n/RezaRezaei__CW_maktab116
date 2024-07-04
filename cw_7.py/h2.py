class Movie:
    def __init__(self, title, director, duration):
        self._title = title
        self._director = director
        self._duration = duration

   
    def get_title(self):
        return self._title

    def get_director(self):
        return self._director

    def get_duration(self):
        return self._duration

   
    def set_title(self, title):
        if isinstance(title, str) and title.strip():
            self._title = title
        else:
            print("Title must be a non-empty string.")

    def set_director(self, director):
        if isinstance(director, str) and director.strip():
            self._director = director
        else:
            print("Director must be a non-empty string.")

    def set_duration(self, duration):
        if isinstance(duration, int) and duration > 0:
            self._duration = duration
        else:
            print("Duration must be a positive integer.")

    
    def display_details(self):
        print(f"Title: {self._title}")
        print(f"Director: {self._director}")
        print(f"Duration: {self._duration} minutes")



movie1 = Movie("Inception", "Christopher Nolan", 148)
movie1.display_details()


movie1.set_title("Interstellar")
movie1.set_director("Christopher Nolan")
movie1.set_duration(169)
movie1.display_details()
