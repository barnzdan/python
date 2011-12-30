#!/usr/bin/env python

import subprocess

proc = subprocess.Popen([ 'ssh', 'dlb@172.16.1.6'], 'cat > %s' % filename ],
                        stdin = subprocess.PIPE)
proc.communicate(file_contents)
if proc.retcode != 0:
    print 'We have a problem'
sys.exit(1)
