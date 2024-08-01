# Problem

"""
we have give a sequences of integers and we need to find the distant pair of numbers whose product is odd in the given sequences. 
"""


# direct code

def distant_number_whose_product_odd(List):
    for i in range(len(List)):
        for j in range(i+1 , len(List)):
        
                if (List[i] * List[j]) %  2 != 0:
                    return True
    
    return False

l = [2,3,4]
print(distant_number_whose_product_odd(l))


# the time complexity of this code is o(n2)




# another approch:

"""

we need to find the odd number because the product of odd number is always odd. 

algorithms:
       1. we will create a variable called count which will count the number of odd number. 

       2. now we will apply loop on the list. 

       3. and now we will check that if the number is odd so update the odd counter. 
       4. and then we will write another condition that if the odd counter is     then return True. 
       5. else return False



"""

def count_odd_number(List):
     odd_counter = 0
     odd_distant_list = []
     for item in List:
        if item % 2 != 0:
            # we need to find the product of distant number
            if item not in odd_distant_list:
                 odd_distant_list.append(item)
                 odd_counter += 1
                

        
        if odd_counter == 2:
            return True
     return False


print(count_odd_number([2,4,5,6]))           
        
        

        
