#!/usr/bin/env python3

import script1
from imp import reload
import imp
imp.reload(script1)


import myfile
t = myfile.title
print (t)

from myfile import title
print (title)
