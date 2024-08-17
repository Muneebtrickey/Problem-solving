# problem

"""
Write a Python class, Flower, that has three instance variables of type str,
int, and float, that respectively represent the name of the flower, its number of petals, and its price. Your class must include a constructor method
that initializes each variable to an appropriate value, and your class should
include methods for setting the value of each type, and retrieving the value
of each type.
"""



# code 

class Flower:
    def __init__(self, name: str, number_of_petals: int, price: float):
        self.flower_name = name
        self.flower_petals = number_of_petals
        self.flower_price = price
    
    def set_flower_name(self, name: str):
        self.flower_name = name
    
    def set_flower_petals(self, flower_petals: int):
        self.flower_petals = flower_petals 
    
    def set_flower_price(self, flower_price: float):
        self.flower_price = flower_price
    
    def get_flower_name(self):
        return self.flower_name
    
    def get_flower_petals(self):
        return self.flower_petals
    
    def get_flower_price(self):
        return self.flower_price

# Example usage
flower = Flower("imran", 20, 1000.0)

print(flower.get_flower_name())
print(flower.get_flower_petals())
print(flower.get_flower_price())

# Updating the attributes
flower.set_flower_name("Rose")
flower.set_flower_petals(50)
flower.set_flower_price(150.0)

# Checking if the values have changed
print(flower.get_flower_name())
print(flower.get_flower_petals())
print(flower.get_flower_price())

