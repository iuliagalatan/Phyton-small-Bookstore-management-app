import unittest
from iter_sort import *
     
class IterTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Obj1([50, 40, 30, 20, 10])
        self.iter = Iter(self.obj)
    
    def tearDown(self):
        self.obj = None
        self.iter = None    
    
    def test__next__(self):
        a = next(self.iter)
        self.assertEqual(a, 50, 'incorect value pointed by iterator')
        print(self.iter, end = ' ') # __iter__(), __next__()
    
    def test__iter__(self):
        a = iter(self.iter)
        self.assertEqual(a, self.iter, 'incorect value pointed by iterator')
        print(self.iter, end = ' ') # __iter__(), __next__()
              
    def test__setitem__getitem__(self):
        self.iter[0] = 6          #__setitem__()
        self.assertEqual(self.iter[0], 6, '__setitem__ not working; incorrect value') #__getitem__()
    
    def test__iadd__(self):
        self.iter = Iter([10, 20])

        self.iter += [500, 600]
      #  self.iter += it      
        self.assertEqual(self.iter.lst, [10, 20, [500, 600]], 'incorrect values') 
        it = Iter([700, 800])
        self.iter += it;
        self.assertEqual(self.iter.lst, [10, 20, [500, 600], [700, 800]], 'incorrect values') 
           
    def test__delitem__(self):
        print()
        for x in self.iter:
            print(x, end = ' ')
        print()
        
        del self.iter[1]          #  __del__()           
        self.assertEqual(len(self.iter), 4, 'delete not working')
        for x in self.iter:       # __iter__(), __next__()
            print(x, end = ' ')   # __getitem__()
        print()

class LessTestCase(unittest.TestCase):
    
    def test_less_numeric(self):
        a, b = 10, 20
        self.assertTrue(less(a, b)) 

    def test_less_objects(self):
        a, b = Obj2(10), Obj2(20)
        self.assertTrue(less(a, b))   

class GreaterTestCase(unittest.TestCase):
    
    def test_greater_numeric(self):
        a, b = 10, 20
        self.assertFalse(greater(a, b)) 

    def test_greater_objects(self):
        a, b = Obj2(10), Obj2(20)
        self.assertFalse(greater(a, b))
        
class AcceptTestCase(unittest.TestCase):
    
    def test_accept_less_numeric(self):
        a, b = 10, 30 
        self.assertTrue(accept_less(a, b)) 

    def test_accept_less_equal_numeric(self):
        a, b = 30, 30 
        self.assertTrue(accept_less_equal(a, b)) 

    def test_accept_greater_numeric(self):
        a, b = 60, 50 
        self.assertTrue(accept_greater(a, b)) 

    def test_accept_greater_equal_numeric(self):
        a, b = 50, 50 
        self.assertTrue(accept_greater_equal(a, b)) 
    
    def test_accept_equal_numeric(self):
        a, b = 50, 50 
        self.assertTrue(accept_equal(a, b)) 
    
    def test_accept_greater_objects(self):
        a, b = Obj2(40), Obj2(30)
        self.assertTrue(accept_greater(a, b))  
        
    def test_accept_greater_equal_objects(self):
        a, b = Obj2(30), Obj2(30)
        self.assertTrue(accept_greater_equal(a, b))  
        
    def test_accept_less_objects(self):
        a, b = Obj2(10), Obj2(30)
        self.assertTrue(accept_less(a, b))  
     
    def test_accept_less_equal_objects(self):
        a, b = Obj2(30), Obj2(30)
        self.assertTrue(accept_less_equal(a, b))  
        a, b = Obj2(20), Obj2(30)
        self.assertTrue(accept_less_equal(a, b))  
        
class FilterTestCase(unittest.TestCase):
    def setUp(self):
        self.List = [12, -23, 34, -34, 43, -23, 0]
    
    def tearDown(self):
        self.List = None    
    
    def test_filter_numeric(self):
        self.List = Filter(self.List, accept_greater, 13)
        self.assertTrue(self.List == [34, 43]) 
        print(self.List, end = ' ')
        
    def test_filter_objects(self):
        self.List = [Obj2(10), Obj2(20), Obj2(30), Obj2(40)]
        self.List = Filter(self.List, accept_greater_equal, Obj2(30))
        self.assertTrue(self.List == [Obj2(30), Obj2(40)]) 
      
class SortTestCase(unittest.TestCase):
               
    def test_sort_list_less(self):
        List = [12, 8, 3, 20, 11]
        sort(List)
        self.assertEqual(List, [3, 8, 11, 12, 20])
        sort(List, less)
        self.assertEqual(List, [3, 8, 11, 12, 20])
    
    def test_sort_list_greater(self):
        List = [12, 8, 3, 20, 11]
        sort(List, greater)
        self.assertEqual(List, [20, 12, 11, 8, 3])
        
    def test_sort_iterable_object(self):
        List = [50, 40, 30, 20, 10]
        obj = Obj1(List)    
        obj = Iter(obj)   # obj - become iterable object
        sort(obj)
        self.assertEqual(obj, [10, 20, 30, 40, 50])
        print(obj, end = ' ')
        print(List, end = ' ')
        
    def test_sort_object_list(self):
        
        List = [Obj2(5), Obj2(4), Obj2(3), Obj2(2), Obj2(1)]        
        #List = Iter(List)  #not really needed here - a list is already iterable
        sort(List, less)
        self.assertEqual(List, [Obj2(1), Obj2(2), Obj2(3), Obj2(4), Obj2(5)])
        print()
        for val in List:
            print(val, end = ' ')
        print()
        sort(List, greater)
        self.assertEqual(List, [Obj2(5), Obj2(4), Obj2(3), Obj2(2), Obj2(1)])
        for val in List:
            print(val, end = ' ')
        print()
       

'''
    Obj1 and Obj2 are pure fabrication classes for testing purposes
'''
class Obj1:
    def __init__(self, List):
        self._L = List
        
    @property
    def lst(self):
        return self._L
        
    def __str__(self):
        return str(self._L)

class Obj2:
    def __init__(self, val):
        self._value = val
        
    @property
    def value(self):
        return self._value
        
    @value.setter
    def value(self, val):
        self._value = val
        
    #mandatory, needed for comparison
    def __lt__(self, obj):
        return self._value < obj._value
        
    def __eq__(self, obj):
        return  self._value == obj._value     
        
    def __str__(self):
        return str(self._value)
        

          
if __name__ == '__main__':
    unittest.main(verbosity = 2)
