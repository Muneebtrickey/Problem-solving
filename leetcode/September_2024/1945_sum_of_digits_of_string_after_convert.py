# problem

"""
1945. Sum of Digits of String After Convert

You are given a string s consisting of lowercase English letters, and an integer k.

First, convert s into an integer by replacing each letter with its position in the alphabet (i.e., replace 'a' with 1, 'b' with 2, ..., 'z' with 26). Then, transform the integer by replacing it with the sum of its digits. Repeat the transform operation k times in total.

For example, if s = "zbax" and k = 2, then the resulting integer would be 8 by the following operations:

Convert: "zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124
Transform #1: 262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17
Transform #2: 17 ➝ 1 + 7 ➝ 8
Return the resulting integer after performing the operations described above.

 

Example 1:

Input: s = "iiii", k = 1
Output: 36
Explanation: The operations are as follows:
- Convert: "iiii" ➝ "(9)(9)(9)(9)" ➝ "9999" ➝ 9999
- Transform #1: 9999 ➝ 9 + 9 + 9 + 9 ➝ 36
Thus the resulting integer is 36.
Example 2:

Input: s = "leetcode", k = 2
Output: 6
Explanation: The operations are as follows:
- Convert: "leetcode" ➝ "(12)(5)(5)(20)(3)(15)(4)(5)" ➝ "12552031545" ➝ 12552031545
- Transform #1: 12552031545 ➝ 1 + 2 + 5 + 5 + 2 + 0 + 3 + 1 + 5 + 4 + 5 ➝ 33
- Transform #2: 33 ➝ 3 + 3 ➝ 6
Thus the resulting integer is 6.
Example 3:

Input: s = "zbax", k = 2
Output: 8

"""


"""
step1: Understand the problem clearly and precisely. Identify inputs and outputs formats:
  

   problem:
        we are given a string and we need to convert this string into integer in which a represent 1 and b represent 2 and  z represent 26. And we have given k 
        in which we will add the all the integers k times and when add all integers k time so we will return the result and that will be our answer. 

    
    
    formats:
       input: 

         S: which is a string 
         k : we will add these string k times 
        
       
       output:
            result: return the result when you add all the integers k times. 
    
            

step2: 
     come up with some example inputs and outputs and try to cover all edges cases. 

"""

all_test_cases = []

# what if the string is empty but here the restriction is that one element will be present always

all_test_cases.append({
    "input": {
        "s": "a",
        "k": 2

    },
    "output": 1
})


# what if the string has two elements


all_test_cases.append({
    "input": {
        "s": "zx",
        "k": 2
    },
    "output": 5
})


"""
step3: come up with a correct solution and state it in plain english. 


   Algorithm: 
            1. First of all i will create a dictionary and in this dictionary i will store values which start from a which is 1 and b which 2 and so on. 

            2. now we will apply loop on the string which is s and we will create a variable and called it string and we will store the values of in this string. for example . 
                     s = "abc"

                     so i create a variable
                     string = ""

                     i will apply loop on the s like this:
                      
                        for item in s:
                           string += str(lower_cases_values[item])
                        
                           
                       so after the completion of the loop 

                       string = "123" values 
            
            3.  Now i will sum all the digits of the string k times for example k is 2. so 
                        first time : 
                                1 + 2 + 3 = 6
                        
                        second time: 
                                 there is only one digit which is 6 so there is not any digit to sum it 
                                 so we will return 6. 
            
                        


step4: Implement the solution and test it using example inputs:

"""
from jovian.pythondsa import evaluate_test_case, evaluate_test_cases

def getLucky(s: str, k : int):

    # first of all i will create  a dictionary
    lower_case_values = {
    "a": 1,  "b": 2,  "c": 3,  "d": 4,  "e": 5,  "f": 6,  "g": 7,  "h": 8,  "i": 9,  "j": 10, 
    "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, 
    "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}


    # now i will create a string variable in which the values of s will be stored
    string = ""

    
    # now i will apply loop on the s and access it values from dictionary and add to string

    for item in s:
        string += str(lower_case_values[item])


    # now i will create a variable total which will store the sum of digits
    total = 0

    # now i will add the sum of digits upto k time

    while k > 0:

        # now i will apply loop on the string and add it values into a variable total
        for item in string:
            total += int(item)
        
        # after completion of the loop we will decrement the k because we add all
        # element one time 
        k -= 1

        # this place is a bit trickey but easy if you see that when i sum 
        # the digits i convert it from str to int right
        # so here the total will have an integer values so we will convert it again
        # to string because we will add again the total element so the int values
        # are not iterable so we can loop through it. for example
                           # total = 3234
                           # so we can loop in the total because it is an integer
                           # so we need to convert it to string first 
        
        string = str(total)

        # now i will make total to zero because above everything add in the total
        # so i make it clear
        total = 0

    
    # and after completion of the while loop we will return the string which 
    # will be answer

    return int(string) # here the answer is asking in int so i convert it


# testing with normal example
s = "zbax"
k = 2
print(getLucky(s, k))



# now we will check will all tests cases
evaluate_test_cases(getLucky, all_test_cases)  # wow all tests cases passed



"""
step5: Identify inefficency if any. 

step6: Repeat step 3 to 6 to overcome the inefficency if any. 

"""


def getLucky2(s: str , k : int):

    # first of all i will create a string in which the numeric value for the 
    # string will be present

    numericstring = ""
    
    # now i will apply loop on the s and find the numerical values

    for item in s:
        numericstring += str(ord(item) - ord("a") + 1)
    

    #now i will do the summation process repeatedly

    while k > 0:
        digitsum = 0
        for item in numericstring:
            digitsum += int(item)
        
        k -= 1

        # now i will conver the integer of digitsum to string again for repeation
        numericstring = str(digitsum)

    
    return int(numericstring)


print(getLucky2(s, k ))



# the time and space complexity of this code is O(n). 

