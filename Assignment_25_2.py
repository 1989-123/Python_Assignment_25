"""
Write a python script to update the above Profile 
class with encapsulation. 
"""

class Profile:

    def __init__(self):
        self.name = None
        self.email = None
        self.age = None

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age


p1 = Profile()
print()
p1.set_name("Jayesh")
print(p1.get_name())
print()
