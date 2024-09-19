# problem

"""
2022. Convert 1D Array Into 2D Array

You are given a 0-indexed 1-dimensional (1D) integer array original, and two integers, m and n. You are tasked with creating a 2-dimensional (2D) array with  m rows and n columns using all the elements from original.

The elements from indices 0 to n - 1 (inclusive) of original should form the first row of the constructed 2D array, the elements from indices n to 2 * n - 1 (inclusive) should form the second row of the constructed 2D array, and so on.

Return an m x n 2D array constructed according to the above procedure, or an empty 2D array if it is impossible.

 

Example 1:


Input: original = [1,2,3,4], m = 2, n = 2
Output: [[1,2],[3,4]]
Explanation: The constructed 2D array should contain 2 rows and 2 columns.
The first group of n=2 elements in original, [1,2], becomes the first row in the constructed 2D array.
The second group of n=2 elements in original, [3,4], becomes the second row in the constructed 2D array.
Example 2:

Input: original = [1,2,3], m = 1, n = 3
Output: [[1,2,3]]
Explanation: The constructed 2D array should contain 1 row and 3 columns.
Put all three elements in original into the first row of the constructed 2D array.
Example 3:

Input: original = [1,2], m = 1, n = 1
Output: []
Explanation: There are 2 elements in original.
It is impossible to fit 2 elements in a 1x1 2D array, so return an empty 2D 

"""



# systematic way to solve this problem

"""
1. understand the problem clearly and precisely. Identify input and output format. 
2. come up with some example inputs and outputs and try to cover all edges cases. 
3. come up with a correct solution and state it in plain english. 
4. Implement the solution and test it using example inputs and outputs and try to fix any bugs if occur. 
5. Identify ineffiency if any. 
6. Repeat step 3 to 6 to overcome inefficency if any. 
"""



"""
step1: Understand the problem clearly and precisely. Identify inputs and outputs format. 


problem:
        we need to convert the 1d array into 2d array looking the the m which denotes rows and n which denotes columns . 


    formats:
      inputs: 
          List: a sequence of elements
          m : which denotes row
          n : which denotes column

      outputs:
           List : which represent 2d array 

           


step2: come up with some example inputs and outputs and try to cover all edge cases. 



"""

all_edge_cases = []

# if the List is empty
all_edge_cases.append({
    "input": {
        "List": [],
        "m": 2,
        "n": 2

    },
    "output": []
    
})



# if the list have only one element and m is also 1 and n is also 1

all_edge_cases.append({
    "input": {
        "List": [1],
        "m": 1,
        "n": 1
    },
    "output": [[1]]
})


# if the List have 2 elements and m is 1 and n is 2

all_edge_cases.append( {
    "input": {
        "List": [1,2],
        "m": 1,
        "n": 2

    },
    "output": [[1,2]]
})


# if the length of the List is greater then m * n

all_edge_cases.append({
    "input": {
        "List": [1,2,3,4,5,6,7],
        "m": 2,
        "n": 3
    },
    "output": []
})


# what if the list have negative values

all_edge_cases.append({
    "input": {
        "List": [-1,-2,-3,-4,-5,-6],
        "m": 2,
        "n": 3
    },
    "output": [[-1,-2,-3],[-4,-5,-6]]
})



# what if the m*n is greater than the length of the List

all_edge_cases.append({
    "input": {
        "List": [1,2,3,4,5],
        "m": 2,
        "n": 3
    },
    "output": []
})



"""
now we define all the above edges cases and now we will come with with a correct solution. 



step3: come up with a correct solution and state it in plain english. 

    Algorithm: 
             1. first of all we will find the length of the List. 
             2. Then we will check that if the length of List is equal to the
                (m*n) then do the following things. 
             
             3. we will apply the loop and this loop will be executed upto m. 
             4. before the loop we will create a variable in which the slicing
                will start from it and we name it previous = 0. 
             
             5. now we will take the slice from the original List and assign the 
                the new slice in that place like this . 
                     original[previous: n] = [original[previous: n]]
                     so it the new list on the right hand side will be added in the original. and we use n because we need n column
            
             6. after the above line we need to update the previous and n for the next step

             7. we i update the previous 1 like previous += 1. for example. 
                  i have a List , List = [1,2,3,4,5,6] and m = 2 , n = 3
                  so my loop will iterate upto m so m is 2
                    previous = 0
                     for i in range(m):
                         original[previous:n ] = [original[previous: n]]
                         [1,2,3]               = [[1,2,3]]

                         i show the values for the above code now the left side list is replaced by the right side

                         [[1,2,3],4,5,6]   so if you look above my previous was 0 and n was 3 right. 

                         now if you look at the original List it have 4 elements one is [1,2,3], second is 4 and third is 5 and 4th is 6. 
                         so i need to update the previous from zero to 1. 
                           previous += 1 so here previous refers to 4 so in the next step 4 to 6 will added in previous place which is 1. 

                           but wait our n  = 3 right so after updating the previous we need to update the n . so we will also update the n to 1 , n += 1 because our origial list have 4 element left and n is refer to 3 so need will update it to refer to 4. 
                            n += 1
                
                8. after completion of the loop we will return original List
                9. if the above condition which is if length == (m*n) is false
                   so return empty List. 


step4: Implemenet the solution and test it using example inputs and outputs and 
       fix bugs if any. 



"""

from typing import List

from jovian.pythondsa import evaluate_test_case, evaluate_test_cases



def convert_to_2d_array(List: List[int], m : int , n : int) -> List[int]:

    # first of all we will calculate the length of the List
    length_of_list = len(List)

    # now we will check that if the length is equal to the m*n so do your work

    if length_of_list == (m*n):

        # now we will create a variable and we call it start or previous
        previous = 0

        
        # now we will apply loop upto m because we need m rows
        for i in range(m):

            # now the original thing happens here , we are replacing here 
            List[previous: n] = [List[previous: n]] # [1,2,3] = [[1,2,3]]

            # after the above step we will update the previous and n
            previous += 1
            n += 1
        
        return List
    
    else:

        return []
    


# normal example

List = [1,2,3,4,5,6]
m = 2 
n = 3
print(convert_to_2d_array(List, m , n ))  

# finally our code is working correctly

# now i want to check all testcase to verify. 

# for this i will import a module and this module have the function to test
# your code 


evaluate_test_cases(convert_to_2d_array, all_edge_cases)  # wow my all test cases are correct. 


# now i am going to optimize it because the time and space complexity if 0(m*n)