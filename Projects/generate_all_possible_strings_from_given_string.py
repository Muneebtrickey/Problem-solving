# Project No 1
# Problem

"""
Write a Python program that outputs all possible strings formed by using
the characters c , a , t , d , o , and g exactly once


"""


# using the shuffle function to do it. 

"""
Algorithm: 
        1. first of all we will be created a  list name generated string which will store the generate string from the given string. 


        2. now we will apply loop and this loop will be terminated when reach to 100. 

        3. Inside the loop i will be using the fisher algorithm to shuffle the list and then using the join funciton to create a single string. 
        
        4. and then i will check that if the givne string is present in the generated string so don't add it. 

        5. after completeion of the loop the generated string will be returned . 

"""
import random

def generation_of_stirng(s):
    generated_string = []
    copy_of_string = s[:]
    for i in range(5000):
        for j in range(len(s)-1,0,-1):
            random_number = random.randint(0,j)
            copy_of_string[j], copy_of_string[random_number] = copy_of_string[random_number], copy_of_string[j]
        
        String = "".join(copy_of_string)
        if String not in generated_string:
            generated_string.append(String)
        
    return generated_string


        
        


s = ["c","a","t","d","o","g"]
generated = generation_of_stirng(s)
print(len(generated))


# the above approch is good approch but it is not efficeint because it
# did not take gurrenty to do the exist permutation 



# approch 2 
# the correct and efficent one
# we will be using itertools 


import itertools

def genertion_of_string2(s):
    return ["".join(p) for p in itertools.permutations(s)]



print(len(genertion_of_string2(s)))
print(genertion_of_string2(s))