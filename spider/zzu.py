#!/usr/bin/env python
# coding=utf-8

import urllib, urllib2, cookielib

source_encode = 'gbk'
target_encode = 'utf-8'
read_timeout = 3
url = 'http://jw.zzu.edu.cn/scripts/qscore.dll/search'
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36'
headers = {'User-Agent': user_agent, 'Referer': 'http://jw.zzu.edu.cn/'} 
values = {}
values['nianji'] = '2012'
values['xuehao'] = '20122430205'
values['mima'] = '482694'
values['selec'] = 'http://jw.zzu.edu.cn/scripts/qscore.dll/search'
data = urllib.urlencode(values)
req = urllib2.Request(url, data, headers)

cookie_file = 'zzu.txt'
cookie = cookielib.MozillaCookieJar(cookie_file)
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
urllib2.install_opener(opener)

rsp_file = 'zzu.html'

def save(filename, s):
    f = open(filename, 'w')
    f.write(s)

try:
    rsp = urllib2.urlopen(req, timeout = read_timeout)
    cookie.save(ignore_discard = True, ignore_expires = True)
    rsp_txt =  rsp.read()
    rsp_txt = rsp_txt.decode(source_encode).encode(target_encode)
    print rsp_txt
    save(rsp_file, rsp_txt)
except urllib2.HTTPError, e:
    print e.code
    print e.reason
except urllib2.URLError, e:
    print e.reason
else:
    print 'ok'
