#!/usr/bin/env python
# coding=utf-8

def lazy_sum(*nums):
	def my_sum():
		res = 0;
		for n in nums:
			res = res + n;
		return res;
	return my_sum;
s = lazy_sum(*[1, 2, 4, 3]);
print s;
print s();
f = lambda x: x * x;
print f(5);
