#problem

"""
The SequenceIterator class of Section 2.3.4 provides what is known as a
forward iterator. Implement a class named ReversedSequenceIterator that
serves as a reverse iterator for any Python sequence type. The first call to
next should return the last element of the sequence, the second call to next
should return the second-to-last element, and so forth.
"""



# first of all i want to create a forward iterator for the sequence


class ForwardSequenceIterator:
    def __init__(self,sequence):
        # we will create a variable which will store the sequence
        self._seq = sequence
        # now we will create another variable which will keep the address of element

        self._k = -1   # for the first call it will be 0

    
    def __next__(self):
        self._k += 1

        if self._k < len(self._seq):
            return self._seq[self._k]
        else:
            raise StopIteration()
    

    def __iter__(self):
        return self
    
    def __str__(self):
        return str(self)





# now our task is to create a reversedsequenceiterator


class ReversedSequenceIterator:
    def __init__(self,sequence):
        self._seq = sequence
        self._k = len(sequence) -1 
                                
    
    def __next__(self):
        
        if self._k >= 0:
            value = self._seq[self._k]
            self._k -= 1
            return value
        else:
            raise StopIteration()
    
    def __iter__(self):
        return self


    
reversed = ReversedSequenceIterator([1,2,3,4,5,6])

for item in reversed:
    print(item)
    
     