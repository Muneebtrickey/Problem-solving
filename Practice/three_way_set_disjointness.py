"""
disjoint: 
       the disjoint means there is no common value in the sequences. for example . a , b , c etc. 

For example: 
          i have three List and i want to check that is there something common in it if not return True if present return False. 
"""


def disjoint1(A,B,C):

    for a in A:
        for b in B:
            for c in C:
                if a == b == c: 
                    return False
    return True



A = [1,2,3]
B = [4,5,6]
C = [7,8,9]


print(disjoint1(A,B,C))



# the time complexity of the above code is O(n3)


# approch 2


def disjoint2(A,B,C):
    """now we will checking that if the value of a and value of b is equal then we will check the last list if not we will skip the loop on the List c"""
    
    for a in A:
        for b in B:
            if a == b:
                for c in C:
                    if a == c:
                        return False
    return True



print(disjoint2(A,B,C))