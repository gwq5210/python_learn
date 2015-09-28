#!/usr/bin/env python
# coding=utf-8

import socket
import os
import time
def tcplink(sock, addr):
	print 'accept new connection from %s:%s' % addr
	sock.send('Welcome!')
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		if data == 'exit' or not data:
			break
		sock.send('Hello, %s' % data)
	sock.close()
	print 'connection from %s:%s closed' % addr
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8888))
s.listen(1024)
while True:
	sock, addr = s.accept()
	p = os.fork()
	if p == 0:
		tcplink(sock, addr)
s.close()
