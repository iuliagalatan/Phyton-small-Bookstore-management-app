import itertools

class Rental:
    cnt = itertools.count(1)
    def __lt__(self, other):
        if (self._id<  other._id):
            return self
    def __init__(self, bookid, clientid, rentdate, returneddate):
        self._id = next(self.cnt)
        self._bookid = bookid.rstrip()
        self._clientid = clientid.rstrip()
        self._rentdate = rentdate
        self._returndate = returneddate
    @property
    def id(self):
        return self._id

    @property
    def bookid(self):
        return self._bookid

    @property
    def clientid(self):
        return self._clientid

    @property
    def rentdate(self):
        return self._rentdate

    @property
    def returndate(self):
        return self._returndate

    @returndate.setter
    def returndate(self, value):
        self._returndate = value

    def __str__(self):
        if (str(self._returndate) == '0001-01-01' ):
            return str(self.id) + '. Client: ' + str(self.clientid) + ' Book: ' + str(
                self.bookid) + ' rentdate: ' + str(self.rentdate) +  ' return date: None'
        return str(self.id) + '. Client: ' + str(self.clientid) + ' Book: ' + str(self.bookid) + ' rentdate: ' + str(self.rentdate) + ' return date: ' + str(self.returndate)
