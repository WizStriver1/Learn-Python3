# -*- coding: utf-8 -*-
import requests, json

from ip_tools import *

rest_port = "5050"
r = requests.get('http://119.23.40.38:%s/api/v1/uiexprecord?_disable_page_=true&_order_column=createtime&_order_style=desc' % rest_port)
# r = requests.get('http://119.23.40.38:%s/api/v1/uiexprecord?get_records&iscook=true&_disable_page_=true&_order_column=createtime&_order_style=desc' % rest_port)
# r = requests.get('http://119.23.40.38:%s/api/v1/uiexprecord?get_records&iscook=true&_order_column=createtime&_order_style=desc' % rest_port)

r_data = json.loads(r.text)

def get_user_ip(userautoid):
  r = requests.get('http://119.23.40.38:%s/api/v1/log?page=1&per_page=1&_order_column=createtime&userautoid=%s' % (rest_port, userautoid))

  r_data = json.loads(r.text)

  if len(r_data['data']['result']):
    return r_data['data']['result'][0]
  return {}

def get_user(userautoid):
  r = requests.get('http://119.23.40.38:%s/api/v1/user?autoid=%s' % (rest_port, userautoid))
  r_data = json.loads(r.text)

  if len(r_data['data']['result']):
    return r_data['data']['result'][0]
  return {}

# record = r_data['data']['result'][0]

# print(record)

# print(get_user(record['userautoid']))
# print(get_user_ip(record['userautoid']))

def get_default_str(val):
  if val:
    return val
  else:
    return ''

with open('ip_address.txt', 'w') as f:
  f.write('')


for record in r_data['data']['result']:
  user_data = get_user(record.get('userautoid'))
  ip_data = get_user_ip(record.get('userautoid'))
  address = get_address(ip_data.get('ip'))

  with open('ip_address.txt', 'ab') as f:
    realname = get_default_str(user_data.get('realname'))
    number = get_default_str(user_data.get('number'))
    life = get_default_str(record.get('life'))
    f.write("用户: %s, 学号: %s, 实验时长: %s, %s" % (realname.encode('utf-8'), number.encode('utf-8'), life.encode('utf-8'), address))
    # f.write("用户: %s" % realname.encode('utf-8'))
    # f.write("用户: %s" % number.encode('utf-8'))
    # f.write("用户: %s" % life.encode('utf-8'))
    # f.write("用户: %s" % address)