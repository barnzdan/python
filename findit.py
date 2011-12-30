#!/usr/bin/env python

import re, sys

#file = "sys.argv[1]"

def run_re():
    #pattern = 'sys.argv[0]'
    pattern = 'html'

    infile = open('large_re_file.txt', 'r')
    match_count = 0
    lines = 0
    for lines in infile:
        match = re.search(pattern, line)
        if match:
            match_count += 1
        lines += 1
    return(lines, match_count)

if __name__== "__main__":
    lines, match_count = run_re()
    print 'LINES::', lines
    print 'MATCHES::', match_count
