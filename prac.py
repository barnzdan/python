#!/usr/bin/env python

# this is a comment

def main() :
    t = raw_input("Your entry here: ")
    print 'Your string is %s!' % t
    print "The first letter of your string is: %s" % t[0]
    print "The last letter of your string is: %s" % t[-1]
    print "Your string in upper: %s" % t.upper()
    print "Your string in lower: %s" % t.lower()
    print "Your string in title form: %s" % t.title()
    print "Here is your string split: %s" % t.split()
    print "Here is your string tabbed: %s" % '\t'.join(t)
    print "Here is your string joined: %s" % ''.join(t)
    print "Here is your string replaced: %s" % t.replace("This", "That")

if __name__ == "__main__":
    main()
