class Book:
    title = ""
    author = ""
    publication_year = 0

    def set_info(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.publication_year}"


book1 = Book()


book1.set_info("To Kill a Mockingbird", "Harper Lee", 1960)


print("Title:", book1.title)
print("Author:", book1.author)
print("Year:", book1.publication_year)


book_info = book1.display_info()
print(book_info)
