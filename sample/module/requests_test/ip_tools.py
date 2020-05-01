# -*- coding: utf-8 -*-
import requests, json, re

def get_address(ip):
  if not ip:
    return '省份:  , 城市:  ;\n'
  r = requests.get('http://ip.ws.126.net/ipquery?ip=%s' % ip)
  matchObj = re.match(r'.*lo="([^"]*)".*lc="([^"]*)".*', r.text, re.M|re.I)
  
  result = '省份:  %s, 城市:  %s;\n' % (matchObj.group(1).encode('utf-8'), matchObj.group(2).encode('utf-8'))

  return result