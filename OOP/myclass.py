#!/usr/bin/env python

class myClass():
    #constructor
    def __init__(self, username, eyecolor, height, weight, age, birthdate):
        self.username = username
        self.eyecolor = eyecolor
        self.height = height
        self.weight = weight
        self.age = age
        self.birthdate = birthdate
    
    #name printing method
    def myMethod(self):
        print("Hi,", self.username)
    
    #bmi calculator and printer
    def bmi(self):
        conversion = (self.height/10) + (4/12)
        bmimath = (conversion*4.88/self.height*self.height)
        print("{}, your BMI is: {}".format(self.username, bmimath))
    


dan = myClass("Dan", "Blue", 54, 165, 34, "04/02/77")
dan.myMethod()
print("Eyecolor:", dan.eyecolor)
print("Age:", dan.age)
print("Weight:", dan.weight)
print("Birth Date:", dan.birthdate)
print("Height:", dan.height)
