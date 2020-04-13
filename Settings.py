import controller
from controller.Controller import Controller
from ui.console import UI
from ui.gui import GUI
from domain.Client import Client
from domain.Book import Book
from domain.Rental import Rental
from repository.BookRepository import *
from repository.ClientRepository import *
from repository.RentalRepository import *
from repository.FileBookRepo import *
from repository.FileClientRepo2 import *
from repository.FileClientRepo import *
from repository.FileRentalRepo import *
from controller.UndoController import *
from repository.BinaryClientRepo import *
from repository.BinaryBookRepo import *
from repository.BinaryRentalRepo import *

class Settings:
    def __init__(self, configFile):
        self.__config_file = configFile
        self.__settings = {}



    def readSettings(self):
        with open(self.__config_file, "r") as f:
            lines = f.read().split("\n")
            settings = {}
            for line in lines:
                setting = line.split("=")
                if len(setting) > 1:
                    self.__settings[setting[0].strip()] = setting[1].strip()

    def config(self):
        self.readSettings()
        clientRepo = None
        bookRepo = None
        rentalRepo = None
        if self.__settings['repository'] == "in-memory":
            clientRepo = ClientRepo()
            bookRepo = BookRepo()
            rentalRepo = RentalRepo()
            
            clientRepo.initialiseclients()
            bookRepo.initialisebooks()
            rentalRepo.initialiserentals()
            
            
        if self.__settings['repository'] == "text-file":
            clientRepo = FileClientRepo2(self.__settings["clients"])
            bookRepo = FileBookRepo(self.__settings["books"])
            rentalRepo = FileRentalRepo(self.__settings["rentals"])

        if self.__settings['repository'] == "binary":
            clientRepo = BinaryClientRepo(self.__settings["clients"])
            bookRepo = BinaryBookRepo(self.__settings["books"])
            rentalRepo = BinaryRentalRepo(self.__settings["rentals"])



        undo = UndoController()
        ctrl = Controller(bookRepo, clientRepo, rentalRepo, undo)
        ui = None
        if self.__settings['ui'] == "console":
            ui = UI(ctrl)
            
        if self.__settings['ui'] == 'gui':
            ui = GUI(ctrl)
        
        return ui