#!/usr/bin/env python
# coding=utf-8

import urllib, urllib2, cookielib

url = 'http://www.zhihu.com/'
values = {}
values['name'] = 'user'
values['pwd'] = 'pwd'
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36'
headers = {'User-Agent': user_agent}
data = urllib.urlencode(values)
print 'encode url:' + data

# proxy
proxy_handler = urllib2.ProxyHandler({'http': 'http://proxy.com:8080'})
opener = urllib2.build_opener(proxy_handler)
urllib2.install_opener(opener)

# cookie
cookie_file = "cookie.txt"
#cookie = cookielib.CookieJar()
#cookie.load(cookie_file, ignore_discard=True, ignore_expires=True)
cookie = cookielib.MozillaCookieJar(cookie_file)
handle = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handle)
urllib2.install_opener(opener)

req = urllib2.Request(url, data, headers)
try:
    rsp = urllib2.urlopen(req, timeout = 1)
    print rsp.read()
except urllib2.HTTPError, e:
    print e.code
    print e.reason
except urllib2.URLError, e:
    print e.reason
else:
    print 'ok'
for item in cookie:
    print 'name = ' + item.name
    print 'val = ' + item.value
cookie.save(ignore_discard = True, ignore_expires = True)
