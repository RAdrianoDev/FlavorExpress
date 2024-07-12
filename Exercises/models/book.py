class Book:
    books = []

    def __init__(self, title, bookAuthor, pages):
        self.title = title
        self.bookAuthor = bookAuthor
        self.pages = pages
        Book.books.append(self)

    def __str__(self):
        return f'{self.title} por {self.bookAuthor} - {self.pages} páginas'

    @property
    def titulo_autor(self):
        return f'{self.title} por {self.bookAuthor}'

    def increase_pages(self, quantity):
        self.pages += quantity
    
    @classmethod
    def list_books(cls):
        print(f'{"*** Title ***".ljust(25)} | {"*** Author ***".ljust(25)} | *** Pages ***')
        for book in cls.books:
            print(f'{book.title.ljust(25)} | {book.bookAuthor.ljust(25)} | {book.pages}')
    
book_1 = Book('Python Crash Course', 'Eric Matthes', 416)
book_2 = Book('Clean Code', 'Robert C. Martin', 464)
book_3 = Book('The Pragmatic Programmer', 'Andrew Hunt', 352)
book_4 = Book('Design Patterns', 'Erich Gamma', 395)

Book.list_books()
