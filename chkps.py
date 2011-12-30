#!/usr/bin/python

import commands, os, string

program = raw_input("Enter the name of the program to check: ")

try:
    #perform a ps command and assign results to a list
    output = commands.getoutput("ps -aux|grep " + program)
    proginfo = string.split(output)

    #display results
    print "\n\
    Full path:\t\t", proginfo[5], "\n\
    Owner:\t\t\t", proginfo[0], "\n\
    Process ID:\t\t", proginfo[1], "\n\
    Parent process ID:\t", proginfo[2], "\n\
    Time started:\t\t", proginfo[4]
except:
    print "There was a problem with the program."
