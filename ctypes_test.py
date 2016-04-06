#!/usr/bin/env python
# coding=utf-8

from ctypes import *;
import os;

#libtest = CDLL(os.getcwd() + '/multiply.so')
#print libtest.multiply(2, 3)

lib = CDLL("./lib.so");
s = "nihao";
lib.display_sz(s);
print "done!"
lib.display(s);
print "done!!"
