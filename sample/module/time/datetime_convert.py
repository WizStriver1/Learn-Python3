# -*- coding: utf-8 -*-
import datetime, time

format_str='%Y-%m-%d %H:%M:%S'

def strpstamp(string, format_str='%Y-%m-%d %H:%M:%S'):
    return time.mktime(time.strptime(string, format_str))


def strfstamp(seconds, format_str='%Y-%m-%d %H:%M:%S'):
    return datetime.strftime(string, format_str)



now = datetime.datetime.now()
print(now.strftime(format_str))

string = '2019-01-01 00:00:00'
strptime = datetime.datetime.strptime(string, format_str)
print(strptime)
print(strptime.strftime(format_str))

print(datetime.datetime.fromtimestamp(time.time()))
print(datetime.datetime.utcfromtimestamp(time.time()))

print(time.time())

print(strpstamp(now.strftime(format_str)))