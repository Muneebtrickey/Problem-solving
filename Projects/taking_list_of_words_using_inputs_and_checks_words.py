# project
# problem:

"""
Write a Python program that inputs a list of words, separated by whitespace, and outputs how many times each word appears in the list. You
need not worry about efficiency at this point, however, as this topic is
something that will be addressed later in this book
"""


"""
step1: understand the problem clearly and precisely. identify inputs and outputs formats. 

    problem:
          we need to find the occurance of each words in a list and we will give each words in the inputs separated by whilte space. 
    
          
    formats: 
        input:  a list of words separated by white space
         
        output: print the occurance of each word
    
        
step2: come up with some example inputs and outputs and try to cover all edge cases. 


"""

tests = []


# if the list is empty

tests.append({
    "input":{
        "list": []
    },
    "output": "List is empty"
})


# if the list have some elements

tests.append({
    "input": {
        "list": ["muneeb","anees","muneeb"]
    },
    "output": ["muneeb appears 2 time","anees appears 1 time"]
})



"""
step3: come up with a correct solution and state it in a plain english. 


   Algorithm: 
            1. first of all we take an input and after taking the inputs we will convert the inputs into a list. 
            2. now we will apply loop on the List and inside the loop we will check  the occurance of the words. 

            3. for checking we will use the count() in the list to count the number of times. 

            4. and then we will print the name and also print the numbers of times. 
        
step4: implement the solution and test it using examples inputs and fix bugs if any. 
"""


def count_occurance_in_a_list():
    List = input("Enter your words: ").split()
    # we will convert the list inot set so that to 
    # remove the duplicate
    set_of_list = set(List)
    for item in set_of_list:
        counter = List.count(item)
        print(f"{item} appears {counter} of times. ")


count_occurance_in_a_list()



# using list comprehension

def count_words_in_a_list():
    List = input("Enter your words: ").split()
    set_of_name = set(List)
    number_of_counts = [item + str(List.count(item)) for item in set_of_name]

    for item in number_of_counts:
        print(item)


count_words_in_a_list()



# approch 3 
# using the dictionary

def count_number_of_words():
    dic = {}
    words_list = input("Enter your words : ").split()
    for word in words_list:
        if word not in dic:
            dic[word] = 1
        else:
            dic[word] += 1
    
    for word in dic.keys():
        print(f"{word} appears {dic[word] } times. ")


count_number_of_words()


