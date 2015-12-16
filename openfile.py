#!/usr/bin/env python

# open file

with open("/tmp/foo.txt", "r") as f:
  lines = f.readlines()
  print lines
  #print f

