#!/usr/bin/env python
# coding=utf-8

from wsgiref.simple_server import make_server
from web_hello import application
httpd = make_server('', 8000, application)
print 'Server HTTP on port 8000...'
httpd.serve_forever()
