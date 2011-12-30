#!/usr/bin/env python

# open file

f = open("/tmp/foo.txt", "r")
lines = f.readlines()
print lines
f.close()
#print f

