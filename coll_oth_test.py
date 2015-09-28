#!/usr/bin/env python
# coding=utf-8

from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print p.x, p.y

import hashlib
md5 = hashlib.md5()
md5.update('gwq5210')
print md5.hexdigest()
