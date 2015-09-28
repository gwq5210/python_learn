#!/usr/bin/env python
# coding=utf-8

import os
print 'process (%s) start ...' % os.getpid()
#pid = os.fork()
#if pid == 0:
#	print 'This is child process %s and my parent is %s' % (os.getpid(), os.getppid())
#else:
#	print 'I %s just created a child process %s' % (os.getpid(), pid)

from multiprocessing import Process
def run_proc(name):
	print 'Run child process %s (%s)' % (name, os.getpid())

p = Process(target = run_proc, args = ('test',))
print 'process will start'
p.start()
p.join()
print 'Process end'
