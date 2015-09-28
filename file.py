#!/usr/bin/env python
# coding=utf-8

try:
	f = open('file.py', 'r')
	s = f.read()
	print s;
finally:
	if f:
		f.close()
with open('nofile', 'r') as f:
	print f.read()
