from models.book import Book

book1 = Book("Hamlet", "Drama", "Shakespeare")
book2 = Book("Think and grow rich", "Self-help", "Napoleon Hill")
book3 = Book("The Shinning", "Horror", "Stephen King")

books = [book1, book2, book3]

def add_book(book):
    books.append(book)

def delete_book(index):
    books.pop(index)