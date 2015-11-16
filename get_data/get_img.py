#!/usr/bin/env python
# coding=utf-8

import urllib2, urllib, cookielib, re, time, os;

debug = 0;
sleepTime = 0.5; #s
encode = "gb2312";
baseUrl = "http://www.qlql11.com";
imgSrc = r'<img.*?src="(.*?)".*?>';
urlSrc = r'<a href="(.*?)".*?>';
imgExt = ".jpg";
prefixStr = "http://www.qlql11.com/a/jingpintupian/yazhouyouhuo/2";
url = "http://www.qlql11.com/a/jingpintupian/yazhouyouhuo/list_12_";
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.99 Safari/537.36",
        "Referer": "http://www.qlql11.com/", "Connection": "keep-alive"};

def AddBaseUrl(url):
    return baseUrl + url;

def mkdir(path):
    path = path.strip()
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        return False

class GetImg:
    def __init__(self, siteUrl):
        self.url = siteUrl;
        self.data = None;
        self.imgPattern = re.compile(imgSrc);
        self.urlPattern = re.compile(urlSrc);
        self.imgUrlList = [];

    def GetData(self, dataUrl):
        cookie = cookielib.CookieJar();
        httpHander = urllib2.HTTPHandler(debuglevel = debug);
        httpsHander = urllib2.HTTPSHandler(debuglevel = debug);
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie), httpHander, httpsHander);
        urllib2.install_opener(opener);

        print "get data from " + dataUrl + " start!";
        req = urllib2.Request(dataUrl, None, headers);
        try:
            rsp = urllib2.urlopen(req, timeout = 1);
            print "get data from " + dataUrl + " end!";
            return rsp.read().decode(encode);
        except Exception, e:
            print e;
            return None;

    def GetPage(self):
        self.data = self.GetData(self.url);

    def GetImgUrl(self):
        if self.data == None:
            print "data is None!\n";
            return;
        if self.data != None:
            urlList = self.urlPattern.findall(self.data);
        urlList = map(AddBaseUrl, urlList);
        urlSetTmp = set(urlList);
        urlSet = set();
        for urlTmp in urlSetTmp:
            if urlTmp.startswith(prefixStr):
                urlSet.add(urlTmp);
        print urlSet;
        print len(urlSet);
        for urlTmp in urlSet:
            text = self.GetData(urlTmp);
            if text != None:
                self.imgUrlList += self.imgPattern.findall(text);

    def SaveImg(self, imgUrl, fileName):
        f = open(fileName, "wb");
        try:
            imgData = urllib2.urlopen(imgUrl, timeout = 1).read();
            print "save img url(" + imgUrl + ") to file " + fileName + ".";
            f.write(imgData);
            f.close();
        except Exception, e:
            print e;

    def Run(self, path):
        self.GetPage();
        self.GetImgUrl();
        print "img url list:\n";
        print self.imgUrlList;
        print "img url list end\n";
        fileName = 1;
        print len(self.imgUrlList);
        for imgUrl in self.imgUrlList:
            self.SaveImg(imgUrl, path + str(fileName) + imgExt);
            time.sleep(sleepTime);
            fileName = fileName + 1;

r = range(1, 100);
for idx in r:
    time.sleep(sleepTime);
    s = GetImg(url + str(idx) + ".html");
    mkdir(str(idx));
    s.Run(str(idx) + "/");
