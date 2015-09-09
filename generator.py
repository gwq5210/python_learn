#!/usr/bin/env python
# coding=utf-8

l = [x * x for x in range(10) if x % 2 == 0];
print l;
g = (x * x for x in range(10) if x % 2 == 0);
print g;
for x in g:
	print x;

def fib(max):
	n, a, b = 0, 0, 1;
	while n < max:
		print b;
		a, b = b, a + b;
		n = n + 1;
fib(8);
def fib_g(max):
	n, a, b = 0, 0, 1;
	while n < max:
		yield b;
		a, b = b, a + b;
		n = n + 1;
print fib_g(8);
for n in fib_g(8):
	print n;
