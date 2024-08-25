from abc import ABCMeta , abstractmethod

class Sequence(metaclass= ABCMeta):
    @abstractmethod
    def __len__(self):
        """Return the length of the sequence"""
        pass

    @abstractmethod
    def __getitem__(self,j):
        """Return an element in the index jth of the sequence"""
        pass

    
    def __contains__(self,val):
        """Checking that the value is present in the sequence if return False"""
        for i in range(len(self)):
            if self[i] == val:
                return True
        return False
    

    def  index(self,val):
        """Return the index if the value is present else return valueError"""
        for i in range(len(self)):
            if self[i] == val:
                return i
        raise ValueError("Value not in a sequence. ")
     
    

    def count(self,value):
        """Return the count of value present in the sequence"""
        k = 0
        for i in range(len(self)):
            if self[i] == value:
                k += 1
        return k
    

    # now this is our task 
    
    def __eq__(self,other):
        """now we are checking that both the sequence are equal element by element or not """
        
        if len(self) != len(other):
            return False
        
        else:
            for i in range(len(self)):
                if self[i] != other[i]:
                    return False
            return True
        

    

    """
    In similar spirit to the previous problem, augment the Sequence class with
method lt , to support lexicographic comparison seq1 < seq2.
    """

    #code 

    def __lt__(self,other):

        L1 = len(self)
        L2 = len(other)

        less_length = min(L1,L2)  # here we apply loop on the minimum length

        for i in range(less_length):
            if self[i] < other[i]:
                return True
            elif self[i] > other[i]:
                return False
        
        return L1 < L2



