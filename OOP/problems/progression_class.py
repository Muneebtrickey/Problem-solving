#problem

"""

Give a short fragment of Python code that uses the progression classes
from Section 2.4.2 to find the 8th value of a Fibonacci progression that
starts with 2 and 2 as its first two values.
"""



# now we are implementing the progression class
"""
first of all what is progression. progession is a series of numbers or sequence in which the current numbers depends on the the previous one like fibonacci series. 
"""


class Progression:
    def __init__(self, start=0):
        """
        Initialize the current to first value of the progression.
        """
        self._current = start
    
    def advance(self):
        """Update self._current to the new value.
        This could be overridden by a subclass to customize progression.

        By convention, if current is set to None, it will be the end of the progression.
        """
        self._current += 1
    
    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self.advance()
            return answer
    
    def __iter__(self):
        return self  # By convention an iterator must return itself as an iterator
    
    def display_progression(self, n):
        # Wrap the generator expression in list() to properly join the results
        print(" ".join(str(next(self)) for _ in range(n)))





class FibonacciProgression(Progression):

    def __init__(self,start=0, second=1):
        super().__init__(start)
        self._prev = second - start
    
    def advance(self):
        self._prev , self._current = self._current , self._prev + self._current 
    

# Example usage
progression = Progression()
progression.display_progression(10)


# no print the fibonacci progression

fibonacci = FibonacciProgression(2,2)
fibonacci.display_progression(9)





# problem

"""
When using the ArithmeticProgression class of Section 2.4.2 with an increment of 128 and a start of 0, how many calls to next can we make
before we reach an integer of 263 or larger?
"""


class ArithmeticProgression(Progression):
    def __init__(self, increment=1 , start=0):

        super().__init__(start)
        self._increment = increment
    
    
    def advance(self):
        self._current += self._increment


    def display_progression(self):
        calls = 0
        while True:
            if str(next(self)) >= str((2 ** 63)):
                break

            calls += 1
        return calls



    




arithmetic = ArithmeticProgression(128)
print(arithmetic.display_progression())




