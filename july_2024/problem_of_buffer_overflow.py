#problem

"""
we need to write a code in which it catch an exception which occur due to index out of bounds in a list. 

"""


# code which catch the exception 


# lets creats a list which will have 5 element and everyone value 0.

List = [0] * 5 

# now we will add the value to the list using indexes

for i in range(10): # we want to add 10 values but our list limit 5. 
    try:
        name = input("Enter your name: ")
        List[i] = name   # if the i is 4 so the list will be full
                         # and exception will be arise

    except IndexError:
        print("Don't try buffer overflow in python!. ")
        break



# approch 2
# using while loop



List2 = [0] * 5
i = 0
while True:
    try:
        name = input("enter your name: ")
        List2[i] = name
    except IndexError:
        print("Don't try buffer overflow in python. ")
        break
    i += 1




# approch 3
# pre_check then add element

List3 = [0] * 5

for i in range(100):
    if i < len(List3):
        name = input("Enter your name: ")
        List3[3] = name
    else:
        print("don't try buffer overflow in python")





