#!/usr/bin/env python
# _*_coding:utf_8_*_
# Author:Alvin.xie
# get filename
fname = raw_input('Enter filename: ')
print


# attempt to open file for reading
try:
    fobj = open(fname, 'r')
except IOError, e:
    print "*** file open error:", e
else:
    # display contents to the screen
    for eachLine in fobj:
        print eachLine,
    fobj.close()