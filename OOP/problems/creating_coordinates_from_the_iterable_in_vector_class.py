# problem

"""
The Vector class of Section 2.3.3 provides a constructor that takes an integer d, and produces a d-dimensional vector with all coordinates equal to
0. Another convenient form for creating a new vector would be to send the
constructor a parameter that is some iterable type representing a sequence
of numbers, and to create a vector with dimension equal to the length of
that sequence and coordinates equal to the sequence values. For example,
Vector([4, 7, 5]) would produce a three-dimensional vector with coordinates <4, 7, 5>. Modify the constructor so that either of these forms is
acceptable; that is, if a single integer is sent, it produces a vector of that
dimension with all zeros, but if a sequence of numbers is provided, it produces a vector with coordinates based on that sequence.

"""




# code

# now our main task is to modify the constructor that if
# someone pass a single parameter so i will create list 
# with the length of the parameter of zeros
# and if someone pass a list so it will create a coordinates 
# from the list










class Vector:
    """represent a vector in multidimensional space"""

    def __init__(self, d):
        """ now we are creating d dimension vectors with zeros
        and if someone pass an iterable so it will create
        coordinates from it. 
        
        """
        if isinstance(d,int):
            self._coords = [0] * d
        
        elif isinstance(d, (list,tuple,set,)):
            self._coords = list(d)
        
        else:
            raise TypeError("parameter will be int or iterable")
        
    

    def __len__(self):
        """return the dimension of vector"""
        return len(self._coords)
    

    def __getitem__(self,j):
        """Returning jth element"""
        return self._coords[j]
    
    
    def __setitem__(self,j,val):
        """set jth coordinate of a vector to given value """
        self._coords[j] = val

    
    def __add__(self,other):
        """Return sum of the two vectors"""
        if len(self) != len(other):
            raise ValueError("Dimensions must agree")
        
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] + other[i]
        
        return result
    

    def __str__(self):
        """Producing string representation of a vector. """
        return "<" +  str(self._coords)[1:-1] + ">"
    

    def __eq__(self,other):
        """Return True if the coordinates of two vector are same"""
        return len(self._coords) ==  len(other._coords)
    
    def __ne__(self,other):
        """Return True if the coordinates of two vector are not same"""
        return not len(self._coords) == len(other._coords)
    


    # this is our main task adding the sub method for the vector'

    def __sub__(self,other):

        if len(self) != len(other):
            raise ValueError("Dimensions must agree.")
        
        result = Vector(len(self))
        
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        
        return result
    


    


    

    
    

vector = Vector(4)
vector1 = Vector([4,5,7,9])

print(vector)
print(vector1)