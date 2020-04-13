import datetime
from controller.UndoController import *
from controller.Controller import *

class UI:
    def __init__(self, ctrl):
        self._ctrl = ctrl

    def PrintMenu(self):
        print("Hello! ")
        print("1. Manage list of clients")
        print("2. Manage list of books")
        print("3. Rent or return")
        print("4. Search")
        print("5. Create statistics")
        print("6. Undo")

    def Submenu(self):
        print("0. List")
        print("1. Add")
        print("2. Remove")
        print("3. Update")


    def Submenu2(self):
        print("0. Print")
        print("1. Rent")
        print("2. Return")


    def check_command(self, command):
        if ( command < '1' or command > '6'):
            raise ValueError("Wrong command")

    def Print(self, clas):
        for c in clas:
            print(c)

    def Printlist(self, list):
        for l in list:
            print(str(l[0]) + ' '+str(l[1]))

    def list(self, clas):
        self.Print(clas)



    def commandbasic(self, command):
        cmd  = input("enter command.. ")
        if ( cmd < '0' or cmd > '3'):
            print("wrong command!")
        else:
            cmd = int(cmd)
            if command == 1:
                if cmd == 0 :
                    print('*')
                    self.Print(self._ctrl.clientrepo.clients)
                if ( cmd == 1 ):
                    self.add_UI_client()
                if ( cmd == 2 ):
                    self.remove_UI_client()
                if ( cmd == 3 ):
                    self.update_UI_client()
            elif command == 2:
                if cmd == 0 :
                    print('0')
                    self.Print(self._ctrl.bookrepo.books)
                if (cmd == 1):
                    self.add_UI_books()
                if (cmd == 2):
                    self.remove_UI_books()
                if (cmd == 3):
                    self.update_UI_books()
            else:
                print("wrong command")


    def commandr(self, command):
        cmd = input('enter command:.. ')
        if cmd == '0':
            self.Print(self._ctrl.rentalrepo.rentals)
        if cmd == '1':
            self.rentUI()
        elif cmd == '2':
            self.returnUI()
        else:
            print('wrong command')
    def Validatedate(self, date):
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorect date")

    def Validaterent(self, bookid, rentdate):
        '''for b in self._ctrl.rentals:
            if b.bid == bookid:
                if(returndate == )
                '''
        pass

    def rentUI(self):
        print('Books:')
        self.Print(self._ctrl.bookrepo.books)
        print('Clients: ')
        self.Print(self._ctrl.clientrepo.clients)
        print('Rentals: ')
        self.Print(self._ctrl.rentalrepo.rentals)

        bookid = input('book id:.. ')
        clientid = input('client id:.. ')
        try:
            rentdate = input('rent date /yyyy-mm-dd/ : ')
            self.Validatedate(rentdate)
        except ValueError as e:
            print(e)
            return
        try:
            self.Validaterent(bookid, rentdate)
        except ValueError as e:
            print(e)
        try:
            rentdate = datetime.datetime.strptime(rentdate, '%Y-%m-%d')
            rentdate = rentdate.date()
            self._ctrl.add_rent_repo(bookid, clientid, rentdate)
        except AddRentError as e:
            print(e)
        self.Print(self._ctrl.rentalrepo.rentals)




    def returnUI(self):
        self.Print(self._ctrl.rentalrepo.rentals)
        rid = input('rental id: ')
        date = input('return date: ')
        try:
            self.Validatedate(date)
        except ValueError as e:
            print(e)
        try:
            self._ctrl.return_rent(rid, date)
            self.Print(self._ctrl.rentalrepo.rentals)
        except RentError as e:
            print(e)




    def command(self):
        command  = input("enter command.. ")
        try:
            self.check_command(command)
        except ValueError as e:
            print(e)
        command = int(command)
        if ( command == 1):
            self.Submenu()
            self.commandbasic(command)
        if ( command == 2):
            self.Submenu()
            self.commandbasic(command)
        if ( command == 3):
            self.Submenu2()
            self.commandr(command)
        if ( command == 4):
            self.search_ui()
        if ( command == 5):
            self.statistics_ui()
        if (command == 6):
            self.undo_ui()




    def start(self):
        while True:
            self.PrintMenu()
            c = self.command()

    def search_ui(self):
        print('search for: ')
        print('1.clients ')
        print('2.books ')
        cmd = input('enter command:.. ')
        if (cmd == '1'):
            string = input('searching for: ')
            s = self._ctrl.search_client(string)
            if ( len(s) != 0):
                self.Print(s)
            else:
                print('no results')
        if (cmd == '2'):
            string = input('searching for: ')
            s = self._ctrl.search_book(string)
            if( len(s)!= 0):
                self.Print(s)
            else:
                print('no results')


    def statistics_ui(self):
        print('1.Most rented books')
        print('2.Most active clients')
        print('3.Most rented author')
        print('4.Most rented books by date')
        cmd = input('enter command')
        if cmd == '1':
            list = []
            list = self._ctrl.statisticsbooks()
            # self.Print(list)
            list2 = []
            list2 = self._ctrl.getbooksbyid(list)
            self.Printlist(list2)

        elif cmd =='2':
            list = []
            list = self._ctrl.statisticsclients()
            self.Printlist(list)
        elif cmd =='3':
            list = []
            '''list = self._ctrl.statisticsbooks()
            list2 = self._ctrl.getbooksbyid2(list)'''
            list = self._ctrl.statisticsauthors()
            self.Printlist(list)
        elif cmd == '4':
            date = input('enter date: (YYYY-MM-DD) ')
            date = datetime.datetime.strptime(date, '%Y-%m-%d')
            date = date.date()

            list = []
            list = self._ctrl.statisticsbooks2(date)
            self.Printlist(list)
        else:
            print('wrong command')


    def undo_ui(self):
        print('1.undo')
        print('2.redo')
        cmd = input('1/2 : ')
        if int(cmd) == 1:
            try:
                self._ctrl.undocontroller.Undo()
            except Exception as e:
                print(e)
        elif int(cmd) == 2:
            try:
                self._ctrl.undocontroller.Redo()
            except Exception as e:
                print(e)
    def add_UI_client(self):

        name = input("Client name : ")
        self._ctrl.add_client_repo(name)

    def remove_UI_client(self):

        id = input('id client: ')
        self._ctrl.remove_client_repo(id)

    def update_UI_client(self):
        id = input('id client: ')
        name = input('new name: ')
        self._ctrl.update_client_repo(id, name)



    def add_UI_books(self):

        name = input("Book name")
        author = input("Book author")
        
        self._ctrl.add_book_repo(name, author)

    def remove_UI_books(self):
        id = input('id book: ')
        self._ctrl.remove_book_repo(id)

    def update_UI_books(self):
        id = input("id book: ")
        title = input("title book: ")
        author = input("author book: ")
        self._ctrl.update_book_repo(id, title, author)




