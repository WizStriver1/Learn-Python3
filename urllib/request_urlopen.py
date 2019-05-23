# -*- coding: utf-8 -*-
from urllib import request
import json

url = 'https://api.douban.com/v2/book/2129650'
url = 'http://119.23.40.38:9100'

# urllib.request.urlopen() returns a http.client.HTTPResponse object
with request.urlopen(url) as f:
    data = f.read()
    headers = f.getheaders()
    msg = f.msg
    v = f.version
    status = f.status
    reason = f.reason
    debuglevel = f.debuglevel
    closed = f.closed
    print(type(f))
    print(f)