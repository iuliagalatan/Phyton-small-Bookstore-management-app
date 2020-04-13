from domain.Book import *

class BookRepo:
    def __init__(self):
        self._books=[]

    @property
    def books(self):
        return self._books

    def add_book(self, name, author):
        '''
        adds a new book to the list ok books
        :param name: name of book
        :param author: author of book
        :return: nothing, appends to the list
        '''
        b = Book(name, author)
        self._books.append(b)
    def add_book2(self, book):
        self._books.append(book)
    def sort(self):
        self._books.sort()
    def remove_book(self, id):
        '''
        Function for the Filter operation. Filters after id
        :param id: book id which we want to filter
        :return: nothing, modifies self.books[] list
        '''
        self.books.remove(self.books[id])

    def remove_book2(self,book):
        self.books.remove(book)

    def update_books(self, b, nname, nauthor):
        '''
        updates book
        :param id: id of the book
        :param nname: new name
        :param nauthor: new author
        :return: modifies list
        '''

        b.title = nname
        b.author = nauthor

    def get_all(self):
        return self._books

    def initialisebooks(self):
        b = Book('ion', 'liviu rebreanu')
        self._books.append(b)
        b = Book('ion', 'aaa')
        self._books.append(b)

        b = Book('ursul', 'mihail sadoveanu')
        self._books.append(b)

        b = Book('Amintiri din copilarie', 'Ion Creanga')
        self._books.append(b)

        b = Book('Colt Alb', 'Jack P.')
        self._books.append(b)

        b = Book('Colt Alb', 'Jack P.')
        self._books.append(b)

        b = Book('Carte de bucate', 'Cristina Stamate')
        self._books.append(b)

        b = Book('Another one', 'unknown')
        self._books.append(b)

        b = Book('Tinkerbell', 'Peter Pan')
        self._books.append(b)

        b = Book('Lala', 'ding-dong')
        self._books.append(b)

