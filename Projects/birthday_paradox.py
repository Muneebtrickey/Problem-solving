#project

#problem

"""
The birthday paradox says that the probability that two people in a room
will have the same birthday is more than half, provided n, the number of
people in the room, is more than 23. This property is not really a paradox,
but many people find it surprising. Design a Python program that can test
this paradox by a series of experiments on randomly generated birthdays,
which test this paradox for n = 5,10,15,20,...,100.
"""



"""
step1: understand the problem clearly and precisely. Identify inputs and outputs formats:
    
      problem:
            we need to check that the two people have  a same birth in a room in which total people is 23. so we need to create a program for this to check probability more in the problem they are saying that there is 50 % more chance two have the same birth in 23 people are more. 
        
            


        input: 
            group: a group of people
        
        output:
            birth_day = if two people are same birth  or not
    
            
step2:
    come up with some example inputs and outputsa and try to cover all edges cases. 

    
# if the group has no member so return group has no member
# if the group has one member return group has only one member
# if the group has two member return same birth or not




step3: 
     come up with a correct solution and state it in plain english. 
    
     
     Algorithm: 
              1. first of all we will apply loop which condition will be 
                 for i in range(sizeofgroup):
                
             2.  now we will generate random birhtday so i will generate a single integer which will represent a birthday so the condition is:
               random_birthday = random.randrange(pass the size of group)
            
               
            3. now i will add the random_brithday in a list or set and check that if the random_bithday in List_of_random_birth so 
            exit the loop and the message will be printed that two people have  a same birthday. 

            


"""
import random


def birthday_paradox(group: int):
    if group == 0:
        return "group have no member"
    
    if group == 1:
        return "group have only one member"
    
    # create a list to store random birthdays
    list_of_random_birthdays = []
    

    for i in range(group):  # because the range function exculde the
                              # last item so i add one. 
        random_birthday = random.randint(1,365)

        if random_birthday not in list_of_random_birthdays:
            list_of_random_birthdays.append(random_birthday)
        
        else:
            return "two people have same birth day" + str(random_birthday)
        
    return "No one shares birthday"
    
groups = [5,10,15,20,25,50,100]
for group in groups:

    print(birthday_paradox(group))