from repository.BookRepository import BookRepo
from repository.ClientRepository import ClientRepo
from repository.RentalRepository import RentalRepo
from domain.Client import *
from domain.Book import *
from domain.Rental import *
from controller.UndoController import *
import datetime


def sortFirst(list):
    return list[0]

def sortSecond(list):
    return list[1]

class Controller:
    def __init__(self, br, cr, rr, undo):
        self._book_repo = br
        self._client_repo = cr
        self._rental_repo = rr
        self._undo_controller = undo

    @property
    def bookrepo(self):
        return self._book_repo

    @property
    def undocontroller(self):
        return self._undo_controller

    @property
    def clientrepo(self):
        return self._client_repo

    @property
    def rentalrepo(self):
        return self._rental_repo
    def remove_client_repo(self, id):
        i = 0
        print('id de sters este:'+str(id))
        cid = -1
        l = len(self._client_repo.clients)
        index = 0
        cascade=[]
        for i in range(len(self._client_repo.clients)):
            if str(self._client_repo.clients[i].id) == str(id):
                index = i
                cid = self._client_repo.clients[i]

        if cid != -1:
            name = cid.name
            id = cid.id
            print(index)
            self._client_repo.remove_client2(cid)

            redo = FunctionCall(self.clientrepo.remove_client2, cid)
            undo = FunctionCall(self.add_client_repo2, cid)
            operation1 = Operation(undo, redo)
            cascade.append(operation1)

            '''
            for removing in cascade- also rentals of that client
            '''
            remove_rentals = []
            add_rentals = []
            pos = 0
            for r in self.rentalrepo.rentals:
                if str(r.clientid) == str(id):
                    remove_rentals.append(r)

                    '''
                    might be a problem for returndate
                    '''
                    add_rentals.append(r)

                    self.remove_rent_repo(pos)
                    print(r)
                pos=pos+1

            undo = FunctionCall(self.add_rentals_back, add_rentals)
            redo = FunctionCall(self.remove_all_rentals, remove_rentals)
            op = Operation(undo, redo)
            cascade.append(op)
            self._undo_controller.recordOperation(CascadedOperation(cascade))

    def add_rentals_back(self, rentals):
        for i in rentals:
            self.rentalrepo.add_rent2(i)

    def remove_all_rentals(self, rentals):
        for i in rentals:
            self._rental_repo.remove_rent_2(i)

    def add_book_repo2(self, book):
        self._book_repo.add_book2(book)
        self.bookrepo.books.sort()
        redo = FunctionCall(self.add_book_repo2, book)
        name = book.title
        id = self.get_book_by_name(name).id
        undo = FunctionCall(self.remove_book_repo, id)
        operation = Operation(undo, redo)
        self._undo_controller.recordOperation(operation)

    def add_rent_repo2(self, rental):
        self._rental_repo.add_rent2(rental)
        self.rentalrepo.rentals.sort()
        pos = self.search_rental(rental)
        undo = FunctionCall(self.remove_rent_repo, pos)
        redo = FunctionCall(self.add_rent_repo2, rental)
        operation = Operation(undo, redo)
        self.undocontroller.recordOperation(operation)

    def search_rental(self, rental):
        pos = 0
        for r in self.rentalrepo.rentals:
            if str(r.id) == str(rental.id):
                return pos
            pos = pos+1

    def add_client_repo2(self, client):
        self._client_repo.add_client2(client)
        self.clientrepo.clients.sort()
        redo = FunctionCall(self.add_client_repo2, client)
        name  = client.name
        pos = self.get_pos(name)
        cl = self.get_client_by_name(name)
        id = cl.id
        undo = FunctionCall(self.remove_client_repo, id)

        cascade = []
        operation = Operation(undo, redo)
        cascade.append(operation)
        self._undo_controller.recordOperation(CascadedOperation(cascade))

    def remove_book_repo(self, id):
        i = 0
        bid = -1
        index = 0
        l = len(self._book_repo.books)
        for b in self._book_repo.books:
            if bid == -1:
                index = index+1
            if str(b.id) == str(id):
                bid = b
           
        if bid != -1:

            id = bid.id
            name  = bid.title
            author = bid.author
            self._book_repo.remove_book2(bid)
            redo = FunctionCall(self.bookrepo.remove_book2,  bid)
            undo = FunctionCall(self.add_book_repo2, bid)
            cascade = []
            operation = Operation(undo, redo)
            cascade.append(operation)

            remove_rentals = []
            add_rentals = []
            pos = 0
            for r in self.rentalrepo.rentals:
                if str(r.clientid) == str(id):
                    remove_rentals.append(r)
                    add_rentals.append(r)
                    self.remove_rent_repo(pos)
                    print(r)
                pos = pos + 1

            undo = FunctionCall(self.add_rentals_back, add_rentals)
            redo = FunctionCall(self.remove_all_rentals, remove_rentals)
            op = Operation(undo, redo)
            cascade.append(op)
            self._undo_controller.recordOperation(CascadedOperation(cascade))

    def update_book_repo(self, id, name, author):
        book = 0
        for b in self._book_repo.books:
            if str(b.id) == str(id):
                book = b
                oldtitle = book.title
                oldauthor = book.author
        if book != 0:
            undo = FunctionCall(self.update_book_repo, id, oldtitle, oldauthor)
            redo = FunctionCall(self.update_book_repo, id, name, author)
            cascade = []
            operation = Operation(undo, redo)
            cascade.append(operation)
            self._undo_controller.recordOperation(CascadedOperation(cascade))
            self._book_repo.update_books(book, name, author)

    def update_client_repo(self, id, name):
        client  =0
        for c in self.clientrepo.clients:
            if str(c.id) == str(id):
                client = c
                oldname = c.name
        if client != 0:
            self._client_repo.update_client(client, name)
            undo = FunctionCall(self.update_client_repo, id, oldname)
            redo = FunctionCall(self.update_client_repo, id, name)
            cascade = []
            operation = Operation(undo, redo)
            cascade.append(operation)
            self._undo_controller.recordOperation(CascadedOperation(cascade))


    def add_book_repo(self, name, author):
        self._book_repo.add_book(name, author)
        redo = FunctionCall(self.add_book_repo, name, author)
        id = self.get_book_by_name(name).id
        undo = FunctionCall(self.remove_book_repo, id)
        cascade = []
        operation = Operation(undo, redo)
        cascade.append(operation)
        self._undo_controller.recordOperation(CascadedOperation(cascade))


    def add_client_repo(self, name):
        cnt = self.search(name)
        if cnt == 0:
            pass
        else:
            cnt = cnt + 1
        if cnt != 0:
            name = str(name) + str(cnt)

        self._client_repo.add_client(name)
        '''
        client = self._client_repo.clients[-1]
        redo = FunctionCall(self.add_client_repo2, client)
        pos = self.get_pos(name)
        cl = self.get_client_by_name(name)
        id = cl.id
        undo = FunctionCall(self.remove_client_repo, id)
        cascade = []
        operation = Operation(undo, redo)
        cascade.append(operation)
        self._undo_controller.recordOperation(CascadedOperation(cascade))
        '''
        #print(self.undocontroller)

    def get_pos(self, name):
        l = len(self._client_repo.clients)
        for i in range(l):
            if str(self._client_repo.clients[i].name) == str(name):
                print(i)
                return i

    def get_client_by_name(self, name):

        for b in self._client_repo.clients:
            if b.name == name:
                return b


    def get_book_by_name(self, name):
        for b in self._book_repo.books:
            if b.title == name:
                return b


    def search_booksinrental_repo(self, bid):
        cnt = 0
        for r in self._rental_repo.rentals:
            if str(bid) == str(r.id):
                cnt = cnt+1
        return cnt

    def statisticsauthors(self):
        list = []
        for a in self._book_repo.books:
            if a.author not in list:
                list.append(a.author)

        l = []

        for a in list:
            l.append([a, 0])
        for r in self._rental_repo.rentals:
            id = r.bookid
            for b in self._book_repo.books:
                if str(id) == str(b.id):
                    for i in l:
                        if str(i[0]) == str(b.author):
                            i[1] = i[1]+1
        l.sort(key=sortSecond, reverse=True)
        return l

    def Days(self, date1, date2):
        '''
        diference in days between 2 dates
        :param date1: first date- type:date
        :param date2: second date - type:date
        :return: date2-date1
        '''
        date1 = str(date1)
        date2 = str(date2)
        date1 = datetime.datetime.strptime(date1, '%Y-%m-%d')
        date2 = datetime.datetime.strptime(date2, '%Y-%m-%d')
        delta = date1-date2
        return delta.days

    def statisticsclients(self):
        list = []
        for c in self._client_repo.clients:
            list.append([c.name, 0, c.id])
        zero = '0001-01-01'
        for r in self._rental_repo.rentals:
            if str(r.returndate) != str(zero):
                id = r.clientid
                for l in list:
                    if str(id) == str(l[2]):
                        l[1] += self.Days(r.returndate, r.rentdate)
        list.sort(key=sortSecond, reverse=True)
        return list


    def statisticsbooks(self):
        list = []
        cnt = 0
        for b in self._book_repo.books:
            cnt = self.search_booksinrental_repo(b.id)
            list.append([cnt, b.id])
        list.sort(key = sortFirst, reverse = True)
        return list

    def statisticsbooks2(self, date):
        list = []
        for b in self._book_repo.books:
            list.append([b.title, 0, b.id])
        for r in self._rental_repo.rentals:
            for l in list:
                if str(l[2]) == str(r.bookid):
                    if r.rentdate == date:
                        l[1] = l[1]+1
        list.sort(key=sortSecond, reverse=True)
        return list


    def search_book_by_id(self, id):
        for b in self._book_repo.books:
            if str(b.id) == str(id):
                return b.title, b.author

    def getbooksbyid(self, list):
        list2 = []
        for elem in list:
            id = elem[1]
            name, author = self.search_book_by_id(id)
            list2.append([name,author,  elem[0]])
        return list2

    def getbooksbyid2(self, list):
        list2 = []
        for elem in list:
            id = elem[1]
            name, author = self.search_book_by_id(id)
            list2.append([author, elem[0]])
        return list2


    def search_client(self, string):
        c = []
        for b in self._client_repo.clients:
            if string.lower() in b.name.lower():
                c.append(b)
            if string in str(b.id):
                c.append(b)
        return c

    def search_book(self, string):
        c = []
        for b in self._book_repo.books:
            if string.lower() in b.title.lower():
                c.append(b)
            if string.lower() in b.author.lower():
                c.append(b)
            if string in str(b.id):
                c.append(b)
        return c

    def add_rent_repo(self, bookid, clientid, rentdate):
        zero = datetime.date(1, 1, 1)
        ok = True
        for b in self._rental_repo.rentals:
            if (str(b.bookid) == str(bookid)):
                if rentdate >= b.rentdate and b.returndate == zero:
                    ok = False
                    raise AddRentError('Book not avaliable')

                elif str(rentdate) > str(b.returndate):
                    ok = True
        if ok:
            self._rental_repo.add_rent(bookid, clientid, rentdate)
            '''aici nu caut cu for... posible problem'''
            pos = len(self._rental_repo.rentals) - 1
            undo = FunctionCall(self.remove_rent_repo, pos)
            redo = FunctionCall(self.add_rent_repo, bookid, clientid, rentdate)
            cascade = []
            operation = Operation(undo, redo)
            cascade.append(operation)
            self.undocontroller.recordOperation(CascadedOperation(cascade))

    def remove_rent_repo(self, pos):
        self._rental_repo.remove_rent(pos)
        print('removed pos'  + str(pos))



    def return_rent(self, id, date):
        zero = datetime.date(1, 1, 1)

        date = datetime.datetime.strptime(date, '%Y-%m-%d')
        date = date.date()
        ok = False
        for b in self._rental_repo.rentals:
            if str(date) == str(zero) and str(b.id) == str(id):
                b.returndate = zero
            elif str(b.id) == str(id) and str(date) >= str(b.rentdate) and b.returndate == zero:
                b.returndate = date
                ok = True
            elif str(b.id) == str(id) and str(date) < str(b.rentdate) and str(date) != str(zero):
                raise RentError('return date should be bigger than rent date')
        if ok:
            undo = FunctionCall(self.return_rent, id, '0001-01-01')
            redo = FunctionCall(self.return_rent, id, date)
            cascade = []
            operation = Operation(undo, redo)
            cascade.append(operation)
            self.undocontroller.recordOperation(CascadedOperation(cascade))


    def search(self, name):
        cnt = 0

        for c in self._client_repo.clients:
            no_digits = ''.join([i for i in c.name if not i.isdigit()])

            if no_digits == str(name):
                cnt = cnt+1
        return cnt



class RentError(Exception):
    def __init__(self, message):
        super().__init__(message)

class AddRentError(Exception):
    def __init__(self, message):
        super().__init__(message)



'''def test_add_client():
    r = repository()
    assert len(r.clients) == 0
    r.add_client2('Gigi')
    assert len(r.clients) == 1
    r.add_client2('Gigi')
    #print(r.clients[0].name)
    #print(r.clients[1].name)
    assert r.clients[1].name =='Gigi2'
    client.cnt = itertools.count(1)
*/

//test_add_client()

'''