#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
class controlled_execution:
    def __enter__(self):
        set things up
        return thing
    def __exit__(self, type, value, traceback):
        tear things down

with controlled_execution() as thing:
     some code
'''
# with use in filesystem
# with open('file.txt', 'r') as f:
#     print(f.read())
class Test(object):
    def __enter__(self):
        print('enter')
        return 1

    def __exit__(self, a, b, c):
        print('exit: %s, %s, %s, %s' % (self, a, b, c))
        return 2

with Test() as t:
    print('in with %s' % t)