op# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 22:43:56 2019

@author: kejie
"""

import urllib.request
import time
from bs4 import BeautifulSoup
import re
def getPM25(cityname):
    site = 'http://www.pm25.com/city/' + cityname+'.html'
#    try:
    html = urllib.request.urlopen(site)
    soup = BeautifulSoup(html,"html5lib")
    city = soup.find("span",{"class":"city_name"})
    aqi = soup.find("a",{"class":"cbol_aqi_num"})
    pm25 = soup.find("span",{"class":"cbol_nongdu_num_1"})
    pm25danwei = soup.find("span",{"class":"cbol_nongdu_num_2"})
    quality = soup.find("span",{"class":re.compile('cbor_gauge_level\d$')})
    result = soup.find("div",{"class":'cbor_tips'})
    replacechar = re.compile("<.*?>") 
    space = re.compile(" ")
    print(city.string + " aqi = "+aqi.string)
    return int(aqi.string)
#    except Exception:
#        print("catched exception")
#        return -1
    
    
if __name__ == '__main__':  
    while True:
        aqi = getPM25('qingdao')
        if aqi == -1:
            time.sleep(1)
            continue