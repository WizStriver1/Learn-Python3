# -*- coding: utf-8 -*-
import re, os, urlparse

path = 'https://fonts.googleapis.com/css?family=Domine:400,700'
matchObj = re.match(r'.*\/([^\/\?]+)?(\?.*)?', path, re.M|re.I)
if matchObj:
  print(matchObj.group())
  print(matchObj.group(1))
  print(matchObj.group(2))