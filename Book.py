class Book:
    def __init__(self,title,author):
        self.name = title
        self.author = author
    def details(self):
        print(f"{self.name} is written by {self.author}")
b1 = Book("The Great Gatsby","F. Scott Fitzgerald")
b1.details()
b2 = Book("python Basics","John Doe")
b2.details()