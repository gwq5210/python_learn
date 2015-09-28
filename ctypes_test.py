#!/usr/bin/env python
# coding=utf-8

from ctypes import *
import os
libtest = cdll.LoadLibrary(os.getcwd() + '/multiply.so')
print libtest.multiply(2, 3)
