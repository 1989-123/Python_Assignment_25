"""
Write a python script to create a Calculator class 
with 2 methods for adding and subtracting 2 values.
"""

class Calculater:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self):
        print(self.a + self.b)

    def __sub__(self):
        print(self.a - self.b)

c1 = Calculater(50, 20)
c2 = Calculater(80, 40)

print()
c1.__add__()
c2.__add__()
print()
c1.__sub__()
c2.__sub__()
print()
