#!/usr/bin/env python

# THIS IS A COMMENT


from random import choice

import string

def GenPasswd(length=8, chars=string.letters+string.digits):
    return ''.join([ choice(chars) for i in range(length) ])
