# problem


"""
Draw a class inheritance diagram for the following set of classes:
• Class Goat extends object and adds an instance variable tail and
methods milk( ) and jump( ).
• Class Pig extends object and adds an instance variable nose and
methods eat(food) and wallow( ).
• Class Horse extends object and adds instance variables height and
color, and methods run( ) and jump( ).
• Class Racer extends Horse and adds a method race( ).
• Class Equestrian extends Horse, adding an instance variable weight
and methods trot( ) and is trained( ).
"""


class Goat(object):
    def __init__(self, tail):
        self.tail = tail
    
    def milk(self):
        print("Goat gives milk.")
    
    def jump(self):
        print("Goat is jumping.")


class Pig(object):
    def __init__(self):
        self.nose = "Pig nose"
    
    def eat(self, food):
        print(f"The pig eats the {food}.")
    
    def wallow(self):
        print("The pig is wallowing in the mud.")


class Horse(object):
    def __init__(self, height, color):
        self._height = height
        self._color = color
    
    def run(self):
        print("The horse is running.")
    
    def jump(self):
        print("The horse is jumping.")


class Racer(Horse):
    def __init__(self, height, color):
        super().__init__(height, color)
    
    def race(self):
        print("The horse is racing.")


class Equestrian(Horse):
    def __init__(self, height, color, weight):
        super().__init__(height, color)
        self._weight = weight
    
    def trot(self):
        print("The horse is trotting.")
    
    def is_trained(self):
        print("The horse is trained.")
