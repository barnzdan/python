#!/usr/bin/env python


"""
1. It takes arguments for: timeout, url, expected_response_code, retry_count
2. The script performs an HTTP GET for the url
3. If the HTTP response code matches the expected_response_code the script will exit with status code 0
4. If the the HTTP GET either times out or the HTTP response code doesn't match, retry until retry count is exhausted
5. If the retry count is exhausted without receiving the expected_response_code, print an error message to STDERR and exit with a non zero status code.
"""

import os, sys, httplib, socket

#
# verify number of arguments
#
args = len(sys.argv)
if not args == 5:
    print "Usage: %s {timeout|url|expected_ response|retry_count}" % \
                     os.path.basename(sys.argv[0])  
    sys.exit(1)

# 
# redirect stderr to null class
#
class NullWriter:
    def write(self, s):
        pass

sys.stderr = NullWriter()

#
# assign the args
#
TimeOut = (sys.argv[1])
site = (sys.argv[2])
ExpectResponse = (sys.argv[3])
RetryCount = (sys.argv[4])

#
#  connect
#
i = 0
t = int(RetryCount)
while i < t:
    c = str(t - i)
    ConnectString = httplib.HTTPConnection(site, 80, TimeOut)
    ConnectString.request("GET", "/")
    Response = ConnectString.getresponse()
    sock = socket.socket()
    sock.settimeout(8.2)
    ConnectString.close()
    if Response.status == httplib.OK:
        print "URL is OK"
        sys.exit(0)
    else:
        print "URL did not connect as expected."
        print "Will attempt the connection " + c + " more times."
        i += 1
sys.exit(1)
