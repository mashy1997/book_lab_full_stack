from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author("Shakespeare")
author_repository.save(author1)

author2 = Author("Napoleon Hill")
author_repository.save(author2)

author3 = Author("Stephen King")
author_repository.save(author3)

author_repository.select_all()

book_1 = Book("Hamlet", "Drama", author1)
book_repository.save(book_1)

book_2 = Book("Think and grow rich", "Self-help", author2)
book_repository.save(book_2)

book_3 = Book("The Shinning", "Horror", author3)
book_repository.save(book_3)