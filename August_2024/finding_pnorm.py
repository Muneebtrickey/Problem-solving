# problem

"""
The p-norm of a vector v = (v1,v2,...,vn) in n-dimensional space is defined as
v =
p
v
p
1 +v
p
2 +···+v
p
n .
For the special case of p = 2, this results in the traditional Euclidean
norm, which represents the length of the vector. For example, the Euclidean norm of a two-dimensional vector with coordinates (4,3) has a
Euclidean norm of √
42 +32 = √16+9 = √
25 = 5. Give an implementation of a function named norm such that norm(v, p) returns the p-norm
value of v and norm(v) returns the Euclidean norm of v. You may assume
that v is a list of numbers

"""



# code 

def norm(v, p=2):
    p_norms = 0
    for vector in v:
        p_norms += (vector ** p)
    square_root = p_norms ** (1/p)

    return square_root


v = [2,3,4]
print(norm(v))




# approch 2 


import math
def norm2(v, p=2):
    p_norms = 0
    for vector in v:
        p_norms += math.pow(vector,p)

        square_root = math.pow(p_norms, 1/p)
    
    return square_root



print(norm2(v))





# using list comprehension

def norm3(v,p=2):
    p_norms  =  sum([vector ** 2 for vector in v])

    square_root  = p_norms ** (1/p)
    return square_root



print(norm3(v))




# approch 4 
# using the numpy library


import numpy as np


def norm4(v,p=2):
    return np.linalg.norm(v,p)


print(norm4(v))
     


