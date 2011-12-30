#!/usr/bin/env python

import os

if os.path.isfile("/etc/passwd"):
    print "passwd is a file"     
else:
    print "passwd is not a file"    
