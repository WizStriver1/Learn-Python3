#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import functools

def addnum(func):
    @functools.wraps(func)
    def wrapper(args):
        func(args, 'WizStriver')

    return wrapper

@addnum
def copy(content, user):
    print("copy's name is %s" % copy.__name__)
    print(content)
    print('    -- %s' % user)

copy("Hello, I like ice cream");