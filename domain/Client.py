import itertools

class Client:
    cnt = itertools.count(1)
    def __init__(self, name):
        self._id = next(self.cnt)
        self._name = name

    def __str__(self):
        return str(self._id) +'. '+str(self._name)

    def __lt__(self, other):
        if (self._id<  other._id):
            return self

    @property
    def id(self):
        return self._id
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
