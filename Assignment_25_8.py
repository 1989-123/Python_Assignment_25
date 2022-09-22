"""
Write a python script to create a SmartPhone class by 
inheriting Calculator 2.0 and Phone Class 
"""

class Calculater_2:

    def __init__(self):
        self.a = None
        self.b = None

    def __mul__(self):
        print(self.a * self.b)

    def __floordiv__(self):
        print(self.a // self.b)

class Phone:

    def calling(self):
        print("Calling...")

    def sms(self):
        print("sms received...")

class SmartPhone(Calculater_2, Phone):

    def show(self):
        print("Someone is calling...")

s1 = SmartPhone()
s1.show()
