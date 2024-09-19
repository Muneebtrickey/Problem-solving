# problem

"""
Element uniquness problem

we need to check that the sequence is unique or not. 

"""


def unique1(Sequence):
    n = len(Sequence)
    for i in range(n):
        for j in range(i+1, n):
            if Sequence[i] == Sequence[j]:
                return False
    return True


print(unique1([1,2,3]))



# approch 2 
# using the sorting technique


def unique2(S):
    n = len(S)
    sorted_list = sorted(S)

    for i in range(1,n):
        if sorted_list[i-1] == sorted_list[i]:
            return False
    return True


print(unique2([2,3,4,3]))