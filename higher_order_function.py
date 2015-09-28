#!/usr/bin/env python
# coding=utf-8

def add_abs(x, y, fun):
	return fun(x) + fun(y);
print add_abs(10, -5, abs);
