# -*- coding: utf-8 -*-

path = "http://modelicabyexample.globalcrown.com.cn/"

import urllib2, os, re, urlparse

def file_exists(filepath):
  return os.path.exists(filepath)

def mkdir(dirname):
  if not os.path.isdir(dirname):
    os.mkdir(dirname)
  return dirname

def mkdirtree(pathdirs):
  dirpath = os.getcwd()
  pathdirs = remove_back_sign(pathdirs)
  for dirname in pathdirs.split('/'):
    if not dirname == '':
      dirpath = os.path.join(dirpath, dirname)
      if not file_exists(dirpath):
        os.mkdir(dirpath)
  return dirpath

def remove_first_slash(path):
  if path.startswith('/'):
    path = path[1:]
    return remove_first_slash(path)
  return path

def remove_back_sign(src):
  if src.startswith('../'):
    src = src[3:]
    return remove_back_sign(src)
  return remove_first_slash(src)

def get_page_root_path(path):
  matchObj = re.match(r'(.*\/?)([^\/]*\.html.*)?', path, re.M|re.I)
  if matchObj:
    return matchObj.group(1)
  else:
    return ''

def get_page(url=''):
  print('Download page: %s' % url)
  try:
    response = urllib2.urlopen(url)
  except urllib2.URLError as e:
    print(url)
    print(e)
    return False

  html = response.read()

  pathname = url.split(path)[1]
  pagename = pathname + 'index.html'

  mkdirtree(pathname)
  with open(pagename, 'w') as f:
    f.write(html)

  from bs4 import BeautifulSoup
  soup = BeautifulSoup(html, 'html.parser')
  for res in soup.findAll('img'):
    src = res.get('src')
    imageurl = urlparse.urljoin(url, src)
    src_split, imagename = os.path.split(src)
    mkdirtree(src_split)
    try:
      img = urllib2.urlopen(imageurl).read()
      with open(os.path.join(os.getcwd(), remove_back_sign(src)), 'wb') as f: f.write(img)
    except urllib2.URLError as e:
      print(imageurl)
      print(e)

  for res in soup.findAll("div", {"class": "right menu"}):
    new_res = res.find('a')
    # print(res)
    if new_res:
      get_page(urlparse.urljoin(url, new_res.get('href')))

if __name__ == '__main__':
  get_page(path)