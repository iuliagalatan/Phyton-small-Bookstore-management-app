import datetime
from tkinter import *

from controller.Controller import RentError, AddRentError
from tkinter import messagebox

class GUI():
    string = StringVar

    def __init__(self, ctrl):
        self._ctrl = ctrl

    def start(self):
        root = Tk()
        root.geometry('350x400')

        l = Label(root, text='Book library', relief = 'solid'  , width='20')
        l.pack(pady = 20)

        b = Button(root, text = 'Manage list of Clients', command = self.ClientMenu)
        b.pack(pady = 5)

        b = Button(root, text='Manage list of Books', command = self.BookMenu)
        b.pack(pady = 5)

        b = Button(root, text='Add/Return Rent', command=self.RentMenu)
        b.pack(pady = 5)

        b = Button(root, text='Search' ,command = self.Search)
        b.pack(pady = 5)

        b = Button(root, text='Statistics', command = self.Statistics)
        b.pack(pady = 5)

        b = Button(root, text='Undo', command=self.Undo)
        b.pack(pady = 5)
        b = Button(root, text='Redo', command=self.Redo)
        b.pack(pady = 5)
        root.mainloop()

    def ClientMenu(self):
        root2 = Tk()
        root2.geometry('300x300')

        l = Label(root2, text='Client Management', relief='solid', width='20')
        l.pack(pady = 20)

        b = Button(root2, text='Show Clients', command=self.ShowClients)
        b.pack(pady = 5)

        b = Button(root2, text='Add Client', command=self.AddClient)
        b.pack(pady = 5)

        b = Button(root2, text='Delete Client', command=self.DeleteClient)
        b.pack(pady = 5)

        b = Button(root2, text='Update Client', command = self.UpdateClient)
        b.pack(pady = 5)
        b.after(6000, root2.destroy)
        root2.mainloop()

    def BookMenu(self):
        root2 = Tk()
        root2.geometry('300x300')

        l = Label(root2, text='Books Management', relief='solid', width='20')
        l.pack(pady = 5)

        b = Button(root2, text='Show Books', command=self.ShowBooks)
        b.pack(pady = 5)

        b = Button(root2, text='Add Book', command=self.AddBook)
        b.pack(pady = 5)

        b = Button(root2, text='Delete Book', command=self.DeleteBook)
        b.pack(pady = 5)

        b = Button(root2, text='Update Book', command=self.UpdateBook)
        b.pack(pady = 5)

        b.after(6000, root2.destroy)
        root2.mainloop()



    def ShowClients(self):
        txt = "ID".ljust(15) + "Name".ljust(15) + "\n"
        for c in self._ctrl.clientrepo.clients:
            txt += str(c.id).ljust(15) + str(c.name).ljust(15) +"\n"
        messagebox.showinfo("List of Clients", txt)

    def ShowBooks(self):
        txt = "ID".ljust(15) + "Title".ljust(40) +"Author".ljust(15)+ "\n"
        for c in self._ctrl.bookrepo.books:
            txt += str(c.id).ljust(15) + str(c.title).ljust(40) + str(c.author).ljust(15)+ "\n"
        messagebox.showinfo("List of Books", txt)

    def AddClient(self):
        root3 = Tk()
        root3.geometry('300x300')

        l = Label(root3, text='Add Client', relief='solid', width='20')
        l.pack(pady = 5)

        labelname = Label(root3, text = 'Name: ', width='20')
        labelname.pack(pady = 5)

        self.entryname = Entry(root3, textvar = self.string )
        self.entryname.pack(pady = 5)

        b = Button(root3, text='Add Client', command=self.AddClient2)
        b.pack(pady = 5)
        b.after(6000, root3.destroy)
    def AddClient2(self):
        name = self.entryname.get()
        self._ctrl.add_client_repo(name)
        messagebox.showinfo("Info", "Added with succes")

    def AddBook(self):
        root3 = Tk()
        root3.geometry('300x300')

        l = Label(root3, text='Add Book', relief='solid', width='20')
        l.pack(pady = 5)

        labelname = Label(root3, text = 'Title: ', width='20')
        labelname.pack(pady = 5)

        self.entrytitle = Entry(root3, textvar = self.string )
        self.entrytitle.pack(pady = 5)

        labelauthor = Label(root3, text='Author: ', width='20')
        labelauthor.pack(pady = 5)

        self.entryauthor = Entry(root3, textvar=self.string)
        self.entryauthor.pack(pady = 5)

        b = Button(root3, text='Add Book', command=self.AddBook2)
        b.pack(pady = 5)
        b.after(6000, root3.destroy)

    def AddBook2(self):
        title = self.entrytitle.get()
        author = self.entryauthor.get()
        self._ctrl.bookrepo.add_book(title, author)
        messagebox.showinfo("Info", "Added with succes")

    def DeleteBook(self):
        root3 = Tk()
        root3.geometry('300x300')

        l = Label(root3, text='Remove Book', relief='solid', width='20')
        l.pack(pady = 5)

        labelname = Label(root3, text='Id: ', width='20')
        labelname.pack(pady = 5)

        self.entryidb = Entry(root3, textvar=self.string)
        self.entryidb.pack(pady = 5)
        b = Button(root3, text='Remove Book', command=self.DeleteBook2)
        b.pack(pady = 5)
        b.after(6000, root3.destroy)

    def DeleteBook2(self):
        id = self.entryidb.get()
        self._ctrl.remove_book_repo(id)
        messagebox.showinfo("Info", "Deleted with succes")

    def DeleteClient(self):
        root3 = Tk()
        root3.geometry('300x300')

        l = Label(root3, text='Remove Client', relief='solid', width='20')
        l.pack(pady = 5)

        labelname = Label(root3, text='Id: ', width='20')
        labelname.pack(pady = 5)

        self.entryidb = Entry(root3, textvar=self.string)
        self.entryidb.pack(pady = 5)
        b = Button(root3, text='Remove Client', command=self.DeleteClient2)
        b.pack(pady = 5)
        b.after(6000, root3.destroy)

    def DeleteClient2(self):
        id = self.entryidb.get()
        #self._repository.clientrepo.remove_client(id)
        self._ctrl.remove_client_repo(id)
        messagebox.showinfo("Info", "Deleted with succes")

    def UpdateBook(self):
        root3 = Tk()
        root3.geometry('300x300')

        l = Label(root3, text='Update Book', relief='solid', width='20')
        l.pack(pady = 5)

        labelid = Label(root3, text='Id: ', width='20')
        labelid.pack(pady = 5)

        self.entryid = Entry(root3, textvar=self.string)
        self.entryid.pack(pady = 5)

        labelname = Label(root3, text='New Title: ', width='20')
        labelname.pack(pady = 5)

        self.entrytitle = Entry(root3, textvar=self.string)
        self.entrytitle.pack(pady = 5)

        labelauthor = Label(root3, text='New Author: ', width='20')
        labelauthor.pack(pady = 5)

        self.entryauthor = Entry(root3, textvar=self.string)
        self.entryauthor.pack(pady = 5)

        b = Button(root3, text='Update Book', command=self.UpdateBook2)
        b.pack(pady = 5)
        b.after(6000, root3.destroy)

    def UpdateBook2(self):
        id = self.entryid.get()
        newtitle = self.entrytitle.get()
        newauthor = self.entryauthor.get()
        self._ctrl.update_book_repo(id, newtitle, newauthor)
        messagebox.showinfo("Info", "Updated with succes")

    def UpdateClient(self):
        root3 = Tk()
        root3.geometry('300x300')

        l = Label(root3, text='Update Client', relief='solid', width='20')
        l.pack(pady = 5)

        labelid = Label(root3, text='Id: ', width='20')
        labelid.pack(pady = 5)

        self.entryid = Entry(root3, textvar=self.string)
        self.entryid.pack(pady = 5)

        labelname = Label(root3, text='New Name: ', width='20')
        labelname.pack(pady = 5)

        self.entrynname= Entry(root3, textvar=self.string)
        self.entrynname.pack(pady = 5)

        b = Button(root3, text='Update Client', command=self.UpdateClient2)
        b.pack(pady = 5)
        b.after(6000, root3.destroy)

    def Undo(self):
        try:
            self._ctrl.undocontroller.Undo()
        except Exception as e:
            messagebox.showerror('error', e)

    def Redo(self):
        try:
            self._ctrl.undocontroller.Redo()
        except Exception as e:
            messagebox.showerror('error', e)

    def UpdateClient2(self):
        id = self.entryid.get()
        newname = self.entrynname.get()
        self._ctrl.update_client_repo(id, newname)
        messagebox.showinfo("Info", "Updated with succes")

    def Search(self):
        root2 = Tk()
        root2.geometry('300x300')

        l = Label(root2, text='Search', relief='solid', width='20')
        l.pack(pady = 5)

        b = Button(root2, text='Search for Clients', command=self.SearchClients)
        b.pack(pady = 5)

        b = Button(root2, text='Search for Books', command=self.SearchBooks)
        b.pack(pady = 5)
        b.after(6000, root2.destroy)

    def SearchClients(self):
        root3 = Tk()
        root3.geometry('300x300')
        labelname = Label(root3, text='Search for: ', width='20')
        labelname.pack(pady = 5)

        self.entrynname = Entry(root3, textvar=self.string)
        self.entrynname.pack(pady = 5)
        b = Button(root3, text='Search for Clients', command=self.SearchClients2)
        b.pack(pady = 5)
        b.after(6000, root3.destroy)

    def SearchClients2(self):
        name = self.entrynname.get()
        s = self._ctrl.search_client(name)
        if (len(s) != 0):
            txt = "ID".ljust(15) + "Name".ljust(15) + "\n"
            for c in s:
                txt += str(c.id).ljust(15) + str(c.name).ljust(15) + "\n"
            messagebox.showinfo("List of Clients", txt)

    def SearchBooks(self):
        root3 = Tk()
        root3.geometry('300x300')
        labelname = Label(root3, text='Search for: ', width='20')
        labelname.pack(pady = 5)

        self.entrynname = Entry(root3, textvar=self.string)
        self.entrynname.pack(pady = 5)
        b = Button(root3, text='Search for Books', command=self.SearchBooks2)
        b.pack(pady = 5)
        b.after(6000, root3.destroy)

    def SearchBooks2(self):
        name = self.entrynname.get()
        s = self._ctrl.search_book(name)
        if (len(s) != 0):
            txt = "ID".ljust(15) + "title".ljust(40) + "author".ljust(15) + "\n"
            for c in s:
                txt += str(c.id).ljust(15) + str(c.title).ljust(40) +  str(c.author).ljust(15)+ "\n"
            messagebox.showinfo("List of Books", txt)
    def RentMenu(self):
        root3 = Tk()
        root3.geometry('300x300')

        l = Label(root3, text='Add/Return Rent', relief='solid', width='20')
        l.pack(pady = 5)

        b = Button(root3, text='Add Rent', command=self.AddRent)
        b.pack(pady = 5)

        b = Button(root3, text='Return Rent', command=self.ReturnRent)
        b.pack(pady = 5)
        b.after(6000, root3.destroy)


    def PrintRent(self):
        s = self._ctrl.rentalrepo.rentals
        if (len(s) != 0):
            txt = "ID".ljust(15) + "ID-Book".ljust(15) + "ID-Client".ljust(15) + "Rent-Date".ljust(
                15) + "Return-Date".ljust(15) + "\n"
            for c in s:
                txt += str(c.id).ljust(15) + str(c.bookid).ljust(15) + str(c.clientid).ljust(15) + str(
                    c.rentdate).ljust(15) + str(c.returndate).ljust(15) + "\n"
            messagebox.showinfo("List of Rentals", txt)

    def ReturnRent(self):
        self.PrintRent()

        root3 = Tk()
        root3.geometry('300x300')

        l = Label(root3, text='Return Rent', relief='solid', width='20')
        l.pack(pady = 5)

        labelid = Label(root3, text='Rental Id: ', width='20')
        labelid.pack(pady = 5)

        self.entryid = Entry(root3, textvar=self.string)
        self.entryid.pack(pady = 5)

        labeldate= Label(root3, text='Return Date (YYYY-MM-DD): ', width='20')
        labeldate.pack(pady = 5)

        self.entrydate = Entry(root3, textvar=self.string)
        self.entrydate.pack(pady = 5)

        b = Button(root3, text='Add', command=self.ReturnRent2)
        b.pack(pady = 5)
        b.after(6000, root3.destroy)

    def ReturnRent2(self):
        error = ""
        rid = self.entryid.get()
        date = self.entrydate.get()
        try:
            self.Validatedate(date)
        except ValueError as e:
            error+=e
            messagebox.showerror("ERROR", error)
            return
        try:
            self._ctrl.return_rent(rid, date)
        except Exception as e:
            error+=e
            messagebox.showerror('Error', error)

        self.PrintRent()

    def Validatedate(self, date):
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorect date")

    def AddRent(self):
        self.PrintRent()

        root3 = Tk()
        root3.geometry('300x300')

        l = Label(root3, text='Add Rent', relief='solid', width='20')
        l.pack(pady = 5)

        labelcid = Label(root3, text='Client Id: ', width='20')
        labelcid.pack(pady = 5)

        self.entrycid = Entry(root3, textvar=self.string)
        self.entrycid.pack(pady = 5)

        labelbid = Label(root3, text='Book Id: ', width='20')
        labelbid.pack(pady = 5)

        self.entrybid = Entry(root3, textvar=self.string)
        self.entrybid.pack(pady = 5)

        labeldate = Label(root3, text='Rent Date(YYYY-MM-DD): ', width='20')
        labeldate.pack(pady = 5)

        self.entrydate = Entry(root3, textvar=self.string)
        self.entrydate.pack(pady = 5)

        b = Button(root3, text='Add', command=self.AddRent2)
        b.pack(pady = 5)
        b.after(6000, root3.destroy)

    def AddRent2(self):
        error = ""
        cid = self.entrycid.get()
        bid = self.entrybid.get()
        date = self.entrydate.get()
        try:
            self.Validatedate(date)
        except ValueError as e:
            error+=str(e)
            messagebox.showerror(error)
            return
        error = ''
        try:
            rentdate = datetime.datetime.strptime(date, '%Y-%m-%d')
            rentdate = rentdate.date()
            self._ctrl.add_rent_repo(bid, cid, rentdate)
        except AddRentError as e:
            error += str(e)
            messagebox.showerror("error", error)
            return
        self.PrintRent()
    def Statistics(self):
        root4= Tk()
        root4.geometry('300x300')

        l = Label(root4, text='Add/Return Rent', relief='solid', width='20')
        l.pack(pady = 5)

        b = Button(root4, text='Most Rented Books', command=self.MostRentedBooks)
        b.pack(pady = 5)

        b = Button(root4, text='Most Active Clients', command=self.MostActiveClients)
        b.pack(pady = 5)

        b = Button(root4, text='Most Rented Authors', command=self.MostRentedAuthors)
        b.pack(pady = 5)
        b.after(6000, root4.destroy)

    def MostRentedBooks(self):
        list = []
        list = self._ctrl.statisticsbooks()
        # self.Print(list)
        list2 = []
        list2 = self._ctrl.getbooksbyid(list)
        txt = "Author".ljust(30) + "Nr. of Rentals".ljust(15) + "\n"
        for l in list:
            txt += str(l[0]).ljust(40) + str(l[1]).ljust(20) + "\n"
        messagebox.showinfo("List of Most Rented Books", txt)

    def MostActiveClients(self):
        list = []
        list = self._ctrl.statisticsclients()

        for l in list:
            print(str(l[0]) + ' '+str(l[1]))

        txt = "ID".ljust(15) + "Client".ljust(15) + "\n"
        for l in list:
            txt += str(l[0]).ljust(15) + str(l[1]).ljust(15) + "\n"
        messagebox.showinfo("List of Most Active Clients", txt)

    def MostRentedAuthors(self):
        list = self._ctrl.statisticsauthors()
        txt = "Author".ljust(30) + "Nr. of Rentals".ljust(15) + "\n"
        for l in list:
            txt += str(l[0]).ljust(40) + str(l[1]).ljust(20) + "\n"
        messagebox.showinfo("List of Most Rented Authors", txt)

