#!/usr/bin/env python

# ex6.py

x = "There are %d types of people." % 10
binary = "binary"
do_not = "dont't"
y = "Those who know %s and those %s." % (binary, do_not)


print x 
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
