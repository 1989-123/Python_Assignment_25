"""
Write a python script to create a Phone class with 2 methods 
to print the features (calling and sms).
"""

class Phone:

    def calling(self):
        print("Calling...")

    def sms(self):
        print("sms received...")

p1 = Phone()
p1.calling()
p1.sms()
