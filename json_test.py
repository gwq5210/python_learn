#!/usr/bin/env python
# coding=utf-8

import json
d = dict(name = 'gwq', age = 20, score = 90)
print d
s = json.dumps(d)
print s
t = json.loads(s)
print t
print type(d), type(s), type(t)

class Student(object):
	def __init__(self, name, age, score):
		self.name = name
		self.age = age
		self.score = score
	#def __str__(self):
	#	return 'name: %s, age: %d, score: %d.' % (self.name, self.age, self.score)
	#__repr__ = __str__
def stu2dict(stu):
	return {'name': stu.name, 'age': stu.age, 'score': stu.score}
def dict2stu(d):
	return Student(d['name'], d['age'], d['score'])

stu = Student('gsj', 20, 95)
print stu, type(stu)
s = json.dumps(stu, default = stu2dict)
print s, type(s)
t = json.loads(s, object_hook = dict2stu)
print t, type(t)
