from domain.Client import *

class ClientRepo:
    def __init__(self):
        self._clients = []

    def initialiseclients(self):
        self.add_client('iulia')
        self.add_client('Cici')
        self.add_client('Didi')
        self.add_client('Coco')

    @property
    def clients(self):
        return self._clients

    def update_client(self, client, nname):
        '''
        updates the name of a given client
        :param id: id of client
        :param nname: new name
        :return: modifies list
        '''

        client.name = nname

    def add_client(self, name):
        '''
        adds a new client to the list of clients
        :param name: name of client
        :return:nothing, appends to the list
        '''
        c = Client(name)
        self._clients.append(c)

    def add_client2(self, client):
        self._clients.append(client)

    def remove_client(self, pos):
        '''
        Function for the remove operation. Removes after id
        :param id: client id which we want to filter
        :return: nothing, modifies self.clients[] list
        '''
        self._clients.remove(self._clients[pos])

    def remove_client2(self, client):
        self._clients.remove(client)

    def get_all(self):
        return self._clients


    def sort(self):
        self._clients.sort()