#!/usr/bin/env python
# coding=utf-8
def str2int(s):
	def char2int(c):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[c];
	def fn(x, y):
		return x * 10 + y;
	return reduce(fn, map(char2int, s));
print str2int('134');
print '134';
