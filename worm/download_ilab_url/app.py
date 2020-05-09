# -*- coding: utf-8 -*-

import requests, json, re

limit = 9
url_list = []
for i in range(300):
  start = limit * i + 1
  path = "http://www.ilab-x.com/json/projects?status=1&del=0&proLevel=1&isToDeclare=1&limit=%d&start=%d&sortby=pubSeq&reverse=true&ts=1588988935570" % (limit, start)
  try:
    r = requests.get(path)
    r_data = json.loads(r.text)
  except Exception as e:
    continue
  for data in r_data['data']:
    with open('url.txt', 'a') as f:
      matchObj = re.match(r'http(s)?:\/\/([^\d^\/]+)\/.*', data['url'], re.M|re.I)
      if matchObj:
        hostname = matchObj.group(2)
        if hostname not in url_list:
          url_str = '%s %s-%s\n' % (hostname, data['schoolTitle'], data['title'])
          f.write(url_str.encode('utf-8'))
          url_list.append(hostname)
