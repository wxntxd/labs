class Book:
    def __init__(self,title, author,year):
        self.title = "Harry Potter"
        self.author = "Joanne Rowling"
        self.year = 1997
    def get_title(self):
        return  f"Title {self.title}"
    def get_info(self):
        return f"Title is {self.title},author : {self.author}, year of publication:{self.year}"
book = Book("Harry Potter" , "Joanne Rowling", 1997)
print(book.get_info())
