"""
Write a python script to update 2nd Question,
change email and age to __email and __age. 
"""

class Profile:

    def __init__(self):
        self.name = None
        self.__email = None
        self.__age = None

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

p1 = Profile()
p1.set_age = 35
p1.set_age = 'pj92147@gmail.com'
p1.get_age()
