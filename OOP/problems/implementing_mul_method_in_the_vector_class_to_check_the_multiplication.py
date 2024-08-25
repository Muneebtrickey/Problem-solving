# problem

"""
Exercise R-2.12 uses the mul method to support multiplying a Vector
by a number, while Exercise R-2.14 uses the mul method to support
computing a dot product of two vectors. Give a single implementation of
Vector. mul that uses run-time type checking to support both syntaxes
u v and u k, where u and v designate vector instances and k represents
a number.
"""


# code of the vector class


class Vector:
    def __init__(self,d):
        """create a vector with d-dimensions"""
        self.d = [0]*d
    
    def __len__(self):
        return len(self.d)
    
    def __getitem__(self,item):
        return self.d[item]
    

    def __setitem__(self,item,value):
        self.d[item] = value
    

    def  __iter__(self):
        return self
    

    def __str__(self):
        return "<" + str(self.d)[1:-1] + ">"
    

    def __mul__(self,other):
        """now we are checking that if self and other both are the 
            object of Vector class so multiply both and return a new vector object. 
            and if other object is a number so multiply that number with the self vector and return a new vector object.  """
        length_of_self = len(self)
        # here we are creating a new object of vector
        result = Vector(length_of_self)
       
        if length_of_self == 0:
            return "The length of the vector is zero. "

        if isinstance(other,Vector):
            # now we will check that if the both vector length is equal 
            # so do the work else raise and exception error

            if length_of_self != len(other):
                raise ValueError("Dimensions must agree. ")
            
            
            # now we apply loop to traverse on the elements
            for i in range(length_of_self):
                result[i] = self[i] * other[i]
            
            return result
        
        elif isinstance(other,(int,float)):
            # here there is no need for length checking
           
            
            for i in range(length_of_self):
                result[i] = other * self[i]
            return result
        else:
            raise TypeError("other must be int or Vector object")
    



vector = Vector(4)
vector[0] = 100
