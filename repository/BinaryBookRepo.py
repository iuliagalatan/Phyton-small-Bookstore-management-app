from repository.BookRepository import *
import pickle

class BinaryBookRepo(BookRepo):
    def __init__(self, fileName):
        BookRepo.__init__(self)
        
        self._file = fileName
        
        self.LoadFile()

    def LoadFile(self):
        try:
            f = open(self._file, "rb")
        except IOError:
            print("File not found! ")
        except EOFError :
            Repo_student._books = []
        try:
            entities = pickle.load(f)
            for e in entities:
                self.add_book2(e)
        except Exception:
            pass

    def get_all(self):
        return super().get_all()

    def WriteAll(self):
        with open(self._file, "wb") as f:
            pickle.dump(super().get_all(), f)

    def add_book(self, title, author):
        BookRepo.add_book(self, title, author)
        self.WriteAll()

    def remove_book2(self, book):
        super().remove_book2( book)
        self.WriteAll()

    def update_Book(self, Book, name, author):
        BookRepo.update_books(self, Book, name, author)
        self.WriteAll()