import itertools

class Book:
    cnt = itertools.count(1)
    def __init__(self,  title, author):
        self._id = next(self.cnt)
        self._title = title
        self._author = author

    def __str__(self):
        return str(self._id) + '. ' + str(self._title) + ' ' + str(self._author)

    def __contains__(self, _title):
        return _title.lower() in (n.lower() for n in self._title)

    def __lt__(self, other):
        if (self._id<  other._id):
            return self

    @property
    def id(self):
        return self._id
    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author
    @id.setter
    def id(self, value):
        self._id = value

    @title.setter
    def title(self, value):
        self._title = value

    @author.setter
    def author(self, value):
        self._author = value






#testing->>
def test():
    b = Book(1, 'iulia', 'mami')
    print(b)
