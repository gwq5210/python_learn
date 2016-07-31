#!/usr/bin/env python
# coding=utf-8

import urllib, urllib2, cookielib, re

class taobao:
    def __init__(self):
        self.login_url = 'https://login.taobao.com/member/login.jhtml'
        self.username = '18576716709'
        self.pwd = '64c37e39a227570e3410feee97792a030d19a6fa9185c88f478e7c5e200d17ff259d98c8c872d2129b28b864eb483cb1280ef0d4d607cf68cd971a15a9e97a4923ce10d85769128d4a343909f15e9dd6d3c0162a66818b8c6690e51d12c4b97fcad2c3c975186c190109b0b1c23b23924f8ec5950a29ecfcdcf2e91a017a1416'
        self.ua = '076#Kf2PUQPncx2PDAcaPPPPPKN5vqf51OAf0sd6vUDkaiWENpQaECpdyRmnxOQ/eBkRpnXSXUMz4UYl57t6DCfnFanOqct0Z+QcPcVqAW+Q3VcZXQC1Lvqs/m0dao3sje47F6T7zLwcPc0Kg7kDkdwiyAzq5xT/BcwEsYTf5y14Pc7gwA2PUMWbvH/l7mamCQ1zno1a2GIrxoUz9+6PqL+YP8PEhodDveov9vVxcmhtd+QLULVdzFO0BQPexYwcPc0Kg7kDkdLwyAzq5xT/BcwEsYTf5y14Pc7gwA2PUMWbvH/lkU6mCQ1zno1a2GIrxoUz9+6PqL+YP8PEhodDveolGvVxcmhtd+QLULVdzFO0BQPexYwcPc0Kg7kDkdZEyAzq5xT/BcwEsYTf5y14Pc7gBP2PUA1C1OiOAutZPcKKaev8hCz+zccCtNNDhmN3KA2PuD/enbNucGHp06iMXayfxfLNTkZxgA2PcPPPav2WP8PH/ehSnbfRuLlZQDfMQb2nuxboJ6zWP8PH/eTSnbOAuLlZQDfMQb2nuxboJ6gmP8P2PPPfa3QcPcVqA5PfM3cZXQCxEOqs/T0ddx2wPt47F6T7z8wcPPpy320S5Pi/schMP8PJ1ANpJqtjGm9XvLE6Upi0hhjDUvI7gA2PcPPPav2AP8PUXqETHO7QpP2PCUkcaUoKvb0HqA2PsU9a1H2ucZ09oIfNQ8HuS8Egvqbcc8HPFU9aZz2uc8cVoIfNQ8HuPUA+P8ikIwtR+v2/bKOBmIEMabvSpnbNqjs7xnWln5aUqRLOSEihdjdMabvSpnbNPfz/zSvx+5HDUBFnN+SuAYJyavZz0y4kl7Fl0oT4R1wnJGFXrgO0Rf9eDm//pZUSjfC7zbT4R1wnUOM/mKgrS73Zdxif0bmICcQg5ZZE6b62XxyntEZkVI3Zdxi/AgvNPfz/zSvx+mP2vr7lrMnSSpfiUjYrGsZpXHgEumhZRS91XowZho0vAH6JWOZ/GbFSqP1oDNrZtZ3ouYNfmVSORiQGw9nQGyLAUp3lpmnrd1KM8LC4rRNYpG+2gcvzBZNhCcQH5n1Fd1KM8LCAP8PUPAVkTI3kqP2PcqJLj22NP8PlqG9YV2dOdbRXUFf7IEugMBMqAwFch8wcPPpy3c0SFPi/sqQCP8PKvWPkSN+PthA6PA2PCH9AiZS2P4MV/PwcPPpy3aOSk8i/s4QYP8PqgOEDveo5oxVcPP8PPi2fBP2PiPCClOC9AutZPwhGaoVcPP8PPi2fKA2PuD/MnbN6VGHp06iMXayfxfLNTkZxBP2PiPCClOC9AutZPP79aoVcPP8PPi2fBP2PiPCCXvC/AutZPP+caL3cPcve/oNSgd+JKESP/uOizL6HnddXhh3cPcve/xNSgWMJKESP/uOizL6HnddXhhwcPcXKb2kDkgcWyAzq5aspWGaPqCYh5y1aP8PFc+Kba4yPXk6PI1PfkDiwsOYQ22x/b+/x59AYP8PEhodDveoXCiVxcmhtd+QLULVdzFO0BQPex5VcPP8PPi2fwA2PUMWbvH/lkgHmCQ1zno1a2GIrxoUz9+6PqL+YP8PEhodDveoJhiVxcmhtd+QLULVdzFO0BQPexYwcPc0Kg7kDkdvVyAzq5xT/BcwEsYTf5y14Pc7gwA2PUMWbvH/l7A7mCQ1zno1a2GIrxoUz9+6PqL+='
        self.login_headers =  {
            'Host': 'login.taobao.com',
            'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36',
            'Referer' : self.login_url,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Connection' : 'Keep-Alive'
        }
        self.values = {
                'TPL_username': self.username,
                'TPL_password': '',
                'ncoSig': '',
                'ncoSessionid': '',
                'ncoToken': '907c726fa301d5e94e8ca75c5d89f9fccde83c50',
                'slideCodeShow': 'false',
                'lang': 'zh_CN',
                'loginsite': '0',
                'newlogin': '0',
                'TPL_redirect_url': 'http://buyer.trade.taobao.com/trade/itemlist/list_bought_items.htm',
                'from': 'tb',
                'fc': 'default',
                'style': 'default',
                'css_style': '',
                'keyLogin': 'false',
                'qrLogin': 'true',
                'newMini': 'false',
                'newMini2': 'false',
                'tid': '',
                'loginType': '3',
                'minititle': '',
                'minipara': '',
                'pstrong': '',
                'sign': '',
                'need_sign': '',
                'isIgnore': '',
                'full_redirect': '',
                'sub_jump': '',
                'popid': '',
                'callback': '',
                'guf': '',
                'not_duplite_str': '',
                'need_user_id': '',
                'poy': '',
                'gvfdcname': '',
                'gvfdcre': '68747470733A2F2F6C6F67696E2E74616F62616F2E636F6D2F6D656D6265722F6C6F676F75742E6A68746D6C3F73706D3D613231626F2E35303836322E3735343839343433372E372E6B445170435126663D746F70266F75743D7472756526726564697265637455524C3D68747470732533412532462532467777772E74616F62616F2E636F6D253246',
                'from_encoding': '',
                'sub': '',
                'TPL_password_2': self.pwd,
                'loginASR': '1',
                'loginASRSuc': '1',
                'allp': '',
                'oslanguage': 'zh-CN',
                'sr': '1920*1080',
                'osVer': '',
                'naviVer': 'chrome|49.0262375',
                'miserHardInfo': '',
                'um_token': 'HV01PAAZ0ab8132624249919579d880d0006256a',
                'ua': ' self.ua'
                }
        self.data = urllib.urlencode(self.values)
        self.proxy_host = 'http://120.193.146.97:843'
        self.proxy_handler = urllib2.ProxyHandler({'http': self.proxy_host})
        self.cookie = cookielib.MozillaCookieJar()
        self.cookie_handler = urllib2.HTTPCookieProcessor(self.cookie)
        self.opener = urllib2.build_opener(self.cookie_handler, self.proxy_handler)

    def is_need_iden_code(self):
        req = urllib2.Request(self.login_url, self.data, self.login_headers)
        res = self.opener.open(req)
        content = res.read()
        print content
        status = res.getcode()
        if status == 200:
            print 'get response success!'
            pattern = re.compile('请输入验证码', re.S)
            result = re.search(pattern, content)
            if result:
                print 'please input verify code!'
                return content
            else:
                print "don't neet verify code!"
                return None
        else:
            print 'get response failed!'

    def start(self):
        self.is_need_iden_code()

spider = taobao()
spider.start()
