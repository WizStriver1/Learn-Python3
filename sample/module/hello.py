#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'WizStriver1'

import sys

def test():
	args = sys.argv
	print('args', args)
	if len(args) == 1:
		print('Hello, %s!' % args[0])
	elif len(args) == 2:
		print('Meet again, %s!' % args[1])
	else:
		print('Too many arguments!')

print(__name__)
import foo
print(foo.foo_var)
# if __name__ == '__main__':
	
    # hello()