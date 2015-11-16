#!/usr/bin/env python
# coding=utf-8

import urllib;
import urllib2;
import cookielib;

values = {"nianji" : "2012", "xuehao": "20122430205", "mima":"482694", "selec": "http://jw.zzu.edu.cn/scripts/qscore.dll/search"};
data = urllib.urlencode(values);
cookie = cookielib.CookieJar();
httpHander = urllib2.HTTPHandler(debuglevel = 1);
httpsHander = urllib2.HTTPSHandler(debuglevel = 1);
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie), httpHander, httpsHander);
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.99 Safari/537.36",
        "Referer": "http://www.qlql11.com/", "Connection": "keep-alive"};
urllib2.install_opener(opener);
#url = "http://jw.zzu.edu.cn/scripts/qscore.dll/search";
#url = "http://www.qlql11.com/a/jingpintupian/yazhouyouhuo/";
url = "http://www.qlql11.com/";
#request = urllib2.Request(url, data);
request = urllib2.Request(url, None, headers);

try:
    response = urllib2.urlopen(request);
    html =  response.read().decode("GBK");
    print html;
except urllib2.HTTPError, e:
    print e.code;
    print e.reason;
except urllib2.URLError, e:
    print e.reason;

