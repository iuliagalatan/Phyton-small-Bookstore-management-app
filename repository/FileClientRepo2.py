from repository.ClientRepository import *
import os

class FileClientRepo2(ClientRepo):
    def __init__(self, fileName):
        ClientRepo.__init__(self)
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
            client = Client(l[0])
            ClientRepo.add_client2(self, client)
            line = f.readline().strip()
        f.close()

    def add_client2(self, client):
        f = open(self._file, "a")
        f.write(client.name )

    def add_client(self, name):
        f = open(self._file, "a")
        f.write(name + '\n')

    def WriteFile(self, lines):
        f = open(self._file, "a+")
        f.write(str(lines))



    def WriteAll(self):
        f = open(self._file, "w")
        line = f.readline().strip()
        while line != "":
            l = line.split(",")
            client = Client(l[0])
            line = str(client.name) + '\n'
            f.write(line)
            line = f.readline().strip()

        f.close()


    def remove_client2(self, client):
        with open("clients.txt", "r+") as f:
            d = f.readlines()
            f.seek(0)
            for line in d:
                if line.strip() != client.name:
                    f.write(line)
            f.truncate()
        f.close()


    def update_client(self, client, name):
        with open("clients.txt", "r+") as f:
            d = f.readlines()
            f.seek(0)
            for line in d:
                if line.strip() != client.name:
                    f.write(line)
                else:
                    print(name)
                    f.write(name + '\n')
            f.truncate()
        f.close()
