# project
# problem



"""
A common punishment for school children is to write out a sentence multiple times. Write a Python stand-alone program that will write out the
following sentence one hundred times: “I will never spam my friends
again.” Your program should number each of the sentences and it should
make eight different random-looking typos.
"""


"""
step1: Understand the problem clearly and precisely, indentify inputs and outputs format. 


   problem: 
         we need to print this sentences 100 time 'i will never spam my friends again' with number and with 8 different random typos. 
    
    inputs:
         string: i will never spam my friend again. 
    
    outputs:
        string: 100 times with numbers and eight typos. 


    
        
step2: come up with some example  inputs and outputs and try to cover all edges cases. 


# if the string is empty so return string is empty. 
# if the string is only one element so print 100 time. 


step3: come up with a correct solution and state it in plain english. 
      Algorithm: 
      
      1. first of all we will apply loop and inside the loop we 
         will write th following condition:
        
            if the i < 8 so do the following:
                we will convert the string into List
                and then we will take random_number for the string
                and then we will take random_item from the string 
                and thn we will change in the list and after changing we will create a single list again using the join function. 
                and then we will print the number and the string. 
        
        3. in the else part we will just print the number and the string. 


"""
import random
def punishment_for_student(student_string):
    length = len(student_string)-1
    
    for i in range(1,101):
        
        if i <= 8:
            List = list(student_string)
            random_number = random.randrange(length)
            random_item = random.choice(student_string)
            List[random_number] = random_item
            # now we will create a single string from the list of 
            # strings
            single_string = "".join(List)
            print(i, single_string)
        
        else:
            print(i,student_string)
    
    if length == 0:
        print("string is empty!")


s = "i will never spam my friends again"
#punishment_for_student(s)




# approch 2 
# using stirng manipulation



def punishment_for_student2(s):
    length = len(s) - 1
    # this loop will go to 100

    for i in  range(1,101):
        
        if i <= 8:
            random_index = random.randrange(length)
            random_item = random.choice(s)

            # now we will create another string in which 
            # we will replace the random_index with the random
            # item

            type_sentence = (s[:random_index] + random_item + s[random_index + 1: ])
            print(i, type_sentence)

        else:
            print(i, s)

    if length == 0:
        print("String is empty:")



#punishment_for_student2(s)





# approch 3
# using the sample() function from the random module


def punishement_for_student3(s):
    typos_list = random.sample(range(100),8)

    for i in range(1,101):

        if i in typos_list:
            random_index = random.randrange(len(s)-1)
            random_item  = random.choice(s)

            typo_sentence = (s[:random_index] + random_item + s[random_index + 1: ])
            print(i, typo_sentence)
        
        else:
            print(i,s)
    
    if len(s) == 0:
        print("String is empty: ")


punishement_for_student3(s)

