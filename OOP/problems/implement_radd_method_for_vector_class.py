#problem


"""
In Section 2.3.3, we note that our Vector class supports a syntax such as
v = u + [5, 3, 10, −2, 1], in which the sum of a vector and list returns
a new vector. However, the syntax v = [5, 3, 10, −2, 1] + u is illegal.
Explain how the Vector class definition can be revised so that this syntax
generates a new vector.

"""


# code


class Vector:
    """represent a vector in multidimensional space"""

    def __init__(self, d):
        """ now we are creating d dimension vectors with zeros"""
        self._coords = [0] * d
    

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
    


  

    def __sub__(self,other):

        if len(self) != len(other):
            raise ValueError("Dimensions must agree.")
        
        result = Vector(len(self))
        
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        
        return result
    


    # our main task is define a method which support
    # this addition  [1,3,4,5] + vector
    # for this we will implement the radd method


    def __radd__(self,other):

        if len(self) != len(other):
            raise ValueError("dimensions must agree.")
        
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] + other[i]
        return result
    


    # now our another task is to implement the mul method
    # to return the coordinates the given times
    # for example vector = [1,2,3,4] * 3 so [3 , 6, 9,12]


    def __mul__(self,other):
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] * other
        
        return result
    
    # now we are creating the method which support rmul
    # for example 3 * vector


    def __rmul__(self,other):
        return self.__mul__(other)

        
    
    


    


    

    
    

vector = Vector(4)
vector1 = Vector(4)
vector[0] = 100
vector[1] = 200
vector[2] = 300
vector[3] = 400


print(vector * 3)
print(4 * vector)