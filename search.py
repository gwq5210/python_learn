#!/usr/bin/env python
# coding=utf-8

import os
import sys
if len(sys.argv) != 3:
	print 'Usage: ./search.py <dir> <text>'
	exit(0);
d = sys.argv[1]
t = sys.argv[2];
def search(d, t):
	res = []
	dirs = [os.path.join(d, x) for x in os.listdir(d) if os.path.isdir(os.path.join(d, x))]
	for y in dirs:
		tmp = search(y, t)
		for a in tmp:
			res.append(a)
	files = [x for x in os.listdir(d) if os.path.isfile(x) and x.find(t) != -1]
	for y in files:
		res.append(y)
	return res
print 'answer:', search(d, t)
