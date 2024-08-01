# problem 

"""
Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing.
"""



# solution


# we need to write the pseudo-code description of a function which # reverse a list and then we will also compare this function with # the built in function. 


# we can reverse a list in different approches.
#  1st one is that we will use the slicing method it will create a # new list from the already existing list but in the reverse order


# pseudo-code of the approch 1.

"""
   1.first we will create a variable and in the this variable the new list will be present .  reverse_list  . 
   2. now we willl write like this  List[::-1] this will create the list which will be in the reverse order. 
   3. and in the last we will return the reverse_list. 

"""


def reverse_list(List):
    list_reverse = List[::-1]
    return list_reverse


List = [5,7,2,1,3]
print(reverse_list(List))




# this is the another approch through which is the list is reversed.


"""
pseudo-code.  
        1. first we will create two varialbe left and right, in left 0 will be assign and in right length of the list -1 will be assigned. 

        2. and then we will apply loop.  
        3. and then we swap the left and right value 
        4. and then we will update the pointer
        5. and then we will check that if the len(L) // 2 == left so terminate the loop because there is only one item left which is the center of the list. 

"""




def reversing_a_list(L):
    left = 0
    right = len(L) -1
    
    while True:
        temp = L[left]
        L[left] = L[right]
        L[right] = temp

        left += 1
        right -= 1

        if (len(L)//2) == left:
            break
    return L

print(reversing_a_list(List))






# now we will use the built in function. 

L2 = [1,2,3,4,5]
L2.reverse()
print(L2)
