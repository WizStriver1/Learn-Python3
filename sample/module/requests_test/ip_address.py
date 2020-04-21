# -*- coding: utf-8 -*-
import requests, json, re

from ip_pools import ip_list

for ip in ip_list:
  r = requests.get('http://ip.ws.126.net/ipquery?ip=%s' % ip)
  matchObj = re.match(r'.*lo="([^"]*)".*lc="([^"]*)".*', r.text, re.M|re.I)

  with open('ip_address.txt', 'a') as f:
    f.write('省份： %s，城市： %s；\n' % (matchObj.group(1).encode('utf-8'), matchObj.group(2).encode('utf-8')))