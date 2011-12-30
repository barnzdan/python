#!/usr/bin/env python

"""1. It takes arguments for: timeout, url, expected_response_code, retry_count
   2. The script performs an HTTP GET for the url
   3. If the HTTP response code matches the expected_response_code the script will exit with status code 0
   4. If the the HTTP GET either times out or the HTTP response code doesn't match, retry until retry count is exhausted
   5. If the retry count is exhausted without receiving the expected_response_code, print an error message to STDERR and exit with a non zero status code.
"""

import sys
import urllib


if not len(sys.argv) == 4:
    print 'Must have the parms: {timeout|url|expected repsonse|retry count}'
sys.exit(1)


