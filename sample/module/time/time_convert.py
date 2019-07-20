# -*- coding: utf-8 -*-
import time

def strpstamp(string, format_str='%Y-%m-%d %H:%M:%S'):
    return time.mktime(time.strptime(string, format_str))

def strfstamp(seconds=time.time(), format_str='%Y-%m-%d %H:%M:%S'):
    return time.strftime(format_str, time.localtime(seconds))

def strfstamp2(seconds=time.time(), format_str='%Y-%m-%d %H:%M:%S'):
    return time.strftime(format_str, time.gmtime(seconds))

stamp = time.time()
print(strfstamp(stamp))
print(strfstamp2(stamp))

def nextday(seconds=time.time()):
    minute = 60
    hours = 60 * minute
    day = 24 * hours
    return seconds + day

def strfnextday(string):
    return strfstamp(nextday(strpstamp(string)))

string = '2019-01-01 00:00:00'
print(strpstamp(string))
print(strfnextday(string))