#!/usr/bin/env python
# coding=utf-8

def fac(n):
	if (n == 0):
		return 1;
	else:
		return n * fac(n - 1);

print fac(5);

import os;
print [d for d in os.listdir(".")]
