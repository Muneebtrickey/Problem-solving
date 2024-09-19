# prefix average:

"""
prefix average means finding the averages of the original list up to the specific position. 

      for example: 
      
               original list : List = [5,10,15,20]
               so average prefix is 
                A = [5,7.5 and so on]

                (5 + 10) / 2 which is equal to 7.7

                for the third one we will add  the 
                   5 + 10 + 15 / 3 and it will give you result and that will be equal to the average for the third. 

"""


def prefix_average1(Sequence):
    # first of all i will calculate the length of the list
    n = len(Sequence)  #  the running time is O(1)

    # now we will create another list which length will be same. 
    A = [0] * n   # so the A will be create with zero values
   
    
    for i in range(n):
        total = 0
        for j in range(i + 1):
            total += Sequence[j]
        
        A[i] = total / (i+1)
    
    return A


List = [5,10,15,20]
print(prefix_average1(List))



# second approch


def prefix_average2(Sequence):
    n = len(Sequence)
    A = [0] * n
    
    for i in range(n):
        A[i] = sum(Sequence[0:i+1]) / (i + 1)
    return A



print(prefix_average2(List))



# the time complexity of both the algorithm is O(n2) which 
# means quadratic


# approch 3

def prefix_average3(S):

    n = len(S)

    A = [0] * n

    total = 0
    
    for i in range(n):
        total += S[i]

        A[i] = total / (i + 1)
    
    return A


print(prefix_average3(List))

# the time complexity of the algorithm 3 is o(n) which means linear



