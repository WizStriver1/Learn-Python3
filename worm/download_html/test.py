# -*- coding: utf-8 -*-
import re, os, urlparse

line = 'http://www.baidu.com/test/test1/'

print(urlparse.urljoin(line, '../index.html'))