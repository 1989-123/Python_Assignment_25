"""
Write a python script to update 2nd Question, add a class variable 
(platform) and create a classmethod to access it.
"""

class Profile:

    company = "Macleods pharmaceuticlas ltd"

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

    @classmethod
    def get_company(cls):
        return cls.company

p1 = Profile()
print()
print(Profile.get_company())
print()
