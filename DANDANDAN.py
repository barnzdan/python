#!/usr/bin/python

import os,sys

passwd="/etc/passwd"
if not os.path.isfile(passwd):
    print "Can't open %s." % passwd
    sys.exit(1)


format="%-18s  %-17s  %10s %-9s"
print format % ("", "", "Disk ", "")
print format % ("Username (UID)", "Home Directory",
                           "Space", "Security")
print "---------------------------------------------\
---------------"
for line in open(passwd).readlines():
    (uname, xpass, uid, gid, junk, home_dir, junk2) = line.split(':')
    if uname == 'root' or uname == 'nobody' or uname[0:2] == 'uu':
        continue
    uid = int(uid)
    if uid <= 100 and uid > 0:
        continue
    if uid == 0 and uname != 'root':
        warn = "** UID=0"
    elif xpass != '!' and xpass != '*' and xpass != 'x':
        warn = "** CK PASS"
    else:
        warn = ""
    if os.path.isdir(home_dir) and home_dir != '/':
        disk = os.popen("du -s -k %s 2>/dev/null" %
                         home_dir).read().split('\t')[0]
        if disk == '':
            disk = "unknown"
        else:
            disk += "K"
    else:
        disk = "skipped"
    print format % ("%s (%s)" % (uname, uid), home_dir, \
           disk, warn)

'''
doc 
'''
