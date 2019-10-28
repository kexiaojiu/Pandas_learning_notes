# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 22:57:04 2019

@author: kejie
"""

import urllib.request
url="http://www.baidu.com"
get=urllib.request.urlopen(url).read()
print(get)