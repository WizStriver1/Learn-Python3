# -*- coding: utf-8 -*-

path = "http://vrlab.swpu.edu.cn:8080/virexp/s/chunk/"

import urllib2

import os

def file_exists(filepath):
  return os.path.exists(filepath)

def mkdir(dirname):
  if not os.path.isdir(dirname):
    os.mkdir(dirname)
  return dirname

def get_page(pathname):
  url = path + pathname
  try:
    response = urllib2.urlopen(url)
  except urllib2.URLError as e:
    print(url)
    print(e)
    return False

  html = response.read()

  with open(pathname, 'w') as f:
    f.write(html)

  from bs4 import BeautifulSoup
  soup = BeautifulSoup(html, 'html.parser')
  for res in soup.findAll('img'):
    src = res.get('src')
    imageurl = path + src
    src_split = src.split('/')
    if len(src_split) > 1:
      mkdir(src_split[0])

    try:
      img = urllib2.urlopen(imageurl).read()
      with open (src, 'wb') as f: f.write(img)
    except urllib2.URLError as e:
      print(imageurl)
      print(e)

  for res in soup.findAll('a'):
    for content in res.contents:
      if content.encode('utf-8') == '下一页':
        get_page(res.get('href'))

get_page('index.html')