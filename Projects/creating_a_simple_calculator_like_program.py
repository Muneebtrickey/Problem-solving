# project

"""
Write a Python program that can simulate a simple calculator, using the
console as the exclusive input and output device. That is, each input to the
calculator, be it a number, like 12.34 or 1034, or an operator, like + or =,
can be done on a separate line. After each such input, you should output
to the Python console what would be displayed on your calculator.


"""



# writing code directly



def simulate_calculator():
    operations = []
    while True:
        num = input("Enter your number: ")
        operations.append(float(num))   


        operator = input("Enter (+,-,*,/) and = for the result: ")

        if operator == "=":
            break

        operations.append(operator)



    i = 0 
    while i < len(operations):
        # first of all we will check multiplication and divison
        if operations[i] == "*":
            result = operations[i-1] * operations[i+1]
            operations[i-1:i+2] = [result]
            i -= 1
        
        elif operations[i] == "/":
            result = operations[i-1] / operations[i+1]
            operations[i-1:i+2] = [result]
            i -= 1
        else:
            i += 1
    

    i = 0

    while i < len(operations):
        
        if operations[i] == "+":
            result = operations[i-1] + operations[i+1]
            operations[i-1:i+2] = [result]
            i -= 1

        elif operations[i] == "-":
            result = operations[i-1] - operations[i+1]
            operations[i-1:  i +2] = [result]
            i -= 1
        
        else:
            i += 1
    
    return operations[0]



print(simulate_calculator())




# approch 2 

# using the eval function


def simulate_calculator_2():
    expression = ""
    
    while True:
        number = input("Enter a number: ")
        operator = input("Enter an operator: ")

        expression += number
        if operator == "=":
            break
        expression += operator

    
    result = eval(expression)
    return result



print(simulate_calculator_2())