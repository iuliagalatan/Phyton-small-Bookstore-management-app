from repository.ClientRepository import *

class FileClientRepo(ClientRepo):
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
        ClientRepo.add_client2(self, client)
        self.WriteAll()

    def add_client(self, name):
        c = Client(name)
        self.add_client2(c)


    def WriteAll(self):
        f = open(self._file, "w")
        clients = ClientRepo.get_all(self)
        for s in clients:
            line = str(s.name) + '\n'
            f.write(line)
        f.close()

    def remove_client2(self, client):
        ClientRepo.remove_client2(self, client)
        self.WriteAll()

    def update_client(self, client, name):
        ClientRepo.update_client(self, client, name)
        self.WriteAll()