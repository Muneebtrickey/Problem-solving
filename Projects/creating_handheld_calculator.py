# project
# problem


"""
Write a Python program that simulates a handheld calculator. Your program should process input from the Python console representing buttons
that are “pushed,” and then output the contents of the screen after each operation is performed. Minimally, your calculator should be able to process
the basic arithmetic operations and a reset/clear operation.
"""



# directly writing the code


def simulate_calculator():
    expressions = ""

    while True:
        command = input("Press Buttons to do operations:  (input) ,(add),(mul),(div),(=) ,(clear or reset) :  ")

    
        
        
        if command == "input":
            number = input("Enter your number: ")
            expressions += number
           

        elif command == "add":
            expressions += "+"

        elif command == "mul":
            expressions += "*"

        elif command == "div":
            expressions += "/"

        elif command == "sub":
            expressions += "-"

        elif command == "=":
            break
        elif command == "clear" or command == "reset":
            expressions = ""
    

    result = eval(expressions)
    return result



print(simulate_calculator())


