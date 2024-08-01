# Problem

"""
 Demonstrate how to use Python’s list comprehension syntax to produce
the list [ a , b , c , ..., z ], but without having to type all 26 such
characters literally
"""


# approch 1
# they are asking that we don't write the complete letters like this

small_letters = [i for i in "abcdefghijklmnopqrstuvwxyz"]
print(small_letters)





# another approch using ascii values
# the ascii value of a is 97 and z is 122 


letters = [chr(i) for i in range(97, 123)]
print(letters)




# approch 3

# using the string module and in the string there is constant
# called ascii_lowercase  in which all character is prsent

import string

L = [char for char in string.ascii_lowercase]
print(L)




# approch 4

# we can do this by using the map function and chr fucntion
# map function apply the function on the iterable 



llist = list(map(chr,range(97,123)))
print(llist)




# approach 5

# this approch is not common but valid for this

result = []
for i in range(97,123):
    result.append(chr(i))

print(result)




# approach 6

# here we will using the ord functin and chr function


lllist = [chr(ord("a")+i)for i in range(26)]

print(lllist)