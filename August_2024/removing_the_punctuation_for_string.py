# problem

"""
Write a short Python function that takes a string s, representing a sentence,
and returns a copy of the string with all punctuation removed. For example, if given the string "Let s try, Mike.", this function would return
"Lets try Mike".
"""


# approch 1

# algorithm

"""
1. first we will create a list of all  letters.  
2. then we will apply loop on the string and the condition is
   for item in string. 

3. now inside the loop we will be check that if the item not in List of letters so remove it from the string. 
4. after terminating the loop return the original string. 

"""

letters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

def removing_punctuation(s):
    copy_string = s[:]
    for item in s:
        if item not in letters:
           copy_string = copy_string.replace(item," ")
    
    return copy_string


s = "Hello, this's me and i love you dad's car"
print(removing_punctuation(s))







# approach 2

# ascii values for the punctuation marks
# start from 34 to 47
# 58 to 64
# 91 to 96
# 123 to 126


ascii_values_punctuation = [
    33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47,
    58, 59, 60, 61, 62, 63, 64,
    91, 92, 93, 94, 95, 96,
    123, 124, 125, 126
]


def removing_punctuation_using_ascii(s):
    for item in s:
        if ord(item) in ascii_values_punctuation:
            s = s.replace(item," ")
    
    return s


print(removing_punctuation_using_ascii(s))





# approch 3
punctuation_marks = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    ':', ';', '<', '=', '>', '?', '@',
    '[', '\\', ']', '^', '_', '`',
    '{', '|', '}', '~'
]



def removing_punctuation_using_list(s):
    for item in s:
        if item in punctuation_marks:
            s = s.replace(item," ")
    
    return s




# approch 4
# using the join function
# join function create a single stirng from the multiple strings.
# it used separator which separate the string. 


def removing_punctuation_4(s):
    result = ''.join(item for item in s if item not in punctuation_marks)
    return result


print(removing_punctuation_4(s))




# approch 5
# using the str.maketrans
# using the string.translate()

"""
str is a class and maketrans is a class method which create the 
transaltion table in which the element are mapped. 

maketrans() take three parameter, first one is item you want to replace . for example "abc" . 

second one is to replace the abc with this one. like "123" 

thrid one is element you want to remove from the string. 

tip: 
     the lenght of  the first and second parameter in the make_trans will be equal because translation table map the element. 


After creating the translation table the translate function is the string is used to implies the translatio table into a string. 
"""
import string


def remove_punctuation_5(s):
    create_translation_table = str.maketrans(" "," ",string.punctuation)
    return s.translate(create_translation_table)


print(remove_punctuation_5(s))