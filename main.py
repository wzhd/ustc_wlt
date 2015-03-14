#!/usr/bin/env python3

import urllib.request
import urllib.parse
import http.cookiejar
import os

keypath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'passwd')
keyfile = open(keypath,'r')
name, password = keyfile.readline().strip().split(' ')
port = 7  #出口

#cookie
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

#login
data = urllib.parse.urlencode({'cmd':'login','url':'URL','ip':'','name':name,
                               'password':password,'go':'登录账户'})
data = data.encode('utf-8')
request = urllib.request.Request("http://wlt.ustc.edu.cn/cgi-bin/ip")

request.add_header("Content-Type","application/x-www-form-urlencoded")

f = opener.open(request,data)
#print(f.read().decode('gb2312'))
#print(f.info())

#开通网络通
params = urllib.parse.urlencode({'cmd':'set','url':'URL','type':port,'exe':0,
                                   'go':'开通网络',})
#params = params.encode('utf-8')
res = opener.open("http://wlt.ustc.edu.cn/cgi-bin/ip?%s" % params)
#print(f.read().decode('gb2312'))
print("ok")
