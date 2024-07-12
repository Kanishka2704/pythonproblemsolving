#constructor

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def display_info(self):
        print(f"Book details: Title is {self.title}, Author is {self.author}")

book1 = Book("Harry Potter and the Chamber of Secrets","J.K. Rowling")
book2 = Book("The Jungle","Upton Sinclair")
book1.display_info()
book2.display_info()


    
