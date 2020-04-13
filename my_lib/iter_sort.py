   
        
class Iter:
    '''
        Iter defines an iterable type
        Iter class provide the features af an iterable
        for any other class C witch expose @property lst returning a containing list,
        or for a list provided as an argument to the __init__() method
    '''
    def __init__(self, other = []):
        self._iterPoz = 0
        if isinstance(other, list):
            self._lst = other
        else:
            self._lst = other.lst
        
    def __setitem__(self, index, value):
        self._lst[index] = value

    def __getitem__(self, index):
        return self._lst[index]
    
    def __delitem__(self, index):
        del self._lst[index]
    
    def __iadd__(self, other): 
        '''
        pt +=
        Add a new list contained in other to the Iter list (self._lst
        '''
        if isinstance(other, list):
            self._lst.append(other)
        else:
            self._lst.append(other.lst)  
        return self
        
    def __iter__(self):
        '''
        Return an iterator object
        '''
        self._iterPoz = 0
        return self   
    
    def __next__(self):
        '''
        Return the next element in the iteration
        raise StopIteration exception if we are at the end
        '''
        if (self._iterPoz >= len(self._lst)):
            raise StopIteration()
        elem = self._lst[self._iterPoz]
        self._iterPoz += 1
        return elem
        
    @property
    def lst(self):
        return self._lst
        
    # operator de insertie
    def __str__(self):
        return str(self._lst)
    
    def __len__(self):
        return len(self._lst)
    
    def __eq__(self, obj):
        if isinstance(obj, list):
            return self._lst == obj
        return self._lst == obj.lst

   
def accept_less(x, val):
    '''
    This accept function return True if value of parameter x is smaller
    then the value of parameter val
    '''
    if x < val:
        return True
    else:
        return False

def accept_equal(x, val):
    '''
    This accept function return True if value of parameter x is equal to
    the  value of parameter val
    '''
    if x == val:
        return True
    else:
        return False
def accept_not_equal(x, val):
    '''
    This accept function return True if value of parameter x is equal to
    the  value of parameter val
    '''
    if not (x == val):
        return True
    else:
        return False
        
def accept_less_equal(x, val):
    '''
    This accept function return True if value of parameter x is smaller or equal
    then the value of parameter val
    '''
    if val < x:
        return False
    else:
        return True


def accept_greater(x, val):
    '''
    This accept function return True if value of parameter x is greater
    then the value of parameter val
    '''
    if val < x:
        return True
    else:
        return False

def accept_greater_equal(x, val):
    '''
    This accept function return True if value of parameter x is greater or equal
    then the value of parameter val
    '''
    if x < val:
        return False
    else:
        return True


def accept_unique(x, used):
    '''
    This accept function return True if x is not in list "used"
    and False otherwise 
    If it returns True, the value of x will be appended to the "used" list
    '''
    
    if x in used: return False
    used.append(x)
    return True

def Filter(List, accept, val = None):
    '''
    The method extract from parameter List a new list filtered with the accept method    
    ''' 
    List = [x for x in List if accept(x, val) ]
    return List
    
def less(obj1, obj2):
    '''
    Comparison function (operation < ) to determine the order between two elements.
    Will be used by sort function
    '''
    return obj1 < obj2

def greater(obj1, obj2):
    '''
    Comparison function (operation > ) to determine the order between two elements.
    Will be used by sort function
    '''
    if obj1 < obj2:
        return False
    return True
    
def sort(List, compare = None):
    '''
    Selection sort function
    Receive a list and a comparison function less in order to determine
    the order between two elements
    '''
    # The value of i corresponds to how many values were sorted
    for i in range(len(List)):
        # We assume that the first item of the unsorted segment is the smallest
        i_min = i
        # This loop iterates over the unsorted items
        for j in range(i + 1, len(List)):
            if (compare == None):
                if List[j] < List[i_min]:
                    i_min = j
            else:
                if compare(List[j], List[i_min]):
                    i_min = j
        # Swap values of the lowest unsorted element with the first unsorted element
        List[i], List[i_min] = List[i_min], List[i]


'''
L = [12, 8, 3, 20, 11]
sort(L)
print(L)
sort(L, less)
print(L)

'''

'''
obj = Obj([59, 39, 23, 10, 49])
it = Iterator(obj)
sort(it, less)
print(it)
print(obj)

obj = Obj([590, 390, 230, 100, 490])
it = Iterator(obj)
sort(it)
print(it)
print(obj)


obj = Obj([10, 23])
it = Iterator(obj)
for x in it:
    print(x, end = ' ')

print()
del it[0]
for x in it:
    print(x, end = ' ')
print()
print(obj)

it[0] = 19876
print(obj)
print(it)
'''
'''
obj = Obj([10, 23, 39, 49, 59])
it = Iterator(obj)
for x in it:
    print(x, end = ' ')

print()
del it[0]
for x in it:
    print(x, end = ' ')
print()
print(obj)

it[0] = 19876
print(obj)
print(it)
'''
