#!/usr/bin/env python
# coding=utf-8

name = raw_input("please enter your name:");
print "hello", name;
a = 100;
if a >= 0:
	print a;
else:
	print -a;
print 0xffff;
# 多行字符串
print '''line1
line2
line3''';
print 3 > 2;
print "中文";
print len("中文");
print len(u"中文");
print "hello, %s, %d" % (name, 100);
a = [1, 2, 3];
print a[0];
a = 10;
s = 0;
while a > 0:
	s += a;
	a = a - 1;
print s;
