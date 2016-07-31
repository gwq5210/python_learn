#!/usr/bin/env python
# coding=utf-8

from selenium import webdriver

url = 'https://login.taobao.com/member/login.jhtml'
#driver = webdriver.PhantomJS()
driver = webdriver.Chrome()
print driver.get(url)
print driver.title
print driver.current_url
print driver.find_element_by_tag_name('img')
#cookies =  driver.get_cookies()
