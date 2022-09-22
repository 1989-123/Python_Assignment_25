"""
 Write a python script to add the new method in SmartPhone 
class which accepts Truecaller object as a parameter and 
call the fetch method of Truecaller. 
"""

class Truecaller:

    def __init__(self):
        self.name = "Jayesh"
        self.number = 8200066734

    def set_name(self, name):
        return self.name

    def get_name(self, number):
        self.number = number
        return self.name

    def set_number(self, number):
        return self.number
        t1.get_name()

    def get_number(self, number, t1):
        return self.number
        return self.get_name(self)

    def new_entry(self, t1):
        self.email = "pj92147@gmail.com"
        return self.email


class SmartPhone(Truecaller):

    def fetch(self, t1):
        t1.new_entry()


t1 = Truecaller()
s1 = SmartPhone()
print()
print(s1.new_entry(t1))
print()
