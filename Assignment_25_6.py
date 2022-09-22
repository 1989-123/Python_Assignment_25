"""
Write a python script to create a Calculator 2.0 class 
with 2 methods for multiplication and division of 
2 values and inherit it from the Calculator class 
"""


class Calculater_2:

    def __init__(self):
        self.a = a
        self.b = b

    def __mul__(self):
        print(self.a * self.b)

    def __floordiv__(self):
        print(self.a // self.b)


class Calculater (Calculater_2):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self):
        print(self.a + self.b)

    def __sub__(self):
        print(self.a - self.b)


c1 = Calculater(100, 20)
c1.__floordiv__()
