from repository.RentalRepository import *
import pickle

class BinaryRentalRepo(RentalRepo):
    def __init__(self, fileName):
        RentalRepo.__init__(self)
        
        self._file = fileName
        
        self.LoadFile()

    def LoadFile(self):
        try:
            f = open(self._file, "rb")
        except IOError:
            print("File not found! ")
        except EOFError :
            Repo_student._Rentals = []
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

    def add_rent2(self, Rental):
        RentalRepo.add_rent2(self, Rental)
        self.WriteAll()


    def remove_rent_2(self, Rental):
        RentalRepo.remove_rent_2(self, Rental)
        self.WriteAll()