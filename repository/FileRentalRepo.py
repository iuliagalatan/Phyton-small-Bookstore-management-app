from repository.RentalRepository import *

class FileRentalRepo(RentalRepo):
    def __init__(self, fileName):
        RentalRepo.__init__(self)
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
            rental = Rental(l[0], l[1], l[2], l[3])
            RentalRepo.add_rent2(self, rental)
            line = f.readline().strip()
        f.close()

    def add_rent2(self, Rental):
        RentalRepo.add_rent2(self, Rental)
        self.WriteAll()


    def WriteAll(self):
        f = open(self._file, "w")
        Rentals = RentalRepo.get_all(self)
        for s in Rentals:
            line = str(s.bookid) + ',' + str(s.clientid) + ',' + str(s.rentdate) + ',' + str(s.returndate) + '\n'
            f.write(line)
        f.close()

    def remove_rent_2(self, Rental):
        RentalRepo.remove_rent_2(self,Rental)
        self.WriteAll()

    