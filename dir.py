#!/usr/bin/env python
# coding=utf-8

import os
print os.name
print os.uname()
#print os.environ
print os.getenv('PATH')

cur = os.path.abspath('.')
new = os.path.join(cur, 'abc')
print cur, new
print os.path.split(new)
