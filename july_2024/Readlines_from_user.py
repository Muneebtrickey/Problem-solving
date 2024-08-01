# problem

"""
we need to print the lines in the reverse order when the file is end. 
"""

List = []
print("Enter your line and if you want to exit so press (ctrl + z)")
try:
    while True:
        read_line = input("Enter your line: ")
        List.append(read_line)
        
except EOFError:   # i am only focus on the end of the file
    print("The file is ended: ")

finally:
    while List:
        print(List.pop()) # this will print in the reverse order



# approches

# we can do the following problem using different approches
# in th  above is used stack , we can use deque from collections
 # module
 # we can also do it to reverse the list



# using deque

from collections import deque
lines = deque()

try:
    while True:
        input_data = input("Enter your line: ")
        lines.append(input_data)

except EOFError:
    print("End of the file. ")

finally: 
    while lines:
        print(lines.pop())








# approach 3 
# using reverse list


List2 = []

try:
    while True:
        inputs = input("Enter your line: ")
        List2.append(inputs)


except EOFError:
    print("End of the file . ")

finally:
    for item in reversed(List2):
        print(item)




# approch 4
# we will be using the sys module and in the sys module we will 
# be using the stdin (standard input) object and in the object we 
# will use the readlines() method 




import sys 
print("Enter your line press ctrl + z if you want to end.")
try:
    lines = sys.stdin.readlines()

except EOFError:
    print("End of the file. ")

finally:
    for item in reversed(lines):
        print(item.strip())




