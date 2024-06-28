class Book:
    def __init__(self, title, author, published_year):
        self.title = title
        self.author = author
        self.published_year = published_year

    def get_summary(self):
        return f"{self.title} by {self.author}, published in {self.published_year}"


my_book = Book(title="Love", author="reza.r", published_year=1377)


print(my_book.get_summary())
