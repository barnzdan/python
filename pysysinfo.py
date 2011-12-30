#!/usr/bin/env python

#A System Information Gathering Script

import subprocess

def namer():
    print __name__
        
#Command 1
def unamer():
    uname = "uname"
    uname_arg = "-a"
    print "Gathering system information with %s command:\n" % uname
    subprocess.call([uname, uname_arg])
        
#Command 2
def diskspacer():
    diskspace = "df"
    diskspace_arg = "-h"
    print "Gathering diskspace information %s command:\n" % diskspace
    subprocess.call([diskspace, diskspace_arg])

def main():
    unamer()
    diskspacer()

#main()

if __name__ == "__main__":
    main() 
