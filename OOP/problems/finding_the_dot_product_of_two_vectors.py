# problem

"""
Implement the mul method for the Vector class of Section 2.3.3, so
that the expression u v returns a scalar that represents the dot product of
the vectors, that is, ∑d
i=1 ui · vi.
"""



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
    


    # this is our main task adding the sub method for the vector'

    def __sub__(self,other):

        if len(self) != len(other):
            raise ValueError("Dimensions must agree.")
        
        result = Vector(len(self))
        
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        
        return result
    

    # now we are finding the dot product of two vectors
    # using the mul method

    def __mul__(self,other):

        if len(self) != len(other):
            raise ValueError("Dimension must agree.")
        
        result = 0
        for i in range(len(self)):
            result += int((self[i] * other[i]))
        return result



            
    


    


    

    
    

vector = Vector(4)
vector1 = Vector(4)
vector[0] = 100
vector[1] = 100
vector[2] = 100

vector1[0] = 1
vector1[1] = 2
vector1[2] = 3


print(vector * vector1)


