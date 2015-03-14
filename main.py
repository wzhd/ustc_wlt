#!/usr/bin/env python3

import os
import requests

keypath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'passwd')
keyfile = open(keypath,'r')
name, password = keyfile.readline().strip().split(' ')
port = 7  #出口


#login
data = dict(cmd='login', url='URL', ip='', name=name, password=password,
            go='登录账户')
request_url = "http://wlt.ustc.edu.cn/cgi-bin/ip"

res = requests.post(request_url, data=data)


#开通网络通
params = dict(cmd ='set', url='URL', type=port, exe=0, go='开通网络')
res = requests.post("http://wlt.ustc.edu.cn/cgi-bin/ip?%s" % params)

print("ok")
