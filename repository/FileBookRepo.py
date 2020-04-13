from repository.BookRepository import *

class FileBookRepo(BookRepo):
    def __init__(self, fileName):
        BookRepo.__init__(self)
        self._file = fileName
        self.LoadFile()

    def LoadFile(self):
        try:
            f = open(self._file, "r")
        except IOError:
            print("File does not exist!")
            return
        line = f.readline().strip()
        while line != "":
            l = line.split(",")
            book = Book(l[0], l[1])
            BookRepo.add_book2(self, book)
            line = f.readline().strip()
        f.close()

    def add_book(self, name, author):
        BookRepo.add_book(self, name, author)
        self.WriteAll()


    def WriteAll(self):
        f = open(self._file, "w")
        Books = BookRepo.get_all(self)
        for s in Books:
            line = str(s.title) + ',' +  str(s.author) + '\n'
            f.write(line)
        f.close()

    def remove_book2(self, book):
        super().remove_book2( book)
        self.WriteAll()

    def update_Book(self, Book, name, author):
        BookRepo.update_books(self, Book, name, author)
        self.WriteAll()