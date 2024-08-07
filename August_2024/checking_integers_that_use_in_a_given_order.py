# Problem

"""
Write a short program that takes as input three integers, a, b, and c, from
the console and determines if they can be used in a correct arithmetic
formula (in the given order), like “a+b = c,” “a = b−c,” or “a ∗ b = c.”
"""


def correct_arithmetic_order():
    first_value = int(input("Enter your first number: "))
    second_value = int(input("Enter your second number: "))
    third_value = int(input("Enter your third number: "))

    if (first_value + second_value) == third_value:
        return True
    elif first_value == (second_value - third_value):
        return True
    elif (first_value * second_value) == third_value:
        return True
    else:
        return False
    


print(correct_arithmetic_order())





# another way of writing this code 


def correct_arithmetic_order_2():
    first_value = int(input("Enter your first number: "))
    second_value = int(input("Enter your seconed number : "))
    third_value = int(input('Enter you third number: '))

    return True if (first_value + second_value) == third_value  else True if third_value == (second_value - first_value) else True if (first_value * second_value ) == third_value else False


print(correct_arithmetic_order_2())