#!/usr/bin/env python
# coding=utf-8

import time, threading
def loop():
	print 'thread %s is running ...' % threading.current_thread().name
loop()
t = threading.Thread(target = loop, name = 'newthread')
t.start()
t.join()
print 'thread %s end' % threading.current_thread().name
