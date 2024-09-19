# Recurssive implementation of a  factorial function


"""
what is factorial function:

Answer: factorial function is a mathematical function which is denoated by  'n!' and it means that the product of all the numbers below the given 'n' to 1 is called factorial of n. 


   for example: 
           factorial of n = 5

           so the factorial of 5 is 120. 
            
           5 x 4 x 3 x 2 x 1 = 120 . 


so i will write a recurisve function which will calcualte the factorial of a number.


important point:
      The factorail of n = 0 is by convention 1. 


In the Recursion two things is important. 
    1. the first is base case. 

           base cases is like the ending point of a recursion

           for example. 
                     if want to find the factorial of 5 so
                     for this 5 x 4 x 3 x 2 x 1 x 0 so when my function reach to zero i will return 1 and stop the recursion 
    
                     
        2. The recursive step:
             what it means that recursive step the recursive step means we will divide the problem into step by step until it reach to teh base case.



             for example:
               i want to find the factorial of 5 so my function will be called like this

               factorial(5) * factorial(5-1) * factorial(5-2) and so on. unitil it reach to 0 
               so this is the recursive step. 

now lets come to the actual implementation of a factorial function. 

      
"""

def factorial(n: int) -> int:
    # first of all we will write the base case

    if n == 0:
        return 1  # we know that the factorial of 0 is 1. 
    
    else:
        return n * factorial(n-1)  # so this function will be called until n == 0 



# now lets test the function that it is working or not


print("The factorial of 5 is: ",factorial(5)) # 120



"""
so in the above function what we did we did the problem into sub-problem and then add the solutions of sub-problem to solve the main problem.


  Flow of the function:
      first we pass n = 5
      so it will check that if n == 0 so return 1 but n is 5. 
      so it come the else part and in the else part 
      we write n * factorial(n-1) so here n is 5 and we call the function again which the value 4 because 5 -1 = 4 
      so when the function is called with 4 so it will check again that if n which is 4 equal to 0 so return 1 but n is 4 so it come again towards else so in the else n which is 4 again come like this 4 * factorial(3) so if you think from the start 5 * 4 * factorial(3) and so on. 
       
      when the n == 0 so it will exit the recursive function and all the value from 5 * 4 * 3 * 2 * 1 will be multiplied and the result will be returned. 

"""