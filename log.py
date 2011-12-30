#!/usr/bin/env python

try:
    import sys

    logfile = open('/tmp/mylog.txt', 'a')
    print >> logfile, 'Fatal error: invalid input!'
    logfile.close()

except:
    print 'Could not pull this off'
