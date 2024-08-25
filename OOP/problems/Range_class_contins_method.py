class Range:
    def __init__(self,start,stop=None,step=1):

        """first of all we will check that if step is 0 then raise an error"""

        if step ==0:
            raise ValueError("Step can't be 0. ")
        
        if stop is None:     # specail case if  range(5) so it will start from zero
            start , stop = 0, start

        
        # now we calculating the effective length

        self._length = max(0, (stop - start + step -1) // step )


        self._start = start
        self._stop = stop
        self._step = step 


    
    def __len__(self):
        return self._length
    
    
    def __getitem__(self,k):

        # here we are handling the special case if the k is negative so we will convert 
        # it into positive

        if k < 0:
            k += len(self)
        
        if not 0 <= k < self._length:
            raise IndexError("Index out of range.")
        
        return self._start + k * self._step
    


    def __contains__(self,value):
        

        if value < self._start or value >=  self._stop: # because the stop is include in the range
            return False
        
        return (value - self._start) % self._step == 0
    
    
    

   



range = Range(-10 , 10)
print(range.__contains__(-99))



    




    

