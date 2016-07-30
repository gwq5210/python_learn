#!/usr/bin/env python
# coding=utf-8

import urllib, urllib2, re

class qiubai:
    def __init__(self):
        self.read_timeout = 10
        self.page_idx = 1
        self.user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36'
        self.headers = {'User-Agent': self.user_agent}
        self.stories = []
        self.enable = True
        self.base_url = 'http://www.qiushibaike.com/text/page/'
        self.re_str = '<div.*?author.*?>.*?<h2>(.*?)</h2>.*?<div.*?content.*?>(.*?)</div>.*?<span class="stats-vote"><i class="number">(.*?)</i>'
        self.pattern = re.compile(self.re_str, re.S)
        self.replace_br_str = '<.*?>'
        self.replace_br_pattern = re.compile(self.replace_br_str)

    def get_page(self, idx):
        url = '%s%d' % (self.base_url, idx)
        req = urllib2.Request(url, headers = self.headers)
        try:
            print 'get content from url: %s' % url
            rsp = urllib2.urlopen(req, timeout = self.read_timeout)
            rsp_txt =  rsp.read()
            print 'get page %d success!' % idx
            return rsp_txt
        except urllib2.URLError, e:
            print 'get page %d failed, reason: %s' % (idx, e.reason)
            return None

    def get_page_items(self, idx):
        html = self.get_page(idx)
        if not html:
            return None
        print 'find page %d all stories' % idx
        items = re.findall(self.pattern, html)
        print 'find success!'
        page_stories = []
        for item in items:
            text = re.sub(self.replace_br_pattern, '\n', item[1])
            page_stories.append([item[0].strip(), text.strip(), item[2].strip()])
        return page_stories

    def load_page(self):
        if self.enable:
            if len(self.stories) < 2:
                page_stories = self.get_page_items(self.page_idx)
                if page_stories:
                    self.stories.append(page_stories)
                    self.page_idx += 1
                else:
                    print 'page stories none'

    def get_one_story(self, page_stories, now_page):
        for story in page_stories:
            print 'page %d' % now_page
            print 'author %s' % story[0]
            print 'like %s' % story[2]
            print 'content\n%s' % story[1]

            input = raw_input()
            if input == 'q':
                self.enable = False
                return
            self.load_page()

    def start(self):
        print 'enter for new story, "q" for quit'
        now_page = 0
        while self.enable:
            self.load_page()

            if len(self.stories) > 0:
                page_stories = self.stories[0]
                del self.stories[0]
                now_page += 1
                self.get_one_story(page_stories, now_page)

spider = qiubai()
spider.start()
