# ！/usr/bin/env python
# -*- coding：utf-8 -*-
import urllib.request

response = urllib.request.urlopen('http://www.baidu.com')
print(response.status)
print(response.read())
print(response.headers)
