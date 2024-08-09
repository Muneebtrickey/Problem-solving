# project 2
# Problem


""""
Write a Python program that can take a positive integer greater than 2 as
input and write out the number of times one must repeatedly divide this
number by 2 before getting a value less than 2.


"""


# Algorithm: 

"""
1. First of all we will create a counter and assign 0 to it. 
2. Then we will apply loop and the condition for the loop is
   while n > 2 if n is less than 2 the loop will be terminated. 
3. now we will divde the n by 2 and assign the result to the n. 
4. then we will check that if the  n > 2 so update the counter by 1. 
5. after termination of the loop return the counter. 

"""

# code 

def number_of_times_divison(n):
    counter = 0
    if n <= 2:
        return "number must be greater than 2. "
    while n > 2:
        n = n / 2 
        counter += 1
    
    return counter


print(number_of_times_divison(50))



# approch 2 
# using recurrsion


def recurrsion(n, counter=0):
    if n < 2:
        return counter
    return recurrsion(n/2, counter+1)

print(recurrsion(50))






# approch 3
# using logrithm
import math
def number_of_times_logarithm(n):

    if n <= 2:
        return "number must be greater than 2. "
    
    return math.floor(math.log(n,2))

print(number_of_times_logarithm(50))




#approch 4
# using bitwise operation


def number_of_times_bitwise(n):
    if n <=2 :
        return "number must be greater than 2. "
    
    counter = 0
    
    while n > 2:
        n >>= 1
        counter += 1
    return counter



print(number_of_times_bitwise(50))
