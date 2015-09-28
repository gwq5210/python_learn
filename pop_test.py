#!/usr/bin/env python
# coding=utf-8

import poplib
import email
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

email = raw_input('Email:')
password = raw_input('Password:')
pop3_server = raw_input('POP3 Server:')

server = poplib.POP3(pop3_server)
server.set_debuglevel(1)
print server.getwelcome()
server.user(email)
server.pass_(password)
print 'Message: %s. Size %s' % server.stat()
resp, mails, octets = server.list()
print mails
index = len(mails)
resp, lines, octets = server.retr(index)
msg_content = '\r\n'.join(lines)
msg = Parser().parsestr(msg_content)
print msg
server.quit()
