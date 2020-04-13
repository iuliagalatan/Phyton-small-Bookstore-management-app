from repository.ClientRepository import *
import pickle

class BinaryClientRepo(ClientRepo):
    def __init__(self, fileName):
        ClientRepo.__init__(self)
        
        self._file = fileName
        
        self.LoadFile()

    def LoadFile(self):
        try:
            f = open(self._file, "rb")
        except IOError:
            print("File not found! ")
        except EOFError :
            Repo_student._clients = []
        try:
            
            entities = pickle.load(f)
            for e in entities:
                self.add_client2(e)
        except Exception:
            pass

    def get_all(self):
        return super().get_all()

    def WriteAll(self):
        with open(self._file, "wb") as f:
            pickle.dump(super().get_all(), f)

    def add_client(self, name):
        c = Client(name)
        ClientRepo.add_client2(self, c)
        self.WriteAll()

    def add_client2(self, client):
        self._clients.append(client)
        self.WriteAll()

    def remove_client2(self, client):
        ClientRepo.remove_client2(self, client)
        self.WriteAll()

    def update_client(self, client, name):
        ClientRepo.update_client(self, client, name)
        self.WriteAll()