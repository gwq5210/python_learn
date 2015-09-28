#!/usr/bin/env python
# coding=utf-8

from email.mime.text import MIMEText
from email.header import Header
from email import encoders
from email.utils import parseaddr, formataddr
def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr(( \
			Header(name, 'utf-8').encode(), \
			addr.encode('utf-8') if isinstance(addr, unicode) else addr))
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
from_addr = raw_input('From:')
password = raw_input('Password:')
smtp_server = raw_input('SMTP server:')
to_addr = raw_input('To:')
msg['From'] = _format_addr('gwq <%s>' % from_addr)
msg['To'] = _format_addr('gsj <%s>' % to_addr)
msg['Subject'] = Header('test', 'utf-8').encode()

import smtplib
server = smtplib.SMTP(smtp_server, 25)	#默认端口号是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
