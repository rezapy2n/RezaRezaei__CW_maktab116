class Book:
    def __init__(self, title, author, published_year):
        self.title = title
        self.author = author
        self.published_year = published_year


my_book = Book(title=" Love", author="reza.r", published_year=1377)

# Print the details
print(f"Title: {my_book.title}")
print(f"Author: {my_book.author}")
print(f"Published Year: {my_book.published_year}")
