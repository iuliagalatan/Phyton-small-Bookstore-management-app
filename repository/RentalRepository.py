from domain.Rental import *
import datetime

class RentalRepo:
    def __init__(self):
        self._rentals = []

    @property
    def rentals(self):
        return self._rentals

    def initialiserentals(self):
        r = Rental(1, 1, datetime.date(2019,7,2), datetime.date(1, 1, 1))
        self._rentals.append(r)
        r = Rental(3, 2, datetime.date(2019,10,15), datetime.date(1, 1, 1))
        self._rentals.append(r)
        r = Rental(4, 4, datetime.date(2019,12,2), datetime.date(1, 1, 1))
        self._rentals.append(r)

    def add_rent(self, bookid, clientid, rentdate):
        '''
        adds a rent to rentals list
        :param bookid: book id
        :param clientid: client id
        :param rentdate: rent date
        :return: append to the list of rentals
        '''


        r = Rental(bookid, clientid, rentdate, datetime.date(1,1,1))
        self._rentals.append(r)

    def add_rent2(self, rent):
        self._rentals.append(rent)

    def remove_rent(self, pos):
        self._rentals.remove(self._rentals[pos])

    def get_all(self):
        return self._rentals

    def remove_rent_2(self, rent):
        self._rentals.remove(rent)
    def sort(self):
        self._rentals.sort()