#!/usr/bin/env python
# coding=utf-8

def is_odd(x):
	if x % 2 == 1:
		return True;
	else:
		return False;
print filter(is_odd, [1, 2, 3]);
