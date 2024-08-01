from jovian.pythondsa import evaluate_test_cases

# problem

"""
Write a short Python program that takes two arrays a and b of length n
storing int values, and returns the dot product of a and b. That is, it returns
an array c of length n such that c[i] = a[i] · b[i], for i = 0,...,n−1.
"""



"""
step 1:
       Understand the problem clearly and precisely. Identify inputs and outputs formats.


       problem:
           we need to find the dot product of the array a and array b and these array have the same lenght and integers values are stored in the array a and b. And we need to return the array c in which the dot product of the a[i] * b[i] is present in c[i] which starts from the 0 to n-1. 

        
           
        inputs: array a and b of same length of int values. 

        output: it will return array c. 


        def dot_prodcut(a,b):
              pass
        

              
step2 : 
       come up with some example inputs and outputs and try to cover all edges cases?

"""

tests = []
# if the list have positive numbers
tests.append({
    "input": {
        "a": [1,2,3],
        "b": [4,5,6]
    },
    "output":[4,10,18]
    
})

# if both the list is empty

tests.append({
    "input": {
        "a": [],
        "b": []

    },
    "output": []
})

# if both the list have only one item


tests.append({
    "input": {
        "a": [1],
        "b": [3]
    },
    "output": [3]
})


# if one list have positive number and another have negative


tests.append( {
    "input": {
        "a": [1,3,4],
        "b": [-3,-4,-5]
    },
    "output": [-3,-12,-20]

})


# if the length of array are not same

tests.append({
    "input": {
        "a": [1,2,3,4],
        "b": [4,7]
    },
    "output": "length of the array must same. "
})


"""
step 3: come up with a correct solution and state it in plain english. 


     step1: first of all we check that the length of a and b is equal. 
     2. we will create  a list name c. 

     3. we will apply loop and the condition is for i in range(len(a)). 
     
     4. now we will append a[i] * b[i] in the c. 

     5. after completion of the loop we will return the c



"""

#step 4. Implement  the solution and fix bugs if any?

def dot_product(a,b):
    if len(a) == len(b):
        c = []
        for i in range(len(a)):
            c.append((a[i]*b[i]))
        
        return c
    else:
        return "length of the array must same. "
    

a = [1,2,3]
b = [4,5,6]
print(dot_product(a,b))



evaluate_test_cases(dot_product,tests)



"""
step 5: Analysize the algorithm complexity and identify inefficencey if any. 

  The item and space complexity of my code is O(n) because it iterate on all the list so the time complexity is O(n). 
   And space complexity is also O(n) because the list c require length which is equal to the list of a and b so it space complexity is also 0(n). 




   step6: Apply the right technique to overcome the inefficeny and repeat step 3 to 6.
 
"""

# approch 2
# using list comprehension

def dot_product_list_comprehesion(a,b):
    if len(a) != len(b):
        return "length must be same. "
    return [a[i]*b[i] for i in range(len(a))]



# the time complexity of this is also O(n) and space is also
# o(n) but the list compreshenison is faster. 




# approach 3
# list comprehsion is also used in this but we use zip function here


def dot_zip_product(a,b):
    if len(a) != len(b):
        return "length must same. "
    return [x*y for x , y in zip(a,b)]


# approch 4 
# using numpy

import numpy as np

def dot_numpy_product(a,b):
    if len(a) != len(b):
        return "length must be same. "
    a_numpy_array = np.array(a)
    b_numpy_array = np.array(b)
    return list(a_numpy_array * b_numpy_array)

print(dot_numpy_product(a,b))